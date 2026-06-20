const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const scoreEl = document.getElementById("score");
const recordEl = document.getElementById("record");
const overlay = document.getElementById("overlay");
const overlayTitle = document.getElementById("overlay-title");
const overlayMsg = document.getElementById("overlay-msg");
const startBtn = document.getElementById("start-btn");

const GRID = 20;
const CELL = canvas.width / GRID;
const TICK_MS = 110;

const COLORS = {
  wall: "#585048",
  floor: "#3a322c",
  carpet: "#5c3e34",
  carpetBorder: "#6e4a3e",
  tail: "#c9925a",
  tailDark: "#a67a45",
  croquette: "#b8732a",
  croquetteLight: "#e8b060",
  meuble: "#64403c",
  meubleTop: "#7a5050",
};

const MEUBLES = [
  { x: 2, y: 2, w: 4, h: 2 },
  { x: 14, y: 3, w: 3, h: 3 },
  { x: 4, y: 14, w: 5, h: 2 },
  { x: 13, y: 13, w: 4, h: 3 },
];

const MIAM_LINES = ["Miam.", "Encore.", "Croquette volée.", "Les humains paieront."];

const nahlaImg = new Image();
nahlaImg.src = "nahla_head.png";
let nahlaReady = false;
nahlaImg.onload = () => {
  nahlaReady = true;
  draw();
};

let snake;
let dir;
let nextDir;
let croquette;
let score;
let record = Number(localStorage.getItem("nahlaSnakeRecord") || 0);
let loopId;
let paused;
let state;
let miamText = "";
let miamUntil = 0;

recordEl.textContent = record;

function randCell() {
  return {
    x: Math.floor(Math.random() * GRID),
    y: Math.floor(Math.random() * GRID),
  };
}

function spawnCroquette() {
  let pos;
  do {
    pos = randCell();
  } while (
    snake.some((s) => s.x === pos.x && s.y === pos.y) ||
    MEUBLES.some((m) => pos.x >= m.x && pos.x < m.x + m.w && pos.y >= m.y && pos.y < m.y + m.h)
  );
  croquette = pos;
}

function resetGame() {
  snake = [
    { x: 10, y: 10 },
    { x: 9, y: 10 },
    { x: 8, y: 10 },
  ];
  dir = { x: 1, y: 0 };
  nextDir = { ...dir };
  score = 0;
  scoreEl.textContent = score;
  spawnCroquette();
  paused = false;
  state = "playing";
  miamText = "";
}

function drawSalon() {
  ctx.fillStyle = COLORS.wall;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  const margin = CELL * 0.5;
  ctx.fillStyle = COLORS.floor;
  ctx.fillRect(margin, margin, canvas.width - margin * 2, canvas.height - margin * 2);

  const carpetPad = CELL * 1.2;
  ctx.fillStyle = COLORS.carpet;
  ctx.beginPath();
  ctx.roundRect(
    carpetPad, carpetPad,
    canvas.width - carpetPad * 2, canvas.height - carpetPad * 2,
    10
  );
  ctx.fill();
  ctx.strokeStyle = COLORS.carpetBorder;
  ctx.lineWidth = 2;
  ctx.stroke();

  MEUBLES.forEach((m) => {
    const x = m.x * CELL;
    const y = m.y * CELL;
    const w = m.w * CELL;
    const h = m.h * CELL;
    ctx.fillStyle = COLORS.meuble;
    ctx.beginPath();
    ctx.roundRect(x, y, w, h, 6);
    ctx.fill();
    ctx.fillStyle = COLORS.meubleTop;
    ctx.beginPath();
    ctx.roundRect(x + 4, y - 8, w - 8, 10, 4);
    ctx.fill();
  });
}

function drawCroquette() {
  const cx = croquette.x * CELL + CELL / 2;
  const cy = croquette.y * CELL + CELL / 2;

  ctx.fillStyle = "rgba(255, 200, 80, 0.25)";
  ctx.beginPath();
  ctx.arc(cx, cy, CELL * 0.42, 0, Math.PI * 2);
  ctx.fill();

  const offsets = [
    [0, 0], [-4, 3], [4, 2], [-2, -4], [3, -3], [5, 0], [-5, -1],
  ];
  offsets.forEach(([ox, oy], i) => {
    ctx.fillStyle = i === 0 ? COLORS.croquetteLight : COLORS.croquette;
    ctx.beginPath();
    ctx.arc(cx + ox, cy + oy, i === 0 ? 5 : 3.5, 0, Math.PI * 2);
    ctx.fill();
  });

  ctx.fillStyle = "#f5e6c8";
  ctx.font = "bold 9px DM Sans, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText("croq", cx, cy + 14);
}

function drawTailSegment(seg, i) {
  const cx = seg.x * CELL + CELL / 2;
  const cy = seg.y * CELL + CELL / 2;
  const r = CELL * 0.38 - i * 0.4;

  const grad = ctx.createRadialGradient(cx - 2, cy - 2, 1, cx, cy, r);
  grad.addColorStop(0, COLORS.tail);
  grad.addColorStop(1, COLORS.tailDark);
  ctx.fillStyle = grad;
  ctx.beginPath();
  ctx.ellipse(cx, cy, r, r * 0.85, 0, 0, Math.PI * 2);
  ctx.fill();

  if (i % 2 === 0) {
    ctx.fillStyle = "rgba(80, 50, 30, 0.35)";
    ctx.beginPath();
    ctx.arc(cx - 3, cy, 1.5, 0, Math.PI * 2);
    ctx.arc(cx + 3, cy + 2, 1.2, 0, Math.PI * 2);
    ctx.fill();
  }
}

function drawNahlaHead(seg) {
  const cx = seg.x * CELL + CELL / 2;
  const cy = seg.y * CELL + CELL / 2;
  const size = CELL * 1.05;

  ctx.fillStyle = "rgba(244, 162, 97, 0.35)";
  ctx.beginPath();
  ctx.arc(cx, cy, size * 0.55, 0, Math.PI * 2);
  ctx.fill();

  if (nahlaReady) {
    const angle = Math.atan2(dir.y, dir.x) + Math.PI / 2;
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(angle);
    ctx.beginPath();
    ctx.arc(0, 0, size * 0.52, 0, Math.PI * 2);
    ctx.closePath();
    ctx.clip();
    ctx.drawImage(nahlaImg, -size / 2, -size / 2, size, size);
    ctx.restore();
  } else {
    ctx.fillStyle = COLORS.tail;
    ctx.beginPath();
    ctx.arc(cx, cy, size * 0.4, 0, Math.PI * 2);
    ctx.fill();
  }
}

function drawSnake() {
  for (let i = snake.length - 1; i >= 1; i--) {
    drawTailSegment(snake[i], i);
  }
  drawNahlaHead(snake[0]);
}

function drawMiam() {
  if (!miamText || Date.now() > miamUntil) return;
  ctx.fillStyle = "#f4a261";
  ctx.font = "bold 14px DM Sans, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(miamText, canvas.width / 2, 28);
}

function draw() {
  drawSalon();
  drawCroquette();
  drawSnake();
  drawMiam();
}

function tick() {
  if (paused || state !== "playing") return;

  dir = nextDir;
  const head = { x: snake[0].x + dir.x, y: snake[0].y + dir.y };

  if (head.x < 0 || head.x >= GRID || head.y < 0 || head.y >= GRID) {
    return gameOver("Nahla a percuté le mur du salon.");
  }
  if (MEUBLES.some((m) => head.x >= m.x && head.x < m.x + m.w && head.y >= m.y && head.y < m.y + m.h)) {
    return gameOver("Nahla s'est cognée contre un meuble.");
  }
  if (snake.some((s) => s.x === head.x && s.y === head.y)) {
    return gameOver("Nahla s'est mordu la queue. Classique.");
  }

  snake.unshift(head);

  if (head.x === croquette.x && head.y === croquette.y) {
    score += 1;
    scoreEl.textContent = score;
    miamText = MIAM_LINES[Math.floor(Math.random() * MIAM_LINES.length)];
    miamUntil = Date.now() + 700;
    if (score > record) {
      record = score;
      recordEl.textContent = record;
      localStorage.setItem("nahlaSnakeRecord", record);
    }
    spawnCroquette();
  } else {
    snake.pop();
  }

  draw();
}

function gameOver(msg) {
  state = "over";
  clearInterval(loopId);
  overlayTitle.textContent = "Nahla a échoué";
  overlayMsg.textContent = `${msg} Croquettes : ${score}`;
  startBtn.textContent = "Rejouer";
  overlay.classList.remove("hidden");
}

function startGame() {
  clearInterval(loopId);
  resetGame();
  overlay.classList.add("hidden");
  draw();
  loopId = setInterval(tick, TICK_MS);
}

function setDirection(nx, ny) {
  if (state !== "playing") return;
  if (nx === -dir.x && ny === -dir.y) return;
  nextDir = { x: nx, y: ny };
}

document.addEventListener("keydown", (e) => {
  const key = e.key.toLowerCase();
  if (key === "arrowup" || key === "z" || key === "w") setDirection(0, -1);
  if (key === "arrowdown" || key === "s") setDirection(0, 1);
  if (key === "arrowleft" || key === "q" || key === "a") setDirection(-1, 0);
  if (key === "arrowright" || key === "d") setDirection(1, 0);
  if (key === " ") {
    e.preventDefault();
    if (state === "playing") paused = !paused;
  }
  if (key === "r" && state === "over") startGame();
});

startBtn.addEventListener("click", startGame);

overlay.classList.remove("hidden");
draw();
