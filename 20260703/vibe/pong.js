const canvas = document.getElementById("pong-canvas");
const ctx = canvas.getContext("2d");

const W = canvas.width;
const H = canvas.height;
const WIN = 7;

const DIFFS = {
  facile: {
    label: "Facile",
    oppSpeed: 3.5, oppMiss: 0.22, oppSlop: 18,
    malikSpeed: 1.4, malikW: 58, malikH: 30,
    baseSpeed: 4.5, maxSpeed: 9, gain: 0.25,
    color: "#5ab45a",
  },
  normal: {
    label: "Normal",
    oppSpeed: 6, oppMiss: 0.08, oppSlop: 8,
    malikSpeed: 2.2, malikW: 72, malikH: 36,
    baseSpeed: 5.5, maxSpeed: 11, gain: 0.35,
    color: "#ffd250",
  },
  enfer: {
    label: "Enfer",
    oppSpeed: 8.5, oppMiss: 0.02, oppSlop: 3,
    malikSpeed: 4.2, malikW: 96, malikH: 46,
    baseSpeed: 6.8, maxSpeed: 14, gain: 0.5,
    color: "#dc5046",
  },
};
const DIFF_KEYS = ["facile", "normal", "enfer"];

const WIN_PHRASES = ["Nahla accepte ce point.", "La croquette obéit.", "Tu sers bien."];
const LOSE_PHRASES = ["Nahla te juge.", "Pathétique.", "L'aspirateur gagne."];

const nahlaImg = new Image();
nahlaImg.src = "nahla_head.png";

let state = "menu";
let menuIdx = 1;
let diffKey = "normal";
let diff = DIFFS.normal;
let g = {};
let keys = {};
let last = 0;

function resetBall(down = false) {
  const a = (Math.random() - 0.5) * 1.2;
  const s = diff.baseSpeed;
  return { x: W / 2, y: H / 2, vx: Math.sin(a) * s, vy: (down ? 1 : -1) * s, speed: s };
}

function newGame() {
  const mw = diff.malikW, mh = diff.malikH;
  return {
    player: { x: W / 2 - 54, y: H - 78, w: 108, h: 60 },
    opp: { x: W / 2 - 65, y: 48, w: 130, h: 22 },
    malik: { x: W / 2 - mw / 2, y: H / 2 - mh / 2, w: mw, h: mh, dir: Math.random() > 0.5 ? 1 : -1 },
    ball: resetBall(),
    sp: 0, so: 0, rally: 0, serve: 900,
    phrase: "", phraseT: 0, parts: [], shake: 0,
  };
}

function bounce(ball, pad, down) {
  const rel = Math.max(-1, Math.min(1, (ball.x - (pad.x + pad.w / 2)) / (pad.w / 2)));
  ball.speed = Math.min(diff.maxSpeed, ball.speed + diff.gain);
  const ang = rel * 0.75;
  ball.vx = Math.sin(ang) * ball.speed;
  ball.vy = (down ? 1 : -1) * Math.cos(ang) * ball.speed;
  if (Math.abs(ball.vy) < 2) ball.vy = down ? 2 : -2;
}

function spawnParts(x, y, color, n = 8) {
  for (let i = 0; i < n; i++) {
    const a = Math.random() * Math.PI * 2;
    const s = 1.5 + Math.random() * 3;
    g.parts.push({ x, y, vx: Math.cos(a) * s, vy: Math.sin(a) * s, life: 200 + Math.random() * 250, color, r: 3 + Math.random() * 3 });
  }
}

function drawMenu() {
  ctx.fillStyle = "#c4a884";
  ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = "#372818";
  ctx.font = "bold 42px Arial";
  ctx.textAlign = "center";
  ctx.fillText("Nahla Pong", W / 2, 100);
  ctx.font = "22px Arial";
  ctx.fillStyle = "#6e5a46";
  ctx.fillText("Choisis la difficulté", W / 2, 140);

  DIFF_KEYS.forEach((k, i) => {
    const d = DIFFS[k];
    const y = 200 + i * 110;
    const sel = i === menuIdx;
    ctx.fillStyle = sel ? "#d2bc9e" : "#b49676";
    roundRect(W / 2 - 220, y, 440, 88, 14);
    ctx.fill();
    ctx.strokeStyle = sel ? d.color : "#3a2a24";
    ctx.lineWidth = 3;
    roundRect(W / 2 - 220, y, 440, 88, 14);
    ctx.stroke();
    ctx.fillStyle = "#372818";
    ctx.font = "bold 24px Arial";
    ctx.textAlign = "left";
    ctx.fillText(`${i + 1}. ${d.label}`, W / 2 - 190, y + 38);
    ctx.font = "18px Arial";
    ctx.fillStyle = "#6e5a46";
    ctx.fillText(k === "facile" ? "Aspirateur lent · Malik tranquille" : k === "enfer" ? "Aspirateur rapide · Malik en furie" : "Équilibré", W / 2 - 190, y + 68);
  });
  ctx.textAlign = "center";
  ctx.font = "18px Arial";
  ctx.fillStyle = "#6e5a46";
  ctx.fillText("1/2/3 ou flèches + Entrée", W / 2, H - 40);
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

function drawGame() {
  const sx = g.shake > 0 ? (Math.random() * 8 - 4) : 0;
  const sy = g.shake > 0 ? (Math.random() * 6 - 3) : 0;

  ctx.fillStyle = "#c4a884";
  ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = "#d2bc9e";
  roundRect(40 + sx, 80 + sy, W - 80, H - 160, 20);
  ctx.fill();
  ctx.strokeStyle = "#a88e6c";
  ctx.lineWidth = 3;
  roundRect(40 + sx, 80 + sy, W - 80, H - 160, 20);
  ctx.stroke();

  for (let x = 0; x < W; x += 24) {
    ctx.fillStyle = "#a88e6c";
    ctx.fillRect(x + sx, H / 2 + sy - 2, 12, 4);
  }

  // Malik
  const m = g.malik;
  ctx.fillStyle = "#ffb464";
  roundRect(m.x + sx, m.y + sy, m.w, m.h, 10);
  ctx.fill();
  ctx.fillStyle = "#372818";
  ctx.font = "16px Arial";
  ctx.textAlign = "center";
  ctx.fillText("Malik", m.x + m.w / 2 + sx, m.y + m.h / 2 + sy + 6);

  // Aspirateur
  ctx.fillStyle = "#5a82aa";
  roundRect(g.opp.x + sx, g.opp.y + sy, g.opp.w, g.opp.h, 10);
  ctx.fill();
  ctx.fillStyle = "#f0f5fa";
  ctx.font = "14px Arial";
  ctx.fillText("Aspirateur", g.opp.x + g.opp.w / 2 + sx, g.opp.y + g.opp.h / 2 + sy + 5);

  // Nahla
  if (nahlaImg.complete) ctx.drawImage(nahlaImg, g.player.x + sx, g.player.y + sy, g.player.w, g.player.h);
  else { ctx.fillStyle = "#ffd250"; roundRect(g.player.x + sx, g.player.y + sy, g.player.w, g.player.h, 12); ctx.fill(); }

  if (g.serve <= 0) {
    const b = g.ball;
    ctx.fillStyle = "#dcb446";
    ctx.beginPath();
    ctx.arc(b.x + sx, b.y + sy, 13, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = "#5a3c14";
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  g.parts.forEach((p) => {
    ctx.globalAlpha = Math.min(1, p.life / 400);
    ctx.fillStyle = p.color;
    ctx.beginPath();
    ctx.arc(p.x + sx, p.y + sy, p.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.globalAlpha = 1;
  });

  ctx.fillStyle = "#372818";
  ctx.font = "bold 36px Arial";
  ctx.textAlign = "center";
  ctx.fillText(`${g.sp}  —  ${g.so}`, W / 2 + sx, 36);
  ctx.font = "18px Arial";
  ctx.fillStyle = diff.color;
  ctx.fillText(diff.label, W / 2 + sx, 62);
  ctx.fillStyle = "#6e5a46";
  ctx.textAlign = "left";
  ctx.fillText(`Échanges : ${g.rally}`, 24 + sx, 24);
  ctx.textAlign = "right";
  ctx.fillText(`Premier à ${WIN}`, W - 24 + sx, 24);

  if (g.phraseT > 0) {
    ctx.textAlign = "center";
    ctx.fillStyle = "#372818";
    ctx.font = "22px Arial";
    ctx.fillText(g.phrase, W / 2 + sx, H - 52);
  }
  if (g.serve > 0 && state === "play") {
    ctx.font = "28px Arial";
    ctx.fillStyle = "#6e5a46";
    ctx.fillText("...", W / 2 + sx, H / 2 + sy);
  }

  if (state === "win" || state === "lose") {
    ctx.fillStyle = "rgba(0,0,0,0.55)";
    ctx.fillRect(0, 0, W, H);
    ctx.textAlign = "center";
    ctx.font = "bold 40px Arial";
    ctx.fillStyle = state === "win" ? "#5ab45a" : "#dc5046";
    ctx.fillText(state === "win" ? "Nahla gagne." : "Nahla te méprise.", W / 2, H / 2 - 20);
    ctx.font = "22px Arial";
    ctx.fillStyle = "#ffd250";
    ctx.fillText(state === "win" ? "La croquette te respecte." : "Honte.", W / 2, H / 2 + 20);
    ctx.font = "18px Arial";
    ctx.fillStyle = "#ddd";
    ctx.fillText("R = rejouer · M = menu", W / 2, H / 2 + 60);
  }
}

function update(dt) {
  if (state !== "play") return;

  const spd = 9;
  if (keys.left) g.player.x -= spd;
  if (keys.right) g.player.x += spd;
  g.player.x = Math.max(16, Math.min(W - g.player.w - 16, g.player.x));

  const target = g.ball.x - g.opp.w / 2;
  if (Math.random() > diff.oppMiss) {
    if (g.opp.x < target - diff.oppSlop) g.opp.x += diff.oppSpeed;
    else if (g.opp.x > target + diff.oppSlop) g.opp.x -= diff.oppSpeed;
  }
  g.opp.x = Math.max(16, Math.min(W - g.opp.w - 16, g.opp.x));

  g.malik.x += g.malik.dir * diff.malikSpeed;
  if (g.malik.x <= 60 || g.malik.x + g.malik.w >= W - 60) g.malik.dir *= -1;

  if (g.serve > 0) { g.serve -= dt; return; }

  const b = g.ball;
  b.x += b.vx; b.y += b.vy;
  const r = 13;

  if (b.x - r <= 0 || b.x + r >= W) { b.vx *= -1; b.x = Math.max(r, Math.min(W - r, b.x)); spawnParts(b.x, b.y, "#a88e6c", 4); }

  if (b.y - r < g.opp.y + g.opp.h && b.y > g.opp.y && b.x > g.opp.x && b.x < g.opp.x + g.opp.w && b.vy < 0) {
    bounce(b, g.opp, true); b.y = g.opp.y + g.opp.h + r + 1; g.rally++; spawnParts(b.x, b.y, "#5a82aa", 8);
  }
  if (b.y + r > g.player.y && b.y < g.player.y + g.player.h && b.x > g.player.x && b.x < g.player.x + g.player.w && b.vy > 0) {
    bounce(b, g.player, false); b.y = g.player.y - r - 1; g.rally++; spawnParts(b.x, b.y, "#ffd250", 10);
  }
  const m = g.malik;
  if (b.x + r > m.x && b.x - r < m.x + m.w && b.y + r > m.y && b.y - r < m.y + m.h) {
    b.vx = b.vx > 0 ? -Math.abs(b.vx) : Math.abs(b.vx);
    b.speed = Math.min(diff.maxSpeed, b.speed + 0.5);
    spawnParts(b.x, b.y, "#ffb464", 12);
    g.phrase = "Malik !!"; g.phraseT = 1200;
  }

  if (b.y < -r) {
    g.sp++; g.phrase = WIN_PHRASES[Math.floor(Math.random() * WIN_PHRASES.length)]; g.phraseT = 1800;
    g.ball = resetBall(); g.serve = 900; g.rally = 0;
    if (g.sp >= WIN) state = "win";
  } else if (b.y > H + r) {
    g.so++; g.phrase = LOSE_PHRASES[Math.floor(Math.random() * LOSE_PHRASES.length)]; g.phraseT = 1800;
    g.ball = resetBall(true); g.serve = 900; g.rally = 0; g.shake = 280;
    if (g.so >= WIN) state = "lose";
  }

  g.parts.forEach((p) => { p.x += p.vx; p.y += p.vy; p.life -= dt; });
  g.parts = g.parts.filter((p) => p.life > 0);
  g.phraseT = Math.max(0, g.phraseT - dt);
  g.shake = Math.max(0, g.shake - dt);
}

function loop(now) {
  const dt = Math.min(now - last, 50);
  last = now;
  if (state === "menu") drawMenu();
  else { update(dt); drawGame(); }
  requestAnimationFrame(loop);
}

document.addEventListener("keydown", (e) => {
  if (["ArrowLeft", "ArrowRight", "q", "Q", "d", "D", "a", "A"].includes(e.key)) e.preventDefault();
  if (e.key === "ArrowLeft" || e.key === "q" || e.key === "Q" || e.key === "a" || e.key === "A") keys.left = true;
  if (e.key === "ArrowRight" || e.key === "d" || e.key === "D") keys.right = true;

  if (state === "menu") {
    if (e.key === "ArrowUp" || e.key === "w") menuIdx = (menuIdx + 2) % 3;
    if (e.key === "ArrowDown" || e.key === "s") menuIdx = (menuIdx + 1) % 3;
    if (e.key === "1") menuIdx = 0;
    if (e.key === "2") menuIdx = 1;
    if (e.key === "3") menuIdx = 2;
    if (e.key === "Enter" || e.key === " ") {
      diffKey = DIFF_KEYS[menuIdx];
      diff = DIFFS[diffKey];
      g = newGame();
      state = "play";
    }
  } else if (e.key === "r" && (state === "win" || state === "lose")) { g = newGame(); state = "play"; }
  else if (e.key === "m") state = "menu";
});

document.addEventListener("keyup", (e) => {
  if (e.key === "ArrowLeft" || e.key === "q" || e.key === "Q" || e.key === "a" || e.key === "A") keys.left = false;
  if (e.key === "ArrowRight" || e.key === "d" || e.key === "D") keys.right = false;
});

canvas.addEventListener("touchmove", (e) => {
  e.preventDefault();
  const rect = canvas.getBoundingClientRect();
  const x = (e.touches[0].clientX - rect.left) * (W / rect.width);
  g.player.x = Math.max(16, Math.min(W - g.player.w - 16, x - g.player.w / 2));
}, { passive: false });

requestAnimationFrame(loop);
