/* HubAuth: optional Google sign-in + cloud copy of your progress, via Supabase.
 *
 * Anonymous by default: everything keeps working from this browser's storage.  When the server has SUPABASE_URL and
 * SUPABASE_ANON_KEY set (see README), people can sign in with Google; their quiz history and marking scheme are then
 * copied to Supabase (table rows protected by Row Level Security) and merged back on any device.
 *
 * Nothing here is loaded for anonymous visitors until they ask: supabase-js is fetched only on the account page, on
 * sign-in, or when a saved session exists.
 */
(function (w) {
  'use strict';
  var SDK = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js';
  var cfg = null, sb = null, user = null, ready, status = 'anon', lastSync = null, lastError = '', listeners = [];

  function emit() { var s = state(); listeners.forEach(function (f) { try { f(s); } catch (e) {} }); document.dispatchEvent(new CustomEvent('hubauth', { detail: s })); }
  function state() { return { enabled: !!(cfg && cfg.enabled), user: user, status: status, lastSync: lastSync, error: lastError }; }
  function on(f) { listeners.push(f); f(state()); }

  function hasSavedSession() {
    try { for (var i = 0; i < localStorage.length; i++) { var k = localStorage.key(i); if (/^sb-.*-auth-token$/.test(k)) return true; } } catch (e) {}
    return false;
  }
  function loadSdk() {
    return new Promise(function (res, rej) {
      if (w.supabase && w.supabase.createClient) return res();
      var s = document.createElement('script'); s.src = SDK; s.onload = res; s.onerror = function () { rej(new Error('Could not load the sign-in library.')); };
      document.head.appendChild(s);
    });
  }
  function getConfig() {
    return fetch('/api/config', { cache: 'no-store' }).then(function (r) { return r.json(); }).then(function (c) { cfg = c; return c; })
      .catch(function () { cfg = { enabled: false }; return cfg; });
  }
  function client() {
    if (sb) return Promise.resolve(sb);
    return loadSdk().then(function () {
      sb = w.supabase.createClient(cfg.url, cfg.anonKey, { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true } });
      sb.auth.onAuthStateChange(function (ev, session) {
        var u = session && session.user || null, changed = (u && u.id) !== (user && user.id);
        user = u;
        if (u) { status = 'signed-in'; emit(); if (changed || ev === 'SIGNED_IN') setTimeout(sync, 0); }
        else { status = 'anon'; emit(); }
      });
      return sb.auth.getSession().then(function (r) {
        user = r.data && r.data.session ? r.data.session.user : null; status = user ? 'signed-in' : 'anon'; emit();
        if (user) sync();
        return sb;
      });
    });
  }

  /* init(): call on every hub page.  Loads the SDK only when needed. */
  function init(force) {
    if (ready) return ready;
    ready = getConfig().then(function (c) {
      if (!c.enabled) { status = 'disabled'; emit(); return state(); }
      if (force || hasSavedSession() || /[#?&](access_token|code)=/.test(location.href)) return client().then(state);
      emit(); return state();
    }).catch(function (e) { lastError = e.message; emit(); return state(); });
    return ready;
  }

  function ensureClient() { return init().then(function () { return cfg && cfg.enabled ? client() : null; }); }
  function signIn() {
    return ensureClient().then(function () {
      if (!sb) throw new Error('Accounts are not set up on this site yet.');
      return sb.auth.signInWithOAuth({ provider: 'google', options: { redirectTo: location.origin + '/account', queryParams: { prompt: 'select_account' } } });
    });
  }
  function signOut() { return ensureClient().then(function () { return sb.auth.signOut(); }).then(function () { user = null; status = 'anon'; lastSync = null; emit(); }); }

  /* ---- cloud copy ---- */
  function toRow(a) { return { id: a.id, ts: a.ts, subject: a.subject, data: a }; }
  function pushAttempt(a) {
    if (!sb || !user || !a) return Promise.resolve();
    return sb.from('attempts').upsert(toRow(a), { onConflict: 'user_id,id' }).then(function (r) { if (r.error) throw r.error; });
  }
  function pushSettings() {
    if (!sb || !user || !w.HubMarking) return Promise.resolve();
    return sb.from('user_settings').upsert({ user_id: user.id, marking: w.HubMarking.get(), updated_at: new Date().toISOString() }, { onConflict: 'user_id' })
      .then(function (r) { if (r.error) throw r.error; });
  }
  /* Merge both ways: cloud rows we do not have are added locally; local attempts the cloud lacks are uploaded. */
  function sync() {
    if (!sb || !user) return Promise.resolve();
    status = 'syncing'; lastError = ''; emit();
    return sb.from('attempts').select('id,data').order('ts', { ascending: false }).limit(1000).then(function (r) {
      if (r.error) throw r.error;
      var remote = r.data || [], remoteIds = {}, added = 0;
      remote.forEach(function (x) { remoteIds[x.id] = 1; });
      if (remote.length && w.HubStore) added = w.HubStore.importJSON(JSON.stringify({ attempts: remote.map(function (x) { return x.data; }) }));
      var local = w.HubStore ? w.HubStore.read().attempts : [];
      var missing = local.filter(function (a) { return !remoteIds[a.id]; }).map(toRow);
      var up = missing.length ? sb.from('attempts').upsert(missing, { onConflict: 'user_id,id' }) : Promise.resolve({});
      return up.then(function (u) { if (u && u.error) throw u.error; return added; });
    }).then(function (added) {
      return sb.from('user_settings').select('marking,updated_at').maybeSingle().then(function (r) {
        if (r.error) throw r.error;
        if (r.data && r.data.marking && w.HubMarking) { localStorage.setItem('hub.marking', JSON.stringify(r.data.marking)); }
        else return pushSettings();
      }).then(function () { lastSync = Date.now(); status = 'signed-in'; emit(); if (added) document.dispatchEvent(new CustomEvent('hubstore-changed')); return added; });
    }).catch(function (e) { status = 'signed-in'; lastError = (e && e.message) || 'Sync failed'; emit(); });
  }
  function deleteCloud() {
    if (!sb || !user) return Promise.resolve();
    return sb.from('attempts').delete().eq('user_id', user.id).then(function () { return sb.from('user_settings').delete().eq('user_id', user.id); }).then(function () { lastSync = Date.now(); emit(); });
  }

  /* Save every new quiz to the cloud too (hub pages patch record; dashboard result pages call pushAttempt). */
  function hookStore() {
    if (!w.HubStore || w.HubStore._hooked) return; w.HubStore._hooked = true;
    var rec = w.HubStore.record;
    w.HubStore.record = function (a) { var att = rec.call(w.HubStore, a); if (att && (user || hasSavedSession())) { ensureClient().then(function () { return pushAttempt(att); }).catch(function (e) { lastError = e.message; emit(); }); } return att; };
  }
  hookStore();

  w.HubAuth = { init: init, on: on, state: state, signIn: signIn, signOut: signOut, sync: sync, pushAttempt: pushAttempt, pushSettings: pushSettings, deleteCloud: deleteCloud };
})(window);
