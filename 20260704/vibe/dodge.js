const canvas = document.getElementById("dodge-canvas");
const ctx = canvas.getContext("2d");

const W = canvas.width;
const H = canvas.height;

const OBJECT_LABELS = [
  "brosse", "reveil", "seringue", "croquettes",
  "laser", "aspirateur", "shampoing", "cage", "collier",
];

const NAHLA_SIZE = 64;
const OBJECT_SIZE = 48;
const SPAWN_MARGIN = 40;
const NAHLA_HITBOX_INSET = { x: 20, y: 16 };
const OBJECT_HITBOX_INSET = 12;
const COLLISION_SUBSTEP = 8;

const LEVELS = [
  {
    id: "chill", name: "Chill", tagline: "Nahla dort, rien ne presse",
    baseSpeed: 2, maxSpeed: 6, accelStep: 180, objectCount: 5, nahlaSpeed: 7, color: "#64be82",
  },
  {
    id: "normal", name: "Normal", tagline: "Une journée classique",
    baseSpeed: 3, maxSpeed: 10, accelStep: 100, objectCount: 8, nahlaSpeed: 6, color: "#78aade",
  },
  {
    id: "stress", name: "Stress", tagline: "Réveil à 6h + brosse + aspirateur",
    baseSpeed: 4.5, maxSpeed: 13, accelStep: 70, objectCount: 10, nahlaSpeed: 5, color: "#f0aa46",
  },
  {
    id: "enfer", name: "Enfer", tagline: "Jour chez le véto, tout tombe",
    baseSpeed: 6, maxSpeed: 16, accelStep: 45, objectCount: 12, nahlaSpeed: 5, color: "#e65050",
  },
];

const nahlaImg = new Image();
nahlaImg.src = "nahla_head.png";

let mode = "menu";
let menuIndex = 1;
let state = null;
let keys = {};
let last = 0;

function fallSpeedForScore(score, level) {
  return Math.min(level.maxSpeed, level.baseSpeed + Math.floor(score / level.accelStep));
}

function insetRect(rect, xInset, yInset) {
  return {
    x: rect.x + xInset,
    y: rect.y + yInset,
    w: rect.w - xInset * 2,
    h: rect.h - yInset * 2,
  };
}

function nahlaHitbox(nahlaRect) {
  return insetRect(nahlaRect, NAHLA_HITBOX_INSET.x, NAHLA_HITBOX_INSET.y);
}

function objectHitbox(objRect) {
  return insetRect(objRect, OBJECT_HITBOX_INSET, OBJECT_HITBOX_INSET);
}

function rectsCollide(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

function objectHitsNahla(nahlaRect, obj) {
  const nahlaHb = nahlaHitbox(nahlaRect);
  let remaining = obj.speed;
  while (remaining > 0) {
    const step = Math.min(remaining, COLLISION_SUBSTEP);
    obj.rect.y += step;
    remaining -= step;
    if (rectsCollide(nahlaHb, objectHitbox(obj.rect))) return true;
  }
  return false;
}

function spawnObject(existing, level) {
  let x = SPAWN_MARGIN + Math.random() * (W - SPAWN_MARGIN * 2 - OBJECT_SIZE);
  for (let i = 0; i < 20; i++) {
    x = SPAWN_MARGIN + Math.random() * (W - SPAWN_MARGIN * 2 - OBJECT_SIZE);
    if (existing.every((o) => Math.abs(x + OBJECT_SIZE / 2 - (o.rect.x + OBJECT_SIZE / 2)) > OBJECT_SIZE)) break;
  }
  const label = OBJECT_LABELS[Math.floor(Math.random() * OBJECT_LABELS.length)];
  const base = level.baseSpeed;
  return {
    rect: { x, y: -OBJECT_SIZE - Math.random() * H, w: OBJECT_SIZE, h: OBJECT_SIZE },
    label,
    speed: base + Math.random() * 1.5,
  };
}

function resetGame(level) {
  const objects = [];
  for (let i = 0; i < level.objectCount; i++) objects.push(spawnObject(objects, level));
  return {
    level,
    nahlaRect: { x: W / 2 - NAHLA_SIZE / 2, y: H - NAHLA_SIZE - 30, w: NAHLA_SIZE, h: NAHLA_SIZE },
    objects,
    score: 0,
    gameOver: false,
    elapsedMs: 0,
  };
}

function roundRect(x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

function drawBrosse(x, y, s) {
  ctx.fillStyle = "#784b2d";
  roundRect(x + s * 0.42, y + s * 0.08, s * 0.16, s * 0.46, 3);
  ctx.fill();
  ctx.fillStyle = "#d2aa6e";
  roundRect(x + s * 0.29, y + s * 0.5, s * 0.42, s * 0.2, 4);
  ctx.fill();
  ctx.strokeStyle = "#f0d296";
  ctx.lineWidth = 2;
  for (let i = 0; i < 6; i++) {
    const px = x + s * (0.33 + i * 0.06);
    ctx.beginPath();
    ctx.moveTo(px, y + s * 0.7);
    ctx.lineTo(px, y + s * 0.92);
    ctx.stroke();
  }
}

function drawReveil(x, y, s) {
  ctx.fillStyle = "#ffd23c";
  ctx.beginPath();
  ctx.arc(x + s * 0.25, y + s * 0.28, s * 0.1, 0, Math.PI * 2);
  ctx.arc(x + s * 0.75, y + s * 0.28, s * 0.1, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#e63c3c";
  ctx.beginPath();
  ctx.arc(x + s * 0.5, y + s * 0.58, s * 0.32, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#fff5e6";
  ctx.beginPath();
  ctx.arc(x + s * 0.5, y + s * 0.58, s * 0.2, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = "#1e1e1e";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(x + s * 0.5, y + s * 0.58);
  ctx.lineTo(x + s * 0.5, y + s * 0.42);
  ctx.moveTo(x + s * 0.5, y + s * 0.58);
  ctx.lineTo(x + s * 0.62, y + s * 0.58);
  ctx.stroke();
}

function drawSeringue(x, y, s) {
  ctx.fillStyle = "#d2e6f5";
  roundRect(x + s * 0.38, y + s * 0.36, s * 0.24, s * 0.42, 2);
  ctx.fill();
  ctx.fillStyle = "#50b4ff";
  roundRect(x + s * 0.42, y + s * 0.5, s * 0.16, s * 0.24, 1);
  ctx.fill();
  ctx.fillStyle = "#c8c8d2";
  roundRect(x + s * 0.42, y + s * 0.16, s * 0.16, s * 0.24, 2);
  ctx.fill();
  ctx.strokeStyle = "#a0a0aa";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(x + s * 0.5, y + s * 0.78);
  ctx.lineTo(x + s * 0.5, y + s * 0.96);
  ctx.stroke();
}

function drawCroquettes(x, y, s) {
  ctx.fillStyle = "#c8503c";
  ctx.beginPath();
  ctx.ellipse(x + s * 0.5, y + s * 0.72, s * 0.28, s * 0.14, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#f0785a";
  ctx.beginPath();
  ctx.ellipse(x + s * 0.5, y + s * 0.66, s * 0.24, s * 0.1, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#965a28";
  [[0.33, 0.5], [0.46, 0.46], [0.58, 0.5], [0.42, 0.58], [0.54, 0.58]].forEach(([px, py]) => {
    ctx.beginPath();
    ctx.arc(x + s * px, y + s * py, s * 0.06, 0, Math.PI * 2);
    ctx.fill();
  });
}

function drawLaser(x, y, s) {
  ctx.fillStyle = "#323237";
  ctx.beginPath();
  ctx.moveTo(x + s * 0.2, y + s * 0.75);
  ctx.lineTo(x + s * 0.58, y + s * 0.75);
  ctx.lineTo(x + s * 0.7, y + s * 0.62);
  ctx.lineTo(x + s * 0.2, y + s * 0.62);
  ctx.fill();
  ctx.fillStyle = "#dc283c";
  ctx.beginPath();
  ctx.arc(x + s * 0.25, y + s * 0.68, s * 0.06, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = "#ff5050";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(x + s * 0.7, y + s * 0.62);
  ctx.lineTo(x + s * 0.88, y + s * 0.16);
  ctx.stroke();
  ctx.fillStyle = "#ff5050";
  ctx.beginPath();
  ctx.arc(x + s * 0.88, y + s * 0.16, s * 0.1, 0, Math.PI * 2);
  ctx.fill();
}

function drawAspirateur(x, y, s) {
  ctx.fillStyle = "#787882";
  roundRect(x + s * 0.38, y + s * 0.2, s * 0.28, s * 0.54, 4);
  ctx.fill();
  ctx.fillStyle = "#a0a0aa";
  ctx.beginPath();
  ctx.moveTo(x + s * 0.33, y + s * 0.75);
  ctx.lineTo(x + s * 0.7, y + s * 0.75);
  ctx.lineTo(x + s * 0.62, y + s * 0.92);
  ctx.lineTo(x + s * 0.42, y + s * 0.92);
  ctx.fill();
}

function drawShampoing(x, y, s) {
  ctx.fillStyle = "#5ab4dc";
  roundRect(x + s * 0.33, y + s * 0.33, s * 0.34, s * 0.54, 4);
  ctx.fill();
  ctx.fillStyle = "#f0f0f5";
  roundRect(x + s * 0.38, y + s * 0.16, s * 0.24, s * 0.2, 2);
  ctx.fill();
  ctx.fillStyle = "#fff";
  roundRect(x + s * 0.38, y + s * 0.46, s * 0.24, s * 0.2, 2);
  ctx.fill();
  ctx.fillStyle = "#fff";
  ctx.beginPath();
  ctx.arc(x + s * 0.46, y + s * 0.7, s * 0.04, 0, Math.PI * 2);
  ctx.arc(x + s * 0.58, y + s * 0.75, s * 0.05, 0, Math.PI * 2);
  ctx.fill();
}

function drawCage(x, y, s) {
  ctx.fillStyle = "#64646e";
  roundRect(x + s * 0.16, y + s * 0.62, s * 0.68, s * 0.28, 3);
  ctx.fill();
  ctx.fillStyle = "#b4bec8";
  roundRect(x + s * 0.2, y + s * 0.2, s * 0.6, s * 0.46, 4);
  ctx.fill();
  ctx.strokeStyle = "#464650";
  ctx.lineWidth = 2;
  for (let i = 0; i < 4; i++) {
    const px = x + s * (0.28 + i * 0.14);
    ctx.beginPath();
    ctx.moveTo(px, y + s * 0.24);
    ctx.lineTo(px, y + s * 0.62);
    ctx.stroke();
  }
  for (let i = 0; i < 3; i++) {
    const py = y + s * (0.32 + i * 0.12);
    ctx.beginPath();
    ctx.moveTo(x + s * 0.24, py);
    ctx.lineTo(x + s * 0.76, py);
    ctx.stroke();
  }
}

function drawCollier(x, y, s) {
  ctx.strokeStyle = "#c83232";
  ctx.lineWidth = 5;
  ctx.beginPath();
  ctx.arc(x + s * 0.5, y + s * 0.72, s * 0.32, Math.PI * 1.1, Math.PI * 1.9);
  ctx.stroke();
  ctx.fillStyle = "#ffd23c";
  ctx.beginPath();
  ctx.moveTo(x + s * 0.46, y + s * 0.7);
  ctx.lineTo(x + s * 0.54, y + s * 0.7);
  ctx.lineTo(x + s * 0.58, y + s * 0.88);
  ctx.lineTo(x + s * 0.42, y + s * 0.88);
  ctx.fill();
}

const SPRITE_DRAWERS = {
  brosse: drawBrosse, reveil: drawReveil, seringue: drawSeringue,
  croquettes: drawCroquettes, laser: drawLaser, aspirateur: drawAspirateur,
  shampoing: drawShampoing, cage: drawCage, collier: drawCollier,
};

function drawObject(obj) {
  const fn = SPRITE_DRAWERS[obj.label];
  if (fn) fn(obj.rect.x, obj.rect.y, OBJECT_SIZE);
}

function levelButtonRect(index) {
  return { x: W / 2 - 220, y: 170 + index * 92, w: 440, h: 72 };
}

function drawMenu() {
  ctx.fillStyle = "#12121c";
  ctx.fillRect(0, 0, W, H);

  ctx.fillStyle = "#ffd250";
  ctx.font = "bold 52px 'Playfair Display', serif";
  ctx.textAlign = "center";
  ctx.fillText("Nahla Dodge", W / 2, 70);

  ctx.fillStyle = "#8c8896";
  ctx.font = "22px 'DM Sans', sans-serif";
  ctx.fillText("Choisis ton niveau de souffrance", W / 2, 118);

  if (nahlaImg.complete) ctx.drawImage(nahlaImg, W - 110, 40, 64, 64);

  LEVELS.forEach((level, index) => {
    const rect = levelButtonRect(index);
    const selected = index === menuIndex;
    ctx.fillStyle = selected ? level.color : "#1c1c2a";
    roundRect(rect.x, rect.y, rect.w, rect.h, 12);
    ctx.fill();
    ctx.strokeStyle = selected ? "#ffd250" : "#3c3c50";
    ctx.lineWidth = selected ? 3 : 2;
    roundRect(rect.x, rect.y, rect.w, rect.h, 12);
    ctx.stroke();

    ctx.textAlign = "left";
    ctx.fillStyle = selected ? "#12121c" : "#f0ebe0";
    ctx.font = "bold 28px 'DM Sans', sans-serif";
    ctx.fillText(level.name, rect.x + 18, rect.y + 32);
    ctx.font = "18px 'DM Sans', sans-serif";
    ctx.fillStyle = selected ? "#12121c" : "#8c8896";
    ctx.fillText(level.tagline, rect.x + 18, rect.y + 54);
    ctx.fillText(`${level.objectCount} objets · vitesse max ${level.maxSpeed}`, rect.x + 18, rect.y + 68);
  });

  ctx.textAlign = "center";
  ctx.fillStyle = "#8c8896";
  ctx.font = "18px 'DM Sans', sans-serif";
  ctx.fillText("↑ ↓ ou Z/S · Entrée · clic", W / 2, H - 28);
}

function drawGameOver() {
  ctx.fillStyle = "rgba(0,0,0,0.65)";
  ctx.fillRect(0, 0, W, H);
  ctx.textAlign = "center";
  ctx.fillStyle = "#dc4646";
  ctx.font = "bold 56px 'DM Sans', sans-serif";
  ctx.fillText("GAME OVER", W / 2, H / 2 - 56);
  ctx.fillStyle = "#f0ebe0";
  ctx.font = "24px 'DM Sans', sans-serif";
  ctx.fillText(`Score final : ${state.score} (${state.level.name})`, W / 2, H / 2 - 8);
  ctx.fillStyle = "#ffd250";
  ctx.fillText("R — Rejouer ce niveau", W / 2, H / 2 + 32);
  ctx.fillStyle = "#f0ebe0";
  ctx.fillText("M — Retour au menu", W / 2, H / 2 + 62);
}

function update(dt) {
  if (mode !== "playing" || !state || state.gameOver) return;

  const level = state.level;
  let move = 0;
  if (keys.ArrowLeft || keys.a || keys.q) move -= level.nahlaSpeed;
  if (keys.ArrowRight || keys.d || keys.s) move += level.nahlaSpeed;

  state.nahlaRect.x += move;
  state.nahlaRect.x = Math.max(0, Math.min(W - NAHLA_SIZE, state.nahlaRect.x));

  state.elapsedMs += dt;
  state.score = Math.floor(state.elapsedMs / 100);
  const fallSpeed = fallSpeedForScore(state.score, level);

  for (const obj of state.objects) {
    obj.speed = Math.max(obj.speed, fallSpeed);
    if (objectHitsNahla(state.nahlaRect, obj)) {
      state.gameOver = true;
      return;
    }
    if (obj.rect.y > H) {
      const others = state.objects.filter((o) => o !== obj);
      const fresh = spawnObject(others, level);
      obj.rect = fresh.rect;
      obj.label = fresh.label;
      obj.speed = fallSpeed + Math.random() * 1.5;
    }
  }
}

function drawGame() {
  ctx.fillStyle = "#12121c";
  ctx.fillRect(0, 0, W, H);

  state.objects.forEach(drawObject);

  if (nahlaImg.complete) {
    ctx.drawImage(nahlaImg, state.nahlaRect.x, state.nahlaRect.y, NAHLA_SIZE, NAHLA_SIZE);
  } else {
    ctx.fillStyle = "#c8a078";
    ctx.beginPath();
    ctx.ellipse(
      state.nahlaRect.x + NAHLA_SIZE / 2,
      state.nahlaRect.y + NAHLA_SIZE / 2,
      NAHLA_SIZE / 2,
      NAHLA_SIZE / 2,
      0, 0, Math.PI * 2,
    );
    ctx.fill();
  }

  const fallSpeed = fallSpeedForScore(state.score, state.level);
  ctx.textAlign = "left";
  ctx.fillStyle = "#f0ebe0";
  ctx.font = "22px 'DM Sans', sans-serif";
  ctx.fillText(`Score : ${state.score}`, 20, 28);
  ctx.fillStyle = "#8c8896";
  ctx.fillText(`Vitesse : ${fallSpeed.toFixed(1)}`, 20, 52);
  ctx.textAlign = "right";
  ctx.fillStyle = "#ffd250";
  ctx.fillText(`Niveau : ${state.level.name}`, W - 20, 28);

  if (state.gameOver) drawGameOver();
}

function frame(ts) {
  const dt = last ? Math.min(ts - last, 50) : 16;
  last = ts;

  if (mode === "menu") drawMenu();
  else if (mode === "playing" && state) {
    update(dt);
    drawGame();
  }

  requestAnimationFrame(frame);
}

function startLevel(index) {
  menuIndex = index;
  state = resetGame(LEVELS[index]);
  mode = "playing";
}

canvas.addEventListener("click", (e) => {
  if (mode !== "menu") return;
  const rect = canvas.getBoundingClientRect();
  const sx = W / rect.width;
  const sy = H / rect.height;
  const x = (e.clientX - rect.left) * sx;
  const y = (e.clientY - rect.top) * sy;
  LEVELS.forEach((_, i) => {
    const btn = levelButtonRect(i);
    if (x >= btn.x && x <= btn.x + btn.w && y >= btn.y && y <= btn.y + btn.h) startLevel(i);
  });
});

window.addEventListener("keydown", (e) => {
  keys[e.key] = true;

  if (mode === "menu") {
    if (e.key === "ArrowUp" || e.key === "w" || e.key === "z") {
      menuIndex = (menuIndex - 1 + LEVELS.length) % LEVELS.length;
    }
    if (e.key === "ArrowDown" || e.key === "s") {
      menuIndex = (menuIndex + 1) % LEVELS.length;
    }
    if (e.key === "Enter" || e.key === " ") startLevel(menuIndex);
  } else if (mode === "playing" && state) {
    if (e.key === "r" && state.gameOver) state = resetGame(state.level);
    if (e.key === "m" && state.gameOver) {
      mode = "menu";
      state = null;
    }
    if (e.key === "Escape") {
      mode = "menu";
      state = null;
    }
  }
});

window.addEventListener("keyup", (e) => {
  keys[e.key] = false;
});

requestAnimationFrame(frame);
