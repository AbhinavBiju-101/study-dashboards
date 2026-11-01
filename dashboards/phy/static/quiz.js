(function(){
  var ans = Q.map(function(){return null;}), flags = Q.map(function(){return false;});
  var cur = 0, maxSeen = 0, t0 = Date.now(), done = false;
  var label = {}; MODS.forEach(function(m){ label[m.n]='Module '+m.n; m.topics.forEach(function(t){ label[t.id]=t.title; t.subtopics.forEach(function(s){ label[s.id]=s.title; }); }); });
  var $ = function(id){return document.getElementById(id);};
  function fmt(s){ var m=Math.floor(s/60), r=s%60; return (m<10?'0':'')+m+':'+(r<10?'0':'')+r; }
  var tick = setInterval(function(){ if(!done) $('timer').textContent = fmt(Math.floor((Date.now()-t0)/1000)); }, 500);
  function canGo(i){ return ALLOW_BACK || i >= cur; }
  function drawPalette(){
    var p=$('palette'); p.innerHTML='';
    Q.forEach(function(q,i){ var b=document.createElement('button'); b.textContent=i+1;
      b.className=(i===cur?'cur ':'')+(ans[i]!==null?'ans ':'')+(flags[i]?'flag ':'')+(!canGo(i)?'lock':'');
      b.disabled=!canGo(i); b.onclick=function(){ go(i); }; p.appendChild(b); });
    $('prog').style.width=(100*ans.filter(function(a){return a!==null;}).length/Q.length)+'%';
  }
  function draw(){
    var q=Q[cur];
    $('qmeta').textContent='Question '+(cur+1)+' of '+Q.length+' · '+label[q.module]+' · '+label[q.topic]+' · Bloom: '+q.bloom;
    $('qtext').textContent=q.question;
    var o=$('opts'); o.innerHTML='';
    q.options.forEach(function(t,i){ var l=document.createElement('label'); l.className='opt'+(ans[cur]===i?' sel':'');
      var r=document.createElement('input'); r.type='radio'; r.name='opt'; r.checked=ans[cur]===i; r.onchange=function(){ ans[cur]=i; draw(); };
      l.appendChild(r); l.appendChild(document.createTextNode(' '+t)); o.appendChild(l); });
    $('prev').disabled = !ALLOW_BACK || cur===0; $('next').disabled = cur===Q.length-1;
    $('flag').textContent = flags[cur] ? '⚑ Unflag' : '⚑ Flag for review';
    drawPalette();
  }
  function go(i){ if(i<0||i>=Q.length||!canGo(i)) return; cur=i; maxSeen=Math.max(maxSeen,i); draw(); }
  $('prev').onclick=function(){ go(cur-1); }; $('next').onclick=function(){ go(cur+1); };
  $('flag').onclick=function(){ flags[cur]=!flags[cur]; draw(); };
  $('submit').onclick=function(){
    var un=ans.filter(function(a){return a===null;}).length;
    if(un && !confirm(un+' question(s) unanswered. Submit anyway?')) return;
    finish();
  };
  function bump(map,key,ok){ var s=map[key]||(map[key]={r:0,t:0}); s.t++; if(ok) s.r++; }
  function finish(){
    done=true; clearInterval(tick); var secs=Math.floor((Date.now()-t0)/1000);
    var right=0, byMod={}, byTop={}, byBloom={}, rows=[];
    Q.forEach(function(q,i){ var ok = ans[i]===q.answer, sk = ans[i]===null; if(ok) right++;
      if(!sk){ bump(byMod,q.module,ok); bump(byTop,q.topic,ok); bump(byBloom,q.bloom,ok); }
      rows.push({i:i,q:q,ok:ok,skipped:sk,flag:flags[i]}); });
    var saved = QMProgress.record(rows.filter(function(r){return !r.skipped;}).map(function(r){return {subtopic:r.q.subtopic, correct:r.ok};}));
    $('runner').style.display='none'; var R=$('results'); R.style.display='block';
    function table(map){ return '<table class="t"><tr><th></th><th>Correct</th><th>Accuracy</th></tr>'+Object.keys(map).map(function(k){var s=map[k];
      return '<tr><td>'+(label[k]||k)+'</td><td>'+s.r+' / '+s.t+'</td><td>'+Math.round(100*s.r/s.t)+'%</td></tr>';}).join('')+'</table>'; }
    R.innerHTML='<div class="card quiz"><h2>Score: '+right+' / '+Q.length+' ('+Math.round(100*right/Q.length)+'%)</h2><p>Time: '+fmt(secs)+' · skipped: '+rows.filter(function(r){return r.skipped;}).length+
      (saved?'':' · <b>progress could not be saved (browser storage blocked)</b>')+'</p></div>'+
      '<div class="grid"><div class="card quiz"><h3>By module</h3>'+table(byMod)+'</div><div class="card quiz"><h3>By topic</h3>'+table(byTop)+'</div><div class="card quiz"><h3>By Bloom\'s level</h3>'+table(byBloom)+'</div></div>'+
      '<div class="card quiz"><h3>Review</h3><p>Show: '+['all','correct','wrong','skipped','flagged'].map(function(f){return '<button class="btn alt" data-f="'+f+'">'+f+'</button>';}).join(' ')+
      ' <a class="btn" href="'+location.pathname.replace('/start','')+'">New quiz</a></p><div id="rev"></div></div>';
    function review(f){ var h=''; rows.forEach(function(r){
        var show = f==='all'||(f==='correct'&&r.ok)||(f==='wrong'&&!r.ok&&!r.skipped)||(f==='skipped'&&r.skipped)||(f==='flagged'&&r.flag); if(!show) return;
        h+='<div class="card quiz" style="margin:10px 0"><b>Q'+(r.i+1)+'.</b> '+esc(r.q.question)+(r.flag?' ⚑':'')+r.q.options.map(function(o,k){
          var c=k===r.q.answer?'right':(k===ans[r.i]?'wrong':''); return '<div class="opt '+c+'">'+esc(o)+(k===ans[r.i]?' ← your answer':'')+(k===r.q.answer?' ✓':'')+'</div>'; }).join('')+
          (r.q.explanation?'<p class="small">'+esc(r.q.explanation)+'</p>':'')+'</div>'; });
      $('rev').innerHTML=h||'<p class="muted">Nothing in this filter.</p>'; }
    function esc(s){ return String(s).replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];}); }
    R.querySelectorAll('[data-f]').forEach(function(b){ b.onclick=function(){ review(b.dataset.f); }; }); review('all');
  }
  draw();
})();
