const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const VW = canvas.width;
const VH = canvas.height;
const WORLD_W = 3200;
const WORLD_H = 2200;
const MARGIN = 64;

const NAHLA_SPEED = 5.2;
const NAHLA_R = 34;
const HIT_R = 26;
const CLAW_RANGE = 130;
const CLAW_COOLDOWN = 1500;
const CLAW_KNOCKBACK = 16;

const HUMAN_TYPES = {
  malik: { name: "Malik", color: "#ffc878", speed: 2.4, r: 22 },
  kays: { name: "Kays", color: "#8cbfff", speed: 2.0, r: 20 },
  noah: { name: "Noah", color: "#b4ffa0", speed: 2.8, r: 18 },
  maman: { name: "Maman", color: "#ffa0dc", speed: 1.1, r: 44 },
};

const PHRASES = {
  malik: ["Viens là !", "NAHLA !", "Je t'aime !", "Bisou bisou !", "Attends-moi !"],
  kays: ["Hé le chat !", "Laisse-toi faire.", "T'es mignonne.", "Bouge pas.", "C'est pour ton bien."],
  noah: ["Nahla !", "Ma puce !", "Caresses !", "Viens ici !", "T'es trop belle."],
  maman: ["Oh mon chaton !", "Ma puce adorée !", "Viens ma chérie !", "Le plus beau chat !", "Maman t'aime !"],
};

const KEYS = {};
const scoreEl = document.getElementById("score");
const waveEl = document.getElementById("wave");
const recordEl = document.getElementById("record");
const overlay = document.getElementById("overlay");
const gameover = document.getElementById("gameover");
const goMsg = document.getElementById("go-msg");
const goScore = document.getElementById("go-score");
const clawFill = document.getElementById("claw-fill");
const startBtn = document.getElementById("start-btn");
const retryBtn = document.getElementById("retry-btn");

const nahlaImg = new Image();
nahlaImg.src = "nahla_head.png";
let nahlaReady = false;
nahlaImg.onload = () => {
  nahlaReady = true;
};

let record = Number(localStorage.getItem("nahlaArenaRecord") || 0);
recordEl.textContent = record;

let state = "menu";
let nahla, humans, camX, camY;
let elapsed = 0;
let spawnTimer = 0;
let spawnInterval = 3200;
let speedMult = 1;
let maxHumans = 5;
let wave = 1;
let lastMamanWave = 0;
let clawCd = 0;
let clawFx = 0;
let caughtBy = "";
let lastTime = 0;
let animId;

class Nahla {
  constructor() {
    this.x = WORLD_W / 2;
    this.y = WORLD_H / 2;
  }

  update() {
    let vx = 0;
    let vy = 0;
    if (KEYS.left) vx -= NAHLA_SPEED;
    if (KEYS.right) vx += NAHLA_SPEED;
    if (KEYS.up) vy -= NAHLA_SPEED;
    if (KEYS.down) vy += NAHLA_SPEED;
    const len = Math.hypot(vx, vy);
    if (len > NAHLA_SPEED) {
      vx = (vx / len) * NAHLA_SPEED;
      vy = (vy / len) * NAHLA_SPEED;
    }
    this.x += vx;
    this.y += vy;
    [this.x, this.y] = clampWorld(this.x, this.y);
  }
}

class Human {
  constructor(kind, x, y) {
    const info = HUMAN_TYPES[kind];
    this.kind = kind;
    this.name = info.name;
    this.color = info.color;
    this.baseSpeed = info.speed;
    this.speed = info.speed;
    this.r = info.r;
    this.x = x;
    this.y = y;
    this.phrase = PHRASES[kind][Math.floor(Math.random() * PHRASES[kind].length)];
    this.phraseMs = 2800;
    this.kbX = 0;
    this.kbY = 0;
    this.kbMs = 0;
  }

  applyKnockback(fromX, fromY, force) {
    const dx = this.x - fromX;
    const dy = this.y - fromY;
    const dist = Math.hypot(dx, dy) || 1;
    this.kbX = (dx / dist) * force;
    this.kbY = (dy / dist) * force;
    this.kbMs = 350;
  }

  update(targetX, targetY, dt) {
    this.phraseMs = Math.max(0, this.phraseMs - dt);
    if (this.kbMs > 0) {
      this.kbMs -= dt;
      this.x += this.kbX;
      this.y += this.kbY;
      this.kbX *= 0.88;
      this.kbY *= 0.88;
      [this.x, this.y] = clampWorld(this.x, this.y, 20);
      return;
    }
    const dx = targetX - this.x;
    const dy = targetY - this.y;
    const dist = Math.hypot(dx, dy) || 1;
    this.x += (dx / dist) * this.speed;
    this.y += (dy / dist) * this.speed;
  }
}

function clampWorld(x, y, margin = MARGIN) {
  return [
    Math.max(margin, Math.min(WORLD_W - margin, x)),
    Math.max(margin, Math.min(WORLD_H - margin, y)),
  ];
}

function spawnAtViewportEdge(cx, cy) {
  const side = Math.floor(Math.random() * 4);
  const pad = 80;
  let x, y;
  if (side === 0) {
    x = cx + Math.random() * (VW - pad * 2) + pad;
    y = cy - 40;
  } else if (side === 1) {
    x = cx + Math.random() * (VW - pad * 2) + pad;
    y = cy + VH + 40;
  } else if (side === 2) {
    x = cx - 40;
    y = cy + Math.random() * (VH - pad * 2) + pad;
  } else {
    x = cx + VW + 40;
    y = cy + Math.random() * (VH - pad * 2) + pad;
  }
  return clampWorld(x, y, 20);
}

function updateCamera() {
  camX = nahla.x - VW / 2;
  camY = nahla.y - VH / 2;
  camX = Math.max(0, Math.min(WORLD_W - VW, camX));
  camY = Math.max(0, Math.min(WORLD_H - VH, camY));
}

function updateDifficulty() {
  const seconds = elapsed / 1000;
  speedMult = 1 + seconds * 0.035;
  spawnInterval = Math.max(650, 3200 - seconds * 28);
  wave = 1 + Math.floor(seconds / 15);
  maxHumans = Math.min(14, 5 + Math.floor(seconds / 18));
}

function spawnHuman(forcedKind) {
  if (humans.length >= maxHumans) return;
  let kind = forcedKind;
  const noMaman = !humans.some((h) => h.kind === "maman");
  if (!kind) {
    if (noMaman && wave >= 3 && wave > lastMamanWave) {
      kind = "maman";
      lastMamanWave = wave;
    } else if (noMaman && Math.random() < 0.22) {
      kind = "maman";
    } else {
      kind = ["malik", "kays", "noah"][Math.floor(Math.random() * 3)];
    }
  }
  const [sx, sy] = spawnAtViewportEdge(camX, camY);
  humans.push(new Human(kind, sx, sy));
}

function doClaw() {
  if (clawCd > 0) return;
  clawCd = CLAW_COOLDOWN;
  clawFx = 220;
  humans.forEach((h) => {
    const dist = Math.hypot(h.x - nahla.x, h.y - nahla.y);
    if (dist <= CLAW_RANGE + h.r) {
      h.applyKnockback(nahla.x, nahla.y, CLAW_KNOCKBACK);
    }
  });
}

function resetGame() {
  nahla = new Nahla();
  humans = [];
  elapsed = 0;
  spawnTimer = 0;
  spawnInterval = 3200;
  speedMult = 1;
  maxHumans = 5;
  wave = 1;
  lastMamanWave = 0;
  clawCd = 0;
  clawFx = 0;
  caughtBy = "";
  updateCamera();
  scoreEl.textContent = "0";
  waveEl.textContent = "1";
}

function startGame() {
  resetGame();
  state = "playing";
  overlay.classList.add("hidden");
  gameover.classList.add("hidden");
  lastTime = performance.now();
  cancelAnimationFrame(animId);
  animId = requestAnimationFrame(loop);
}

function endGame(name) {
  state = "over";
  caughtBy = name;
  const score = Math.floor(elapsed / 1000);
  if (score > record) {
    record = score;
    localStorage.setItem("nahlaArenaRecord", String(record));
    recordEl.textContent = record;
  }
  goMsg.textContent = `${caughtBy} t'a caressée. Nahla est furieuse.`;
  goScore.textContent = score;
  gameover.classList.remove("hidden");
}

function drawFloor() {
  ctx.fillStyle = "#2a2430";
  ctx.fillRect(0, 0, VW, VH);
  const tile = 64;
  const startX = Math.floor(camX / tile) * tile;
  const startY = Math.floor(camY / tile) * tile;
  for (let y = startY; y < camY + VH + tile; y += tile) {
    for (let x = startX; x < camX + VW + tile; x += tile) {
      const sx = x - camX;
      const sy = y - camY;
      ctx.fillStyle = (x / tile + y / tile) % 2 === 0 ? "#3a323e" : "#342e38";
      ctx.fillRect(sx, sy, tile, tile);
    }
  }
  ctx.strokeStyle = "#1c181f";
  ctx.lineWidth = 8;
  ctx.strokeRect(-camX, -camY, WORLD_W, WORLD_H);
}

function drawBubble(h, sx, sy) {
  ctx.font = "16px DM Sans, sans-serif";
  const text = h.phrase;
  const padX = 10;
  const padY = 6;
  const tw = ctx.measureText(text).width;
  const bw = tw + padX * 2;
  const bh = 28;
  let bx = sx - bw / 2;
  let by = sy - h.r - bh - 14;
  bx = Math.max(8, Math.min(VW - bw - 8, bx));
  by = Math.max(8, by);
  ctx.fillStyle = "#faf5ff";
  ctx.beginPath();
  ctx.roundRect(bx, by, bw, bh, 8);
  ctx.fill();
  ctx.strokeStyle = "#b4aabf";
  ctx.stroke();
  ctx.fillStyle = "#1e1c26";
  ctx.fillText(text, bx + padX, by + 20);
}

function draw() {
  drawFloor();

  humans.forEach((h) => {
    const sx = h.x - camX;
    const sy = h.y - camY;
    if (h.kind === "maman") {
      ctx.fillStyle = "#ffbee6";
      ctx.beginPath();
      ctx.arc(sx, sy, h.r + 4, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.fillStyle = h.color;
    ctx.beginPath();
    ctx.arc(sx, sy, h.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = "#fff";
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.fillStyle = "#1e1c26";
    ctx.font = "bold 18px DM Sans, sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(h.name[0], sx, sy);
    if (h.phraseMs > 0) drawBubble(h, sx, sy);
  });

  const nx = nahla.x - camX;
  const ny = nahla.y - camY;
  if (nahlaReady) {
    const w = 72;
    const h = (w * nahlaImg.height) / nahlaImg.width;
    ctx.drawImage(nahlaImg, nx - w / 2, ny - h / 2, w, h);
  } else {
    ctx.fillStyle = "#f4a261";
    ctx.beginPath();
    ctx.arc(nx, ny, NAHLA_R, 0, Math.PI * 2);
    ctx.fill();
  }

  if (clawFx > 0) {
    const alpha = clawFx / 220;
    ctx.strokeStyle = `rgba(255, 120, 90, ${alpha * 0.8})`;
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.arc(nx, ny, CLAW_RANGE, 0, Math.PI * 2);
    ctx.stroke();
    for (const a of [-0.5, 0, 0.5]) {
      ctx.beginPath();
      ctx.moveTo(nx, ny);
      ctx.lineTo(nx + Math.cos(a) * CLAW_RANGE * 0.7, ny + Math.sin(a) * CLAW_RANGE * 0.7);
      ctx.stroke();
    }
  }

  ctx.fillStyle = "rgba(20, 16, 28, 0.75)";
  ctx.fillRect(0, VH - 32, VW, 32);
  ctx.fillStyle = "#9a9288";
  ctx.font = "18px DM Sans, sans-serif";
  ctx.textAlign = "left";
  ctx.fillText(`${humans.length}/${maxHumans} humains — ESPACE : griffe`, 16, VH - 10);
}

function update(dt) {
  nahla.update();
  updateCamera();
  elapsed += dt;
  scoreEl.textContent = Math.floor(elapsed / 1000);
  clawCd = Math.max(0, clawCd - dt);
  clawFx = Math.max(0, clawFx - dt);
  clawFill.style.width = clawCd <= 0 ? "100%" : `${(1 - clawCd / CLAW_COOLDOWN) * 100}%`;
  clawFill.style.background = clawCd <= 0 ? "#64d28c" : "#9a9288";

  updateDifficulty();
  waveEl.textContent = wave;

  spawnTimer += dt;
  if (spawnTimer >= spawnInterval) {
    spawnTimer = 0;
    spawnHuman();
  }

  for (const h of humans) {
    h.speed = h.baseSpeed * speedMult;
    h.update(nahla.x, nahla.y, dt);
    if (Math.hypot(nahla.x - h.x, nahla.y - h.y) < HIT_R + h.r) {
      endGame(h.name);
      return;
    }
  }
}

function loop(now) {
  if (state !== "playing") return;
  const dt = Math.min(50, now - lastTime);
  lastTime = now;
  update(dt);
  draw();
  animId = requestAnimationFrame(loop);
}

document.addEventListener("keydown", (e) => {
  const k = e.key.toLowerCase();
  if (["arrowup", "arrowdown", "arrowleft", "arrowright", " ", "z", "q", "s", "d", "w", "a", "r", "escape"].includes(k) || e.key.startsWith("Arrow")) {
    e.preventDefault();
  }
  if (k === "arrowleft" || k === "q" || k === "a") KEYS.left = true;
  if (k === "arrowright" || k === "d") KEYS.right = true;
  if (k === "arrowup" || k === "z" || k === "w") KEYS.up = true;
  if (k === "arrowdown" || k === "s") KEYS.down = true;

  if (k === " " && state === "playing") doClaw();
  if (k === "r") startGame();
  if (k === "escape" && state === "playing") {
    state = "menu";
    overlay.classList.remove("hidden");
    cancelAnimationFrame(animId);
  }
});

document.addEventListener("keyup", (e) => {
  const k = e.key.toLowerCase();
  if (k === "arrowleft" || k === "q" || k === "a") KEYS.left = false;
  if (k === "arrowright" || k === "d") KEYS.right = false;
  if (k === "arrowup" || k === "z" || k === "w") KEYS.up = false;
  if (k === "arrowdown" || k === "s") KEYS.down = false;
});

startBtn.addEventListener("click", startGame);
retryBtn.addEventListener("click", startGame);

draw();
