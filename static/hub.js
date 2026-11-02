/* Shared helpers for hub pages. */
(function (w) {
  'use strict';
  var H = w.Hub = {};
  var S = (w.HUB && w.HUB.subjects) || {};

  H.subjects = S;
  H.esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  H.pct = function (c, n) { return n ? Math.round(100 * c / n) : 0; };
  H.cls = function (p) { return p >= 75 ? '' : p >= 50 ? 'warn' : 'bad'; };
  H.name = function (slug) { return slug === 'mixed' ? 'Mixed quiz' : (S[slug] ? S[slug].title : slug); };
  H.accent = function (slug) { return S[slug] ? S[slug].accent : '#5f6b63'; };
  H.fmtTime = function (s) {
    s = Math.round(s || 0);
    if (s < 60) return s + 's';
    var m = Math.floor(s / 60), r = s % 60;
    return m < 60 ? m + 'm ' + (r < 10 ? '0' : '') + r + 's' : Math.floor(m / 60) + 'h ' + (m % 60) + 'm';
  };
  H.ago = function (ts) {
    var s = (Date.now() - ts) / 1000;
    if (s < 60) return 'just now';
    if (s < 3600) return Math.floor(s / 60) + ' min ago';
    if (s < 86400) return Math.floor(s / 3600) + ' h ago';
    var d = Math.floor(s / 86400);
    return d === 1 ? 'yesterday' : d < 30 ? d + ' days ago' : new Date(ts).toLocaleDateString();
  };
  H.bar = function (label, right, p, extra) {
    return '<div class="bar-row"><div class="bar-label"><span>' + label + '</span><span>' + right + '</span></div>' +
      '<div class="bar-track"><div class="bar-fill ' + H.cls(p) + '" style="width:' + p + '%"></div></div>' + (extra || '') + '</div>';
  };

  // "/" focuses the search box (unless you're typing somewhere)
  document.addEventListener('keydown', function (e) {
    var t = e.target, typing = t && (/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName) || t.isContentEditable);
    if (e.key === '/' && !typing && !e.ctrlKey && !e.metaKey && !e.altKey) {
      var q = document.getElementById('page-q') || document.getElementById('nav-q');
      if (q) { e.preventDefault(); q.focus(); q.select(); }
    }
  });
})(window);
