/* Loaded only on a dashboard's quiz-result page (injected by the hub).
 * The dashboard's own quiz code calls window.hubRecord({secs, rows:[[section, level, ok], ...]}). */
(function (w) {
  'use strict';
  var slug = (document.currentScript && document.currentScript.dataset.slug) || location.pathname.split('/')[1];
  var saved = false;
  w.hubRecord = function (a) {
    if (saved || !w.HubStore) return;   // one quiz = one saved attempt
    saved = true;
    w.HubStore.record({
      subject: slug, mode: 'subject', secs: a.secs,
      rows: (a.rows || []).map(function (r) { return [slug, String(r[0]), String(r[1]), r[2]]; })
    });
  };
})(window);
