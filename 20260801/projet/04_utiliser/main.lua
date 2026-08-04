-- ============================================================
-- Exercice 4/6 — Utiliser deux retours
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260801/projet/04_utiliser
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260801/projet/04_utiliser/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================

function stats(vie, armure)
  return vie, armure
end

-- total = somme des deux retours de stats(30, 20)

vie, armure = stats(30, 20)
total = vie + armure