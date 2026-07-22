-- ============================================================
-- Exercice 6/6 — Kit de combat
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260722/projet/06_kit
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260722/projet/06_kit/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function soigner(vie, soin)
    return math.min(100, vie + soin)
end

function degats(vie, montant)
    return math.max(0, vie - montant)
end

function critique(min, max)
    return math.random(min, max)
end