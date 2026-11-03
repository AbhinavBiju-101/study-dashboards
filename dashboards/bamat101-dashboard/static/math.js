/* Render \( \) and \[ \] maths inside an element with KaTeX. */
window.renderMath = function (el) {
  if (!window.renderMathInElement) return;
  window.renderMathInElement(el || document.body, {
    delimiters: [{ left: '\\[', right: '\\]', display: true }, { left: '\\(', right: '\\)', display: false }],
    throwOnError: false, strict: 'ignore'
  });
};
document.addEventListener('DOMContentLoaded', function () { window.renderMath(document.querySelector('.notes') || undefined); });
