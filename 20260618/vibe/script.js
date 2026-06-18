const quotes = [
  "« Les humains sont lents. »",
  "« Le canapé m'appartient. »",
  "« Miaou = laisse-moi tranquille. »",
  "« Malik qui ? »",
  "« Kays peut attendre. »",
  "« 6h de sieste, c'est le minimum. »",
  "« Vous travaillez, je juge. »",
];

const quoteEl = document.getElementById("quote");
const quoteBtn = document.getElementById("quote-btn");

quoteBtn.addEventListener("click", () => {
  let next = quotes[Math.floor(Math.random() * quotes.length)];
  while (next === quoteEl.textContent && quotes.length > 1) {
    next = quotes[Math.floor(Math.random() * quotes.length)];
  }
  quoteEl.classList.add("fade");
  setTimeout(() => {
    quoteEl.textContent = next;
    quoteEl.classList.remove("fade");
  }, 200);
});

function animateStat(el) {
  const target = parseFloat(el.dataset.target);
  const isFloat = target % 1 !== 0;
  const duration = 1400;
  const start = performance.now();

  function tick(now) {
    const t = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - t, 3);
    const val = target * eased;
    el.textContent = isFloat ? val.toFixed(1) : Math.floor(val).toLocaleString("fr-FR");
    if (t < 1) requestAnimationFrame(tick);
  }

  requestAnimationFrame(tick);
}

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animateStat(entry.target);
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.3 }
);

document.querySelectorAll(".stat-num").forEach((el) => observer.observe(el));

document.querySelectorAll(".btn-copy").forEach((btn) => {
  btn.addEventListener("click", async () => {
    const card = btn.closest(".game-card");
    const cmd = card.querySelector(".launch-cmd").dataset.cmd;
    try {
      await navigator.clipboard.writeText(cmd);
      btn.textContent = "Copié !";
      btn.classList.add("copied");
      setTimeout(() => {
        btn.textContent = "Copier la commande";
        btn.classList.remove("copied");
      }, 2000);
    } catch {
      btn.textContent = "Sélectionne le texte ci-dessus";
    }
  });
});
