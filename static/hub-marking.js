/* HubMarking: the marking scheme (correct / incorrect / unanswered), kept in this browser.
 * Default is +2 / -1 / 0.  Used by:
 *   - the quiz setup page of every dashboard (a small panel is injected before the Start button),
 *   - every quiz result page (a "Marks" card is injected after the score),
 *   - the hub's mixed quiz (quiz-mixed.js calls the same API).
 * Cloud sync (hub-auth.js) carries the scheme along with the account. */
(function (w) {
  'use strict';
  var KEY = 'hub.marking', DEF = { c: 2, w: -1, u: 0 };
  function num(v, d) { v = parseFloat(v); return isFinite(v) ? Math.max(-100, Math.min(100, v)) : d; }
  function get() {
    try { var s = JSON.parse(localStorage.getItem(KEY) || 'null'); if (s) return { c: num(s.c, DEF.c), w: num(s.w, DEF.w), u: num(s.u, DEF.u) }; } catch (e) {}
    return { c: DEF.c, w: DEF.w, u: DEF.u };
  }
  function set(s) {
    s = { c: num(s.c, DEF.c), w: num(s.w, DEF.w), u: num(s.u, DEF.u) };
    try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {}
    if (w.HubAuth && w.HubAuth.pushSettings) w.HubAuth.pushSettings();
    return s;
  }
  function sign(n) { return (n > 0 ? '+' : n < 0 ? '−' : '') + Math.abs(n); }
  function label(s) { s = s || get(); return sign(s.c) + ' correct · ' + sign(s.w) + ' incorrect · ' + sign(s.u) + ' unanswered'; }
  /* rows: [ok, ...] where ok is 1 right, 0 wrong, -1 skipped.  Pass an array of ok values. */
  function score(oks, s) {
    s = s || get();
    var c = 0, x = 0, u = 0;
    oks.forEach(function (o) { if (o === 1) c++; else if (o === 0) x++; else u++; });
    var marks = c * s.c + x * s.w + u * s.u;
    return { marks: Math.round(marks * 100) / 100, max: Math.round(oks.length * Math.max(s.c, 0) * 100) / 100, right: c, wrong: x, skipped: u, scheme: s };
  }
  function fmtScore(r) { return sign(r.marks).replace('+', '') + ' / ' + r.max; }

  var CSS = '.hm-panel{border:1px solid #d9d3c2;border-radius:10px;background:#fff;padding:14px 18px;margin:16px 0;font:14px/1.5 system-ui,sans-serif;color:#1c2420}' +
    '.hm-panel h3{margin:0 0 4px;font-size:15px}.hm-panel p{margin:0 0 10px;color:#5f6b63;font-size:13px}' +
    '.hm-row{display:flex;gap:14px;flex-wrap:wrap;align-items:flex-end}.hm-row label{display:flex;flex-direction:column;gap:4px;font-size:12px;font-weight:600;color:#5f6b63}' +
    '.hm-row input{width:84px;padding:7px 9px;border:1px solid #d9d3c2;border-radius:8px;font:inherit;font-size:15px;color:#1c2420}' +
    '.hm-row button{padding:8px 12px;border:1px solid #d9d3c2;border-radius:8px;background:#faf8f3;font:inherit;font-size:13px;cursor:pointer}' +
    '.hm-card{margin:14px 0;padding:14px 18px;border:1px solid #d9d3c2;border-radius:10px;background:#fff;font:14px/1.5 system-ui,sans-serif;color:#1c2420}' +
    '.hm-card .big{font-size:26px;font-weight:700}.hm-card small{color:#5f6b63;display:block}';
  function css() { if (document.getElementById('hm-css')) return; var s = document.createElement('style'); s.id = 'hm-css'; s.textContent = CSS; document.head.appendChild(s); }

  /* The editable panel.  `host` receives it; values are saved on every change. */
  function panel(host, before) {
    css();
    var s = get(), el = document.createElement('div'); el.className = 'hm-panel'; el.id = 'hm-panel';
    el.innerHTML = '<h3>Marking scheme</h3><p>Used for the score on the result screen. Defaults: +2 correct, −1 incorrect, 0 unanswered. Change it any time, e.g. 4 / −1 / 0 or 1 / 0 / 0.</p>' +
      '<div class="hm-row"><label>Correct<input type="number" step="any" id="hm-c" value="' + s.c + '"></label><label>Incorrect<input type="number" step="any" id="hm-w" value="' + s.w + '"></label>' +
      '<label>Unanswered<input type="number" step="any" id="hm-u" value="' + s.u + '"></label><button type="button" id="hm-reset">Reset to +2 / −1 / 0</button></div>';
    if (before) host.insertBefore(el, before); else host.appendChild(el);
    function read() { set({ c: el.querySelector('#hm-c').value, w: el.querySelector('#hm-w').value, u: el.querySelector('#hm-u').value }); }
    el.addEventListener('input', read); el.addEventListener('change', read);
    el.querySelector('#hm-reset').onclick = function () { set(DEF); el.querySelector('#hm-c').value = DEF.c; el.querySelector('#hm-w').value = DEF.w; el.querySelector('#hm-u').value = DEF.u; };
    return el;
  }

  /* Dashboard quiz result pages: add a Marks card under the score block. */
  function banner(oks) {
    css();
    var r = score(oks), el = document.createElement('div'); el.className = 'hm-card'; el.id = 'hm-card';
    el.innerHTML = '<div class="big">Marks: ' + r.marks + ' / ' + r.max + '</div><small>' + r.right + ' right × ' + sign(r.scheme.c) + ', ' + r.wrong + ' wrong × ' + sign(r.scheme.w) + ', ' + r.skipped + ' unanswered × ' + sign(r.scheme.u) + '</small>';
    var anchor = document.querySelector('.score-hero');
    if (anchor) anchor.insertAdjacentElement('afterend', el);
    else { var res = document.getElementById('results'); if (res) res.insertBefore(el, res.firstChild); else document.body.insertBefore(el, document.body.firstChild); }
    return r;
  }

  /* Setup pages: the script tag carries data-mode="setup". */
  function mountSetup() {
    var form = document.querySelector('form[action*="quiz/start"]'); if (!form || document.getElementById('hm-panel')) return;
    var btn = form.querySelector('button[type=submit],#start-btn,#go,.start-btn'), at = btn ? btn.parentNode : null;
    if (at === form) panel(form, btn); else if (at) panel(at.parentNode, at); else panel(form);
  }
  var me = document.currentScript;
  if (me && me.dataset.mode === 'setup') { if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountSetup); else mountSetup(); }

  w.HubMarking = { get: get, set: set, score: score, label: label, sign: sign, fmtScore: fmtScore, panel: panel, banner: banner, DEFAULT: DEF };
})(window);
