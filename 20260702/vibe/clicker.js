const canvas = document.getElementById("clicker-canvas");
const ctx = canvas.getContext("2d");

const W = canvas.width;
const H = canvas.height;

const COUCH = "#c4a884";
const COUCH_DARK = "#a88e6c";
const PANEL = "#947c60";
const PANEL_LIGHT = "#b09676";
const SELECTED = "#ffdc78";
const TORTIE_DARK = "#3a2a24";
const TEXT = "#372818";
const MUTED = "#6e5a46";
const ACCENT = "#ffd250";
const CROQUETTE = "#b47828";

const NAHLA_BASE_SIZE = 70;
const GROW_EVERY = 10;
const GROW_AMOUNT = 8;
const PHRASE_EVERY = 15;

const HUNGER_MAX = 100;
const HUNGER_DRAIN = 5.5;
const HUNGER_LOW_THRESHOLD = 30;
const HUNGER_COMPLAIN_MS = 2200;
const BOUNCE_MS = 180;

const RESET_RECT = { x: W - 132, y: 20, w: 100, h: 38 };

const LEVELS = [
  [0, "Chat normal"],
  [10, "Chat dodu"],
  [30, "Boule"],
  [60, "Rouleau de Nahla"],
  [100, "Menace planétaire"],
];

const FOODS = [
  { name: "Croquette", points: 1, growth: 1, hunger: 14, color: "#b47828", key: "1" },
  { name: "Pâtée", points: 3, growth: 3, hunger: 28, color: "#c3825a", key: "2" },
  { name: "Thon", points: 5, growth: 6, hunger: 45, color: "#78a0be", key: "3" },
  { name: "Festin", points: 10, growth: 12, hunger: 100, color: "#dcb446", key: "4" },
];

const PHRASES = [
  "Nahla te ignore.",
  "Nahla juge ton existence.",
  "Nahla exige plus de croquettes.",
  "Nahla te considère comme un serveur.",
  "Nahla pense que tu peux faire mieux.",
  "Nahla soupire de mépris.",
  "Nahla voulait du thon, pas ça.",
  "Nahla te regarde comme un meuble.",
  "Nahla approche du statut boule.",
  "Nahla devient une menace géométrique.",
];

const HUNGER_PHRASES = [
  "Nahla a FAIM.",
  "Nahla miaule de colère.",
  "Nahla te fixe avec haine — elle veut manger.",
  "Nahla commence à gratter le canapé.",
  "Nahla menace de te réveiller à 4h du mat.",
  "Nahla pense que tu l'a oubliée.",
  "Le ventre de Nahla fait un bruit de tonnerre.",
];

const NAHLA_CROP = { x: 0.18, y: 0.08, w: 0.64, h: 0.72 };
const CENTER_X = W / 2;
const CENTER_Y = H / 2 - 10;

const nahlaImg = new Image();
nahlaImg.src = "nahla_photo.jpg";
let nahlaReady = false;
nahlaImg.onload = () => {
  nahlaReady = true;
};

let state = freshState();
let foodRects = [];
let mouse = { x: 0, y: 0 };
let lastTime = 0;

function freshState() {
  return {
    score: 0,
    growthPoints: 0,
    hunger: HUNGER_MAX,
    selectedFood: 0,
    phrase: "Choisis une nourriture, puis clique sur Nahla.",
    popups: [],
    feedAnim: 0,
    hungerTimer: 0,
  };
}

function nahlaSize(growthPoints) {
  return NAHLA_BASE_SIZE + Math.floor(growthPoints / GROW_EVERY) * GROW_AMOUNT;
}

function nahlaLevel(growthPoints) {
  let title = LEVELS[0][1];
  for (const [threshold, name] of LEVELS) {
    if (growthPoints >= threshold) title = name;
  }
  return title;
}

function hungerColor(ratio) {
  if (ratio <= 0.3) return "#dc5046";
  if (ratio <= 0.6) return "#e6b432";
  return "#5ab45a";
}

function pickRandom(list) {
  return list[Math.floor(Math.random() * list.length)];
}

function foodButtonRects() {
  const gap = 12;
  const btnW = Math.floor((W - 80 - gap * (FOODS.length - 1)) / FOODS.length);
  const btnH = 72;
  const y = H - 108;
  const rects = [];
  let x = 40;
  for (let i = 0; i < FOODS.length; i++) {
    rects.push({ x, y, w: btnW, h: btnH });
    x += btnW + gap;
  }
  return rects;
}

function inRect(px, py, r) {
  return px >= r.x && px <= r.x + r.w && py >= r.y && py <= r.y + r.h;
}

function getNahlaDrawInfo() {
  const size = nahlaSize(state.growthPoints);
  const animScale = 1 + 0.2 * state.feedAnim;
  const yOffset = -14 * state.feedAnim;
  const maxSide = size * 2 * animScale;

  let dw = maxSide;
  let dh = maxSide;
  let sx = 0;
  let sy = 0;
  let sw = nahlaImg.naturalWidth || 1;
  let sh = nahlaImg.naturalHeight || 1;

  if (nahlaReady) {
    sx = sw * NAHLA_CROP.x;
    sy = sh * NAHLA_CROP.y;
    sw = sw * NAHLA_CROP.w;
    sh = sh * NAHLA_CROP.h;
    const scale = Math.min(maxSide / sw, maxSide / sh);
    dw = Math.max(1, sw * scale);
    dh = Math.max(1, sh * scale);
  }

  const x = CENTER_X - dw / 2;
  const y = CENTER_Y + yOffset - dh / 2;
  return { x, y, w: dw, h: dh, sx, sy, sw, sh, size };
}

function feedNahla(food, mx, my) {
  state.popups.push({
    x: mx,
    y: my,
    life: 700,
    text: `+${food.points}`,
    color: food.color,
  });
  state.score += food.points;
  state.growthPoints += food.growth;
  state.hunger = Math.min(HUNGER_MAX, state.hunger + food.hunger);
  state.feedAnim = 1;
  if (state.score % PHRASE_EVERY === 0) {
    state.phrase = pickRandom(PHRASES);
  }
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

function drawHungerBar() {
  const barX = 32;
  const barY = 132;
  const barW = 220;
  const barH = 18;
  const ratio = Math.max(0, Math.min(1, state.hunger / HUNGER_MAX));

  ctx.fillStyle = TEXT;
  ctx.font = "22px Arial, sans-serif";
  ctx.textAlign = "left";
  ctx.fillText("Faim", barX, barY - 6);

  roundRect(barX, barY, barW, barH, 9);
  ctx.fillStyle = COUCH_DARK;
  ctx.fill();
  if (ratio > 0) {
    roundRect(barX, barY, barW * ratio, barH, 9);
    ctx.fillStyle = hungerColor(ratio);
    ctx.fill();
  }
  roundRect(barX, barY, barW, barH, 9);
  ctx.strokeStyle = TORTIE_DARK;
  ctx.lineWidth = 2;
  ctx.stroke();
}

function drawResetButton(hovered) {
  const r = RESET_RECT;
  roundRect(r.x, r.y, r.w, r.h, 10);
  ctx.fillStyle = hovered ? "#967358" : "#785a46";
  ctx.fill();
  roundRect(r.x, r.y, r.w, r.h, 10);
  ctx.strokeStyle = TORTIE_DARK;
  ctx.lineWidth = 2;
  ctx.stroke();
  ctx.fillStyle = TEXT;
  ctx.font = "22px Arial, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText("Reset", r.x + r.w / 2, r.y + r.h / 2);
}

function drawFoodIcon(cx, cy, color) {
  ctx.beginPath();
  ctx.arc(cx, cy - 4, 14, 0, Math.PI * 2);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.strokeStyle = "#5a3c14";
  ctx.lineWidth = 2;
  ctx.stroke();
}

function drawFoodButtons() {
  roundRect(32, H - 120, W - 64, 96, 16);
  ctx.fillStyle = PANEL;
  ctx.fill();

  foodRects.forEach((rect, i) => {
    const food = FOODS[i];
    const selected = i === state.selectedFood;
    roundRect(rect.x, rect.y, rect.w, rect.h, 12);
    ctx.fillStyle = selected ? SELECTED : PANEL_LIGHT;
    ctx.fill();
    roundRect(rect.x, rect.y, rect.w, rect.h, 12);
    ctx.strokeStyle = TORTIE_DARK;
    ctx.lineWidth = 2;
    ctx.stroke();

    drawFoodIcon(rect.x + rect.w / 2, rect.y + rect.h / 2, food.color);

    ctx.fillStyle = TEXT;
    ctx.font = "22px Arial, sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "top";
    ctx.fillText(food.name, rect.x + rect.w / 2, rect.y + 8);

    ctx.fillStyle = MUTED;
    ctx.font = "22px Arial, sans-serif";
    ctx.textBaseline = "bottom";
    ctx.fillText(`+${food.points} | x${food.growth}`, rect.x + rect.w / 2, rect.y + rect.h - 8);

    ctx.fillStyle = TEXT;
    ctx.textAlign = "right";
    ctx.textBaseline = "top";
    ctx.fillText(String(i + 1), rect.x + rect.w - 10, rect.y + 6);
  });
}

function drawPopups() {
  state.popups.forEach((popup) => {
    const alpha = Math.min(1, popup.life / 700);
    ctx.globalAlpha = alpha;
    ctx.beginPath();
    ctx.arc(popup.x, popup.y, 10, 0, Math.PI * 2);
    ctx.fillStyle = popup.color;
    ctx.fill();
    ctx.fillStyle = ACCENT;
    ctx.font = "22px Arial, sans-serif";
    ctx.textAlign = "left";
    ctx.textBaseline = "middle";
    ctx.fillText(popup.text, popup.x + 14, popup.y - 10);
    ctx.globalAlpha = 1;
  });
}

function draw() {
  ctx.fillStyle = COUCH;
  ctx.fillRect(0, 0, W, H);

  const nahla = getNahlaDrawInfo();
  if (nahlaReady) {
    ctx.drawImage(nahlaImg, nahla.sx, nahla.sy, nahla.sw, nahla.sh, nahla.x, nahla.y, nahla.w, nahla.h);
  } else {
    roundRect(nahla.x, nahla.y, nahla.w, nahla.h, 20);
    ctx.fillStyle = ACCENT;
    ctx.fill();
  }

  if (inRect(mouse.x, mouse.y, nahla)) {
    roundRect(nahla.x - 12, nahla.y - 12, nahla.w + 24, nahla.h + 24, 12);
    ctx.strokeStyle = ACCENT;
    ctx.lineWidth = 3;
    ctx.stroke();
  }

  ctx.fillStyle = TEXT;
  ctx.font = "bold 42px Arial, sans-serif";
  ctx.textAlign = "left";
  ctx.textBaseline = "top";
  ctx.fillText(`Croquettes : ${state.score}`, 32, 24);

  ctx.fillStyle = ACCENT;
  ctx.font = "28px Arial, sans-serif";
  ctx.fillText(`Niveau : ${nahlaLevel(state.growthPoints)}`, 32, 72);

  ctx.fillStyle = MUTED;
  ctx.font = "22px Arial, sans-serif";
  ctx.fillText(`Croissance : ${state.growthPoints}`, 32, 104);

  drawHungerBar();
  drawResetButton(inRect(mouse.x, mouse.y, RESET_RECT));

  const selected = FOODS[state.selectedFood];
  ctx.fillStyle = MUTED;
  ctx.font = "22px Arial, sans-serif";
  ctx.fillText(
    `1-4 nourriture | Clic Nahla = ${selected.name} | R = reset`,
    280,
    132
  );

  ctx.fillStyle = TEXT;
  ctx.font = "28px Arial, sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(state.phrase, W / 2, H - 138);

  drawFoodButtons();
  drawPopups();
}

function handleClick(px, py) {
  if (inRect(px, py, RESET_RECT)) {
    state = freshState();
    return;
  }

  const foodIdx = foodRects.findIndex((r) => inRect(px, py, r));
  if (foodIdx >= 0) {
    state.selectedFood = foodIdx;
    return;
  }

  const nahla = getNahlaDrawInfo();
  if (inRect(px, py, nahla)) {
    feedNahla(FOODS[state.selectedFood], px, py);
  }
}

function canvasPos(evt) {
  const rect = canvas.getBoundingClientRect();
  const scaleX = W / rect.width;
  const scaleY = H / rect.height;
  const clientX = evt.clientX ?? evt.touches?.[0]?.clientX ?? 0;
  const clientY = evt.clientY ?? evt.touches?.[0]?.clientY ?? 0;
  return {
    x: (clientX - rect.left) * scaleX,
    y: (clientY - rect.top) * scaleY,
  };
}

function tick(now) {
  if (!lastTime) lastTime = now;
  const dt = Math.min(now - lastTime, 50);
  lastTime = now;

  state.hunger = Math.max(0, state.hunger - (HUNGER_DRAIN * dt) / 1000);
  state.feedAnim = Math.max(0, state.feedAnim - dt / BOUNCE_MS);

  if (state.hunger < HUNGER_LOW_THRESHOLD) {
    state.hungerTimer += dt;
    if (state.hungerTimer >= HUNGER_COMPLAIN_MS) {
      state.phrase = pickRandom(HUNGER_PHRASES);
      state.hungerTimer = 0;
    }
  } else {
    state.hungerTimer = 0;
  }

  state.popups = state.popups.filter((p) => {
    p.life -= dt;
    p.y -= dt * 0.05;
    return p.life > 0;
  });

  draw();
  requestAnimationFrame(tick);
}

canvas.addEventListener("mousemove", (evt) => {
  const pos = canvasPos(evt);
  mouse.x = pos.x;
  mouse.y = pos.y;
});

canvas.addEventListener("click", (evt) => {
  const pos = canvasPos(evt);
  handleClick(pos.x, pos.y);
});

canvas.addEventListener(
  "touchstart",
  (evt) => {
    evt.preventDefault();
    const pos = canvasPos(evt);
    mouse.x = pos.x;
    mouse.y = pos.y;
    handleClick(pos.x, pos.y);
  },
  { passive: false }
);

window.addEventListener("keydown", (evt) => {
  if (evt.key === "r" || evt.key === "R") {
    state = freshState();
    return;
  }
  const idx = FOODS.findIndex((f) => f.key === evt.key);
  if (idx >= 0) state.selectedFood = idx;
});

foodRects = foodButtonRects();
requestAnimationFrame(tick);
