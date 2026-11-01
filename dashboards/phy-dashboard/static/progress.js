/* Progress kept in localStorage (always wrapped in try/catch: storage can be blocked). */
var QMProgress = (function(){
  var KEY='qm_notes_progress_v1';
  function load(){ try{ var s=localStorage.getItem(KEY); return s?JSON.parse(s):{sub:{}}; }catch(e){ return {sub:{}}; } }
  function save(p){ try{ localStorage.setItem(KEY, JSON.stringify(p)); return true; }catch(e){ return false; } }
  function record(results){ // results: [{subtopic, correct}]
    var p=load(); p.sub=p.sub||{};
    results.forEach(function(r){ var s=p.sub[r.subtopic]||{right:0,total:0}; s.total++; if(r.correct) s.right++; p.sub[r.subtopic]=s; });
    return save(p);
  }
  return {load:load, save:save, record:record};
})();
