/* HubStore: quiz history for every subject, kept in this browser (localStorage).
 *
 * One attempt = { id, ts, subject, mode, secs, total, answered, correct, rows }
 *   subject: a subject slug, or "mixed" for the cross-subject quiz
 *   mode:    "subject" (taken inside a dashboard) | "mixed"
 *   rows:    [ [subjectSlug, sectionLabel, bloomLevel, ok], ... ]   ok: 1 right, 0 wrong, -1 skipped
 *
 * When Supabase is added, only read()/write()/record() need to change.
 */
(function (w) {
  'use strict';
  var KEY = 'hub.v1', MAX_ATTEMPTS = 400, mem = null;

  function read() {
    try {
      var raw = localStorage.getItem(KEY);
      if (raw) { var d = JSON.parse(raw); if (d && Array.isArray(d.attempts)) return d; }
    } catch (e) { /* storage blocked or corrupt */ }
    return mem || { v: 1, attempts: [] };
  }
  function write(d) {
    mem = d;
    try { localStorage.setItem(KEY, JSON.stringify(d)); return true; } catch (e) { return false; }
  }
  function uid() { return Date.now().toString(36) + Math.random().toString(36).slice(2, 6); }

  function record(a) {
    var rows = (a.rows || []).filter(function (r) { return r && r.length === 4; });
    if (!rows.length) return null;
    var answered = rows.filter(function (r) { return r[3] !== -1; }).length;
    var correct = rows.filter(function (r) { return r[3] === 1; }).length;
    var att = { id: uid(), ts: Date.now(), subject: a.subject, mode: a.mode || 'subject', secs: Math.round(a.secs || 0),
                total: rows.length, answered: answered, correct: correct, rows: rows };
    var d = read();
    d.attempts.push(att);
    if (d.attempts.length > MAX_ATTEMPTS) d.attempts = d.attempts.slice(-MAX_ATTEMPTS);
    return write(d) ? att : null;
  }

  function dayKey(ts) {
    var d = new Date(ts), m = d.getMonth() + 1, day = d.getDate();
    return d.getFullYear() + '-' + (m < 10 ? '0' : '') + m + '-' + (day < 10 ? '0' : '') + day;
  }

  function summarize(attempts) {
    attempts = attempts || read().attempts;
    var S = { attempts: attempts.length, answered: 0, correct: 0, perSubject: {}, perLevel: {}, perSection: {}, byDay: {}, streak: 0, last: null };
    attempts.forEach(function (a) {
      S.last = (!S.last || a.ts > S.last.ts) ? a : S.last;
      var dk = dayKey(a.ts), day = S.byDay[dk] || (S.byDay[dk] = { attempts: 0, answered: 0 });
      day.attempts++; day.answered += a.answered;
      a.rows.forEach(function (r) {
        if (r[3] === -1) return;
        var ok = r[3] === 1 ? 1 : 0;
        S.answered++; S.correct += ok;
        var ps = S.perSubject[r[0]] || (S.perSubject[r[0]] = { answered: 0, correct: 0, last: 0 });
        ps.answered++; ps.correct += ok; ps.last = Math.max(ps.last, a.ts);
        var pl = S.perLevel[r[2]] || (S.perLevel[r[2]] = { answered: 0, correct: 0 });
        pl.answered++; pl.correct += ok;
        var sk = r[0] + '::' + r[1], sec = S.perSection[sk] || (S.perSection[sk] = { subject: r[0], section: r[1], answered: 0, correct: 0 });
        sec.answered++; sec.correct += ok;
      });
    });
    var d = new Date(); d.setHours(12, 0, 0, 0);
    if (!S.byDay[dayKey(d)]) d.setDate(d.getDate() - 1);   // a streak survives until the end of tomorrow
    while (S.byDay[dayKey(d)]) { S.streak++; d.setDate(d.getDate() - 1); }
    return S;
  }

  function weakSections(S, minAnswered, below) {
    return Object.keys(S.perSection).map(function (k) { return S.perSection[k]; })
      .filter(function (s) { return s.answered >= (minAnswered || 3) && s.correct / s.answered < (below || 0.7); })
      .sort(function (a, b) { return a.correct / a.answered - b.correct / b.answered || b.answered - a.answered; });
  }

  function exportJSON() { return JSON.stringify({ app: 'study-dashboards', exported: new Date().toISOString(), data: read() }); }

  function importJSON(text) {
    var p = JSON.parse(text), inc = p && (p.data || p);
    if (!inc || !Array.isArray(inc.attempts)) throw new Error('This file does not look like a Study Dashboards backup.');
    var d = read(), have = {};
    d.attempts.forEach(function (a) { have[a.id] = 1; });
    var added = 0;
    inc.attempts.forEach(function (a) {
      if (a && a.id && Array.isArray(a.rows) && !have[a.id]) { d.attempts.push(a); have[a.id] = 1; added++; }
    });
    d.attempts.sort(function (a, b) { return a.ts - b.ts; });
    d.attempts = d.attempts.slice(-MAX_ATTEMPTS);
    write(d);
    return added;
  }

  function clear() { return write({ v: 1, attempts: [] }); }

  w.HubStore = { read: read, record: record, summarize: summarize, weakSections: weakSections, dayKey: dayKey,
                 exportJSON: exportJSON, importJSON: importJSON, clear: clear };
})(window);
