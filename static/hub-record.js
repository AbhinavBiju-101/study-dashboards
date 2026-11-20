/* Loaded only on a dashboard's quiz-result page (injected by the hub).
 * The dashboard's own quiz code calls window.hubRecord({secs, rows:[[section, level, ok], ...]}).
 * Pass noMarks:true for self-graded sets where the marking scheme does not apply. */
(function (w) {
  'use strict';
  var slug = (document.currentScript && document.currentScript.dataset.slug) || location.pathname.split('/')[1];
  var saved = false;
  w.hubRecord = function (a) {
    if (saved || !w.HubStore) return;   // one quiz = one saved attempt
    saved = true;
    var rows = (a.rows || []).map(function (r) { return [slug, String(r[0]), String(r[1]), r[2]]; }), extra = {};
    if (!a.noMarks && w.HubMarking) {
      var sc = w.HubMarking.score(rows.map(function (r) { return r[3]; }));
      extra = { marks: sc.marks, max: sc.max, scheme: [sc.scheme.c, sc.scheme.w, sc.scheme.u] };
      setTimeout(function () { try { w.HubMarking.banner(rows.map(function (r) { return r[3]; })); } catch (e) {} }, 80);
    }
    w.HubStore.record({ subject: slug, mode: 'subject', secs: a.secs, rows: rows, marks: extra.marks, max: extra.max, scheme: extra.scheme });
  };
})(window);
