/* Mixed cross-subject quiz: setup -> run -> results, all in the page.  Results go to HubStore. */
(function () {
  'use strict';
  var H = Hub, esc = H.esc, app = document.getElementById('app');
  var LV = ['Remember', 'Understand', 'Apply', 'Analyze', 'Evaluate', 'Create'], LETTERS = 'ABCDEFGH';

  var BANK, SECS = {}, CELL = {}, SUBJ_TOTAL = {}, LEVELS = [];
  var sel = {}, lvlOn = {}, opts = { count: 10, balance: true, back: true }, notice = '';
  var run = null, tick = null, keyHandler = null;

  /* ---------- helpers ---------- */
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function fmt(s) { s = Math.floor(s); var m = Math.floor(s / 60), r = s % 60; return m + ':' + (r < 10 ? '0' : '') + r; }

  function load() {
    fetch('/api/bank').then(function (r) { return r.json(); }).then(function (b) {
      BANK = b;
      b.subjects.forEach(function (s) {
        SUBJ_TOTAL[s.slug] = 0;
        s.sections.forEach(function (sec) { sec.slug = s.slug; SECS[sec.id] = sec; CELL[sec.id] = {}; SUBJ_TOTAL[s.slug] += sec.n; });
      });
      var seen = {};
      b.questions.forEach(function (q) { CELL[q.c][q.l] = (CELL[q.c][q.l] || 0) + 1; seen[q.l] = 1; });
      LEVELS = Object.keys(seen).sort(function (a, c) { return (LV.indexOf(a) + 99) % 99 - (LV.indexOf(c) + 99) % 99 || (a < c ? -1 : 1); });
      LEVELS.forEach(function (l) { lvlOn[l] = true; });
      applyUrl();
    }).catch(function () {
      app.innerHTML = '<div class="page-head"><h1>Couldn\'t load the questions.</h1><p class="lede">Check your connection and <a href="/quiz">try again</a>.</p></div>';
    });
  }

  function applyUrl() {
    var p = new URLSearchParams(location.search), preset = p.get('preset');
    if (p.get('subjects')) p.get('subjects').split(',').forEach(function (k) { (BANK.subjects.filter(function (s) { return s.slug === k; })[0] || { sections: [] }).sections.forEach(function (x) { sel[x.id] = 1; }); });
    p.getAll('sec').forEach(function (key) {
      var i = key.indexOf('::'), slug = key.slice(0, i), label = key.slice(i + 2);
      Object.keys(SECS).forEach(function (id) { if (SECS[id].slug === slug && SECS[id].label === label) sel[id] = 1; });
    });
    if (preset === 'quick') { selectAll(true); opts.count = 10; return start(); }
    if (preset === 'weak') {
      var weak = HubStore.weakSections(HubStore.summarize()).slice(0, 6);
      weak.forEach(function (w) { Object.keys(SECS).forEach(function (id) { if (SECS[id].slug === w.subject && SECS[id].label === w.section) sel[id] = 1; }); });
      if (Object.keys(sel).length) { opts.count = 15; return start(); }
      notice = 'No weak areas yet. Weak spots appear after you answer at least 3 questions in a topic and score under 70%.';
    }
    setup();
  }

  function selectAll(on) { sel = {}; if (on) Object.keys(SECS).forEach(function (id) { sel[id] = 1; }); }
  function avail(id) { var c = CELL[id], n = 0; LEVELS.forEach(function (l) { if (lvlOn[l]) n += c[l] || 0; }); return n; }
  function totalAvail() { var n = 0; Object.keys(sel).forEach(function (id) { n += avail(id); }); return n; }

  /* ---------- setup ---------- */
  function setup() {
    stopRun();
    var weakN = HubStore.weakSections(HubStore.summarize()).length;
    app.innerHTML =
      '<div class="page-head"><p class="eyebrow">Mixed quiz</p><h1>Build your quiz.</h1><p class="lede">Tick any mix of subjects and topics. Options are reshuffled every attempt, and results land on your Progress page.</p></div>' +
      (notice ? '<div class="card" style="border-color:#e9d7a6;background:#fffaeb;margin-bottom:16px">' + esc(notice) + '</div>' : '') +
      '<div class="quiz-layout"><section class="picker" aria-label="Choose topics">' +
        '<div class="preset-row"><button class="chip" data-act="quick">⚡ Quick 10 from everything</button>' +
        '<button class="chip" data-act="weak"' + (weakN ? '' : ' disabled style="opacity:.5;cursor:not-allowed"') + '>🎯 Weak areas' + (weakN ? ' (' + weakN + ')' : '') + '</button>' +
        '<button class="chip" data-act="all">Select everything</button><button class="chip" data-act="none">Clear</button></div>' +
        BANK.subjects.map(subjectHtml).join('') +
      '</section>' +
      '<aside class="card sticky" aria-label="Quiz options"><div class="muted small" style="font-weight:700;text-transform:uppercase;letter-spacing:.07em">Available</div>' +
        '<div class="avail" id="avail">0</div><div class="muted small" id="avail-s"></div>' +
        '<div class="field"><label for="count">Number of questions</label><input id="count" type="number" min="1" value="' + opts.count + '"> ' +
          '<div class="chips" style="margin-top:8px">' + [10, 20, 30, 50].map(function (n) { return '<button class="chip" data-n="' + n + '">' + n + '</button>'; }).join('') + '<button class="chip" data-n="all">All</button></div></div>' +
        '<div class="field"><span class="lbl">Bloom\'s levels</span><div class="chips" id="lvls">' + LEVELS.map(function (l) { return '<button class="chip" data-l="' + esc(l) + '" aria-pressed="' + !!lvlOn[l] + '">' + esc(l) + '</button>'; }).join('') + '</div></div>' +
        '<label class="toggle"><input type="checkbox" id="bal"' + (opts.balance ? ' checked' : '') + '><span>Balance across subjects<small>Take a similar number from each ticked subject instead of fully random.</small></span></label>' +
        '<label class="toggle"><input type="checkbox" id="back"' + (opts.back ? ' checked' : '') + '><span>Allow going back<small>Turn off to lock questions once you move on.</small></span></label>' +
        '<button class="btn primary" id="go" style="width:100%;justify-content:center;margin-top:6px">Start quiz →</button>' +
      '</aside></div>';
    notice = '';
    sync();
  }

  function subjectHtml(s) {
    var groups = [], map = {};
    s.sections.forEach(function (sec) { if (!map[sec.group]) { map[sec.group] = []; groups.push(sec.group); } map[sec.group].push(sec); });
    return '<div class="subj" data-subj="' + s.slug + '" style="--accent:' + s.accent + ';border:1px solid var(--line);border-left:5px solid ' + s.accent + ';border-radius:10px;margin-top:10px;background:#fff">' +
      '<div style="display:flex;align-items:center;gap:10px;padding:12px 14px">' +
        '<label style="display:flex;align-items:center;gap:10px;flex:1;cursor:pointer"><input type="checkbox" data-all="' + s.slug + '"><span class="name" style="font:700 1.02rem var(--serif)">' + esc(s.title) + '</span></label>' +
        '<span class="small muted" data-count></span><button class="btn sm" data-toggle="' + s.slug + '" aria-expanded="false">Topics ▾</button></div>' +
      '<div class="body" hidden style="padding:0 14px 12px;border-top:1px solid var(--line)">' +
        groups.map(function (g) {
          return '<div class="grp"><span style="flex:1">' + esc(g) + '</span><button class="btn sm" data-grp="' + esc(g) + '" data-s="' + s.slug + '">toggle</button></div>' +
            map[g].map(function (sec) {
              return '<label class="row"><input type="checkbox" data-sec="' + esc(sec.id) + '"><span>' + esc(sec.label) + '</span><span class="n">' + sec.n + '</span></label>';
            }).join('');
        }).join('') + '</div></div>';
  }

  function sync() {
    document.querySelectorAll('[data-sec]').forEach(function (cb) { cb.checked = !!sel[cb.dataset.sec]; });
    BANK.subjects.forEach(function (s) {
      var on = s.sections.filter(function (x) { return sel[x.id]; }).length, box = app.querySelector('[data-all="' + s.slug + '"]');
      box.checked = on === s.sections.length; box.indeterminate = on > 0 && on < s.sections.length;
      var n = 0; s.sections.forEach(function (x) { if (sel[x.id]) n += avail(x.id); });
      app.querySelector('[data-subj="' + s.slug + '"] [data-count]').textContent = on ? n + ' questions' : SUBJ_TOTAL[s.slug] + ' total';
    });
    var n = totalAvail(), c = document.getElementById('count');
    document.getElementById('avail').textContent = n;
    document.getElementById('avail-s').textContent = n ? 'questions from ' + Object.keys(sel).length + ' topic' + (Object.keys(sel).length > 1 ? 's' : '') : 'Tick something on the left';
    c.max = n || 1;
    if (n && opts.count > n) { opts.count = n; c.value = n; }
    document.getElementById('go').disabled = !n;
  }

  function onSetupClick(e) {
    var t = e.target.closest('button,input'); if (!t) return;
    var d = t.dataset;
    if (d.act) {
      if (d.act === 'quick') { selectAll(true); opts.count = 10; return start(); }
      if (d.act === 'weak') { sel = {}; HubStore.weakSections(HubStore.summarize()).slice(0, 6).forEach(function (w) { Object.keys(SECS).forEach(function (id) { if (SECS[id].slug === w.subject && SECS[id].label === w.section) sel[id] = 1; }); }); opts.count = 15; return start(); }
      selectAll(d.act === 'all'); return sync();
    }
    if (d.toggle) { var sub = app.querySelector('[data-subj="' + d.toggle + '"] .body'); sub.hidden = !sub.hidden; t.setAttribute('aria-expanded', !sub.hidden); t.textContent = sub.hidden ? 'Topics ▾' : 'Topics ▴'; return; }
    if (d.all !== undefined) { BANK.subjects.filter(function (s) { return s.slug === d.all; })[0].sections.forEach(function (x) { if (t.checked) sel[x.id] = 1; else delete sel[x.id]; }); return sync(); }
    if (d.sec) { if (t.checked) sel[d.sec] = 1; else delete sel[d.sec]; return sync(); }
    if (d.grp !== undefined) {
      var ids = BANK.subjects.filter(function (s) { return s.slug === d.s; })[0].sections.filter(function (x) { return x.group === d.grp; }).map(function (x) { return x.id; });
      var all = ids.every(function (i) { return sel[i]; });
      ids.forEach(function (i) { if (all) delete sel[i]; else sel[i] = 1; }); return sync();
    }
    if (d.n) { opts.count = d.n === 'all' ? Math.max(1, totalAvail()) : +d.n; document.getElementById('count').value = opts.count; return sync(); }
    if (d.l) { lvlOn[d.l] = !lvlOn[d.l]; if (!LEVELS.some(function (l) { return lvlOn[l]; })) lvlOn[d.l] = true; t.setAttribute('aria-pressed', !!lvlOn[d.l]); return sync(); }
    if (t.id === 'go') return start();
  }

  /* ---------- building and running ---------- */
  function start(retry) {
    var pool;
    if (retry) pool = retry;
    else {
      pool = BANK.questions.filter(function (q) { return sel[q.c] && lvlOn[q.l]; });
      if (!pool.length) { notice = 'Nothing matched that selection.'; return setup(); }
    }
    var count = Math.max(1, Math.min(retry ? retry.length : (opts.count || 10), pool.length));
    var chosen;
    var bal = document.getElementById('bal'); if (bal) opts.balance = bal.checked;
    var back = document.getElementById('back'); if (back) opts.back = back.checked;
    if (retry) chosen = shuffle(pool.slice());
    else if (opts.balance) {
      var by = {}; shuffle(pool.slice()).forEach(function (q) { (by[q.s] = by[q.s] || []).push(q); });
      var keys = shuffle(Object.keys(by)); chosen = [];
      while (chosen.length < count) { var took = false; keys.forEach(function (k) { if (chosen.length < count && by[k].length) { chosen.push(by[k].pop()); took = true; } }); if (!took) break; }
      shuffle(chosen);
    } else chosen = shuffle(pool.slice()).slice(0, count);
    var Q = chosen.map(function (src) {
      var order = shuffle(src.o.map(function (_, i) { return i; }));
      return { src: src, s: src.s, c: src.c, l: src.l, q: src.q, o: order.map(function (i) { return src.o[i]; }), a: order.indexOf(src.a), ans: null, flag: false, t: 0 };
    });
    run = { Q: Q, i: 0, t0: Date.now(), ts: Date.now(), done: false, back: retry ? opts.back : opts.back };
    history.replaceState(null, '', '/quiz');
    drawRun();
    tick = setInterval(function () { var el = document.getElementById('tm'); if (el && !run.done) el.textContent = fmt((Date.now() - run.t0) / 1000); }, 500);
    keyHandler = function (e) {
      if (!run || run.done || /^(INPUT|TEXTAREA)$/.test(e.target.tagName)) return;
      if (e.key >= '1' && e.key <= '9' && +e.key <= run.Q[run.i].o.length) { run.Q[run.i].ans = +e.key - 1; drawRun(); }
      else if (e.key === 'ArrowRight') go(run.i + 1); else if (e.key === 'ArrowLeft') go(run.i - 1);
      else if (e.key === 'f' || e.key === 'F') { run.Q[run.i].flag = !run.Q[run.i].flag; drawRun(); }
    };
    document.addEventListener('keydown', keyHandler);
    window.onbeforeunload = function () { return run && !run.done && run.Q.some(function (q) { return q.ans !== null; }) ? 'Quiz in progress' : undefined; };
    window.scrollTo(0, 0);
  }

  function stopRun() { clearInterval(tick); if (keyHandler) document.removeEventListener('keydown', keyHandler); keyHandler = null; window.onbeforeunload = null; run = null; }

  function go(n) {
    if (n < 0 || n >= run.Q.length || (!run.back && n < run.i)) return;
    var now = Date.now(); run.Q[run.i].t += (now - run.ts) / 1000; run.ts = now; run.i = n; drawRun();
  }

  function drawRun() {
    var R = run, q = R.Q[R.i], sec = SECS[q.c], subj = H.subjects[q.s] || {};
    var answered = R.Q.filter(function (x) { return x.ans !== null; }).length;
    app.innerHTML =
      '<div class="wrap" style="padding:0"><div class="page-head" style="padding:28px 0 14px"><div class="run-top"><a class="btn sm" href="/quiz" id="quit">← Quit</a><span class="grow"></span>' +
        '<span class="muted small">' + answered + ' / ' + R.Q.length + ' answered</span>' + (R.back ? '' : '<span class="tag" style="--accent:#b7791f">🔒 No backtracking</span>') + '<span class="timer" id="tm">' + fmt((Date.now() - R.t0) / 1000) + '</span></div></div>' +
      '<div class="run-layout"><div class="card qcard"><div class="meta"><span class="tag" style="--accent:' + (subj.accent || '#555') + '">' + esc(subj.code || q.s) + '</span><span>' + esc(sec ? sec.label : '') + '</span><span class="tag" style="--accent:#5f6b63">' + esc(q.l) + '</span><span style="margin-left:auto">Question ' + (R.i + 1) + ' of ' + R.Q.length + '</span></div>' +
        '<p class="stem">' + esc(q.q) + '</p><div role="radiogroup" aria-label="Answers">' +
        q.o.map(function (o, k) { return '<button class="opt ' + (q.ans === k ? 'sel' : '') + '" role="radio" aria-checked="' + (q.ans === k) + '" data-pick="' + k + '"><span class="letter">' + LETTERS[k] + '</span><span>' + esc(o) + '</span></button>'; }).join('') + '</div>' +
        '<div class="nav-row"><button class="btn" data-go="-1"' + (!R.back || !R.i ? ' disabled' : '') + '>← Previous</button><button class="btn" data-flag>' + (q.flag ? '🚩 Flagged' : '⚑ Flag for review') + '</button>' +
        '<span class="grow"></span><button class="btn" data-go="1"' + (R.i === R.Q.length - 1 ? ' disabled' : '') + '>Next →</button><button class="btn primary" data-submit>Submit</button></div>' +
        '<p class="muted small" style="margin-top:12px">Shortcuts: 1–' + q.o.length + ' answer · ← → move · F flag</p></div>' +
      '<aside class="card"><div class="muted small" style="font-weight:700;margin-bottom:10px;text-transform:uppercase;letter-spacing:.07em">Questions</div><div class="palette">' +
        R.Q.map(function (x, k) { return '<button class="' + (x.ans !== null ? 'ans ' : '') + (k === R.i ? 'cur ' : '') + (x.flag ? 'flag' : '') + '" data-jump="' + k + '"' + (!R.back && k < R.i ? ' disabled' : '') + ' aria-label="Question ' + (k + 1) + '">' + (k + 1) + '</button>'; }).join('') +
        '</div></aside></div></div>';
  }

  function onRunClick(e) {
    var t = e.target.closest('button,a'); if (!t || !run || run.done) return;
    var d = t.dataset;
    if (t.id === 'quit') { if (run.Q.some(function (q) { return q.ans !== null; }) && !confirm('Quit this quiz? Your answers so far will not be saved.')) e.preventDefault(); else { stopRun(); e.preventDefault(); setup(); } return; }
    if (d.pick !== undefined) { run.Q[run.i].ans = +d.pick; return drawRun(); }
    if (d.go) return go(run.i + +d.go);
    if (d.jump !== undefined) return go(+d.jump);
    if (d.flag !== undefined) { run.Q[run.i].flag = !run.Q[run.i].flag; return drawRun(); }
    if (d.submit !== undefined) {
      var un = run.Q.filter(function (q) { return q.ans === null; }).length;
      if (un && !confirm(un + ' question' + (un > 1 ? 's are' : ' is') + ' unanswered. Submit anyway?')) return;
      finish();
    }
  }

  /* ---------- results ---------- */
  function status(q) { return q.ans === null ? 'skipped' : q.ans === q.a ? 'correct' : 'wrong'; }

  function finish() {
    var R = run; R.Q[R.i].t += (Date.now() - R.ts) / 1000; R.done = true; clearInterval(tick); window.onbeforeunload = null;
    var secs = R.Q.reduce(function (a, q) { return a + q.t; }, 0);
    var saved = HubStore.record({ subject: 'mixed', mode: 'mixed', secs: secs, rows: R.Q.map(function (q) { return [q.s, SECS[q.c].label, q.l, q.ans === null ? -1 : (q.ans === q.a ? 1 : 0)]; }) });
    R.saved = !!saved; R.secs = secs; R.filter = 'all';
    drawResults();
    window.scrollTo(0, 0);
  }

  function agg(Q, keyFn) {
    var m = {}, order = [];
    Q.forEach(function (q) { var k = keyFn(q); if (!m[k]) { m[k] = { c: 0, n: 0 }; order.push(k); } m[k].n++; if (q.ans === q.a) m[k].c++; });
    return order.map(function (k) { return [k, m[k]]; });
  }

  function drawResults() {
    var R = run, Q = R.Q, n = Q.length, c = Q.filter(function (q) { return status(q) === 'correct'; }).length,
        sk = Q.filter(function (q) { return q.ans === null; }).length, p = H.pct(c, n), missed = Q.filter(function (q) { return status(q) !== 'correct'; });
    var bars = function (rows, label) { return rows.map(function (r) { var pp = H.pct(r[1].c, r[1].n); return H.bar(label(r[0]), pp + '% · ' + r[1].c + '/' + r[1].n, pp); }).join(''); };
    var weakHere = agg(Q, function (q) { return q.s + '::' + q.c; }).filter(function (r) { return r[1].c < r[1].n; }).sort(function (a, b) { return a[1].c / a[1].n - b[1].c / b[1].n || b[1].n - a[1].n; }).slice(0, 5);
    var f = R.filter, list = Q.map(function (q, i) { return [q, i]; }).filter(function (x) { return f === 'all' || (f === 'flagged' ? x[0].flag : status(x[0]) === f); });
    app.innerHTML = '<div class="wrap" style="padding:0"><div class="page-head" style="padding:30px 0 18px"><p class="eyebrow">Results</p></div>' +
      '<div class="score-hero"><div class="big">' + c + ' / ' + n + '</div><div style="opacity:.9">' + p + '% correct' + (p >= 85 ? ' · excellent' : p >= 60 ? ' · solid' : ' · keep at it') + '</div><div class="stats"><div><b>' + c + '</b>Correct</div><div><b>' + (n - c - sk) + '</b>Wrong</div><div><b>' + sk + '</b>Skipped</div><div><b>' + H.fmtTime(R.secs) + '</b>Time</div></div></div>' +
      '<p class="small" style="margin-top:10px;color:' + (R.saved ? 'var(--muted)' : 'var(--bad)') + '">' + (R.saved ? 'Saved to your <a href="/progress">progress</a>.' : 'Could not save progress (browser storage is blocked).') + '</p>' +
      '<div class="grid cols-2 section" style="margin-top:20px"><div class="card"><h2>By subject</h2>' + bars(agg(Q, function (q) { return q.s; }), function (k) { return esc(H.name(k)); }) + '</div>' +
      '<div class="card"><h2>By Bloom\'s level</h2>' + bars(agg(Q, function (q) { return q.l; }).sort(function (a, b) { return (LV.indexOf(a[0]) + 99) % 99 - (LV.indexOf(b[0]) + 99) % 99; }), esc) + '</div></div>' +
      (weakHere.length ? '<div class="card section"><h2>Revisit these topics</h2>' + weakHere.map(function (r) { var k = r[0].split('::'), sec = SECS[k[1]]; return '<div class="weak-row"><span class="tag" style="--accent:' + H.accent(k[0]) + '">' + esc((H.subjects[k[0]] || {}).code || k[0]) + '</span><div class="info"><div>' + esc(sec.label) + '</div></div><span class="small muted">' + r[1].c + '/' + r[1].n + ' right</span><a class="btn sm" href="' + esc(sec.slug ? '/' + sec.slug + '/' : '/') + '">Open notes</a></div>'; }).join('') + '</div>' : '') +
      '<div class="card section"><div class="section-head"><h2>Review</h2><div class="chips">' + ['all', 'correct', 'wrong', 'skipped', 'flagged'].map(function (x) { return '<button class="chip" data-f="' + x + '" aria-pressed="' + (f === x) + '">' + x + '</button>'; }).join('') + '</div></div>' +
        (list.map(function (x) {
          var q = x[0], i = x[1], sec = SECS[q.c];
          return '<div class="review-item"><div class="r-meta">Q' + (i + 1) + ' · ' + esc(H.name(q.s)) + ' · ' + esc(sec.label) + ' · ' + esc(q.l) + ' · ' + fmt(q.t) + (q.flag ? ' · 🚩' : '') + '</div><p class="stem" style="font-size:1.02rem;margin-bottom:8px">' + esc(q.q) + '</p>' +
            q.o.map(function (o, k) { return '<div class="opt static ' + (k === q.a ? 'right' : k === q.ans ? 'wrong' : '') + '"><span class="letter">' + LETTERS[k] + '</span><span>' + esc(o) + (k === q.a ? ' ✔' : k === q.ans ? ' ✘ your answer' : '') + '</span></div>'; }).join('') +
            (q.ans === null ? '<div class="muted small">Skipped</div>' : '') + '</div>';
        }).join('') || '<p class="muted">Nothing matches this filter.</p>') + '</div>' +
      '<div class="nav-row" style="margin:22px 0 0">' + (missed.length ? '<button class="btn primary" data-retry>Retry the ' + missed.length + ' I missed</button>' : '') + '<button class="btn" data-new>New quiz</button><a class="btn" href="/progress">View progress</a></div></div>';
  }

  function onResultClick(e) {
    var t = e.target.closest('button'); if (!t || !run || !run.done) return;
    if (t.dataset.f) { run.filter = t.dataset.f; return drawResults(); }
    if (t.dataset.new !== undefined) { stopRun(); return setup(); }
    if (t.dataset.retry !== undefined) {
      var missed = run.Q.filter(function (q) { return status(q) !== 'correct'; }).map(function (q) { return q.src; });
      var back = run.back; stopRun(); opts.back = back; return start(missed);
    }
  }

  app.addEventListener('click', function (e) { if (run) { if (run.done) onResultClick(e); else onRunClick(e); } else onSetupClick(e); });
  app.addEventListener('input', function (e) { if (e.target.id === 'count') { opts.count = Math.max(1, +e.target.value || 1); } });
  app.addEventListener('change', function (e) { if (e.target.id === 'count') sync(); });
  load();
})();
