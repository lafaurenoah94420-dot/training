const EMOJI = {
  rock: "✊",
  paper: "✋",
  scissors: "✌️",
};

const LABELS = {
  rock: "Pierre",
  paper: "Feuille",
  scissors: "Ciseaux",
};

const CHOICES = ["rock", "paper", "scissors"];

const BEATS = {
  rock: "scissors",
  paper: "rock",
  scissors: "paper",
};

const QUOTES = {
  // Le joueur gagne — Nahla refuse d'admettre sa défaite
  playerWins: [
    "« Tu as gagné ? Non. J'ai choisi de t'humilier en te laissant croire. »",
    "« Une manche. Une seule. Le canapé reste à moi pour l'éternité. »",
    "« Profite. C'est la dernière fois qu'un humain me bat avant la sieste. »",
    "« Le hasard est un concept inventé par les perdants. Toi inclus… sauf cette fois. »",
  ],
  // Nahla gagne — elle règne
  nahlaWins: [
    "« Évidemment. Tu jouais contre une déesse du salon. »",
    "« Pathétique. Même Malik ferait moins n'importe quoi — et c'est dire. »",
    "« J'ai même pas levé la patte. T'as perdu tout seul. »",
    "« Reviens quand t'auras un cerveau, des griffes, et mon autorisation. »",
    "« Une victoire de plus pour moi. Une humiliation de plus pour toi. »",
  ],
  tie: [
    "« Égalité ? Non. J'ai imposé le rythme, tu as copié. »",
    "« Même main. Moi c'était de l'art. Toi c'était du plagiat. »",
    "« Match nul officiel. Dans ma tête, j'ai gagné. »",
    "« On s'ennuie. Va me remplir la gamelle pendant qu'on y est. »",
  ],
};

// Répliques liées à la main jouée (plus de sens)
const CONTEXT = {
  playerWins: {
    rock: "« Tu m'as écrasée ? …La pierre, c'est mon trône. Tu l'as volé. Je porterai plainte. »",
    paper: "« Ta feuille m'a enveloppée ? Dégoûtant. Lave tes mains avant de me toucher. »",
    scissors: "« Tes ciseaux m'ont coupé ? J'ai des griffes, pas besoin de ton jouet en plastique. »",
  },
  nahlaWins: {
    rock: "« Pierre. Comme mon poids quand je m'assois sur tes genoux. Écrasant. »",
    paper: "« Feuille. Je t'ai recouvert de honte. Facile. »",
    scissors: "« Ciseaux. J'aurais pu te couper les câbles internet. J'ai été clémente. »",
  },
  tie: {
    rock: "« Deux pierres. Deux masses. Une seule intelligence — la mienne. »",
    paper: "« Deux feuilles. La mienne valait un trône. La tienne, un ticket de caisse. »",
    scissors: "« Deux ciseaux. Je coupe les liens humains depuis 2022. »",
  },
};

const SCORE_KEY = "nahla_rps_score";

const playerEl = document.getElementById("player-choice");
const nahlaEl = document.getElementById("nahla-choice");
const resultEl = document.getElementById("result");
const quoteEl = document.getElementById("nahla-quote");
const winsEl = document.getElementById("wins");
const tiesEl = document.getElementById("ties");
const lossesEl = document.getElementById("losses");
const resetBtn = document.getElementById("reset-btn");

let score = loadScore();

function loadScore() {
  try {
    const saved = JSON.parse(localStorage.getItem(SCORE_KEY));
    if (saved && typeof saved.wins === "number") return saved;
  } catch (_) {}
  return { wins: 0, ties: 0, losses: 0 };
}

function saveScore() {
  localStorage.setItem(SCORE_KEY, JSON.stringify(score));
}

function updateHud() {
  winsEl.textContent = score.wins;
  tiesEl.textContent = score.ties;
  lossesEl.textContent = score.losses;
}

function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function getQuote(outcome, playerChoice, nahlaChoice) {
  const poolKey =
    outcome === "win" ? "playerWins" : outcome === "lose" ? "nahlaWins" : "tie";
  const choiceKey = outcome === "lose" ? nahlaChoice : playerChoice;

  if (Math.random() < 0.45 && CONTEXT[poolKey][choiceKey]) {
    return CONTEXT[poolKey][choiceKey];
  }
  return pickRandom(QUOTES[poolKey]);
}

function getOutcome(player, nahla) {
  if (player === nahla) return "tie";
  if (BEATS[player] === nahla) return "win";
  return "lose";
}

function flashChoice(el, emoji) {
  el.textContent = emoji;
  el.classList.remove("reveal");
  void el.offsetWidth;
  el.classList.add("reveal");
}

function play(playerChoice) {
  const nahlaChoice = pickRandom(CHOICES);
  const outcome = getOutcome(playerChoice, nahlaChoice);

  flashChoice(playerEl, EMOJI[playerChoice]);
  flashChoice(nahlaEl, EMOJI[nahlaChoice]);

  resultEl.className = "result-msg " + outcome;

  if (outcome === "win") {
    score.wins += 1;
    resultEl.textContent = `Tu gagnes ! (${LABELS[playerChoice]} bat ${LABELS[nahlaChoice]})`;
  } else if (outcome === "lose") {
    score.losses += 1;
    resultEl.textContent = `Nahla gagne. (${LABELS[nahlaChoice]} bat ${LABELS[playerChoice]})`;
  } else {
    score.ties += 1;
    resultEl.textContent = `Égalité — ${LABELS[playerChoice]} vs ${LABELS[nahlaChoice]}`;
  }

  quoteEl.textContent = getQuote(outcome, playerChoice, nahlaChoice);
  saveScore();
  updateHud();
}

document.querySelectorAll(".rps-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    play(btn.dataset.choice);
  });
});

resetBtn.addEventListener("click", () => {
  score = { wins: 0, ties: 0, losses: 0 };
  saveScore();
  updateHud();
  playerEl.textContent = "❔";
  nahlaEl.textContent = "❔";
  resultEl.className = "result-msg";
  resultEl.textContent = "Score réinitialisé. Choisis ta main.";
  quoteEl.textContent = "";
});

updateHud();
