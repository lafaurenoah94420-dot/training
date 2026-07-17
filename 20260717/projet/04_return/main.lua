-- ============================================================
-- Exercice 4/6 — Return avec plafond
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260717/projet/04_return
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260717/projet/04_return/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function soigner(vie, soin)
    total = vie + soin
    return math.min(total, 100)
end