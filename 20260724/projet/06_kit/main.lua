-- ============================================================
-- Exercice 6/6 — Kit joueur
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260724/projet/06_kit
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260724/projet/06_kit/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function creer(nom, armure)
    armure = armure or 0
    return { nom = nom, armure = armure }
end

function soigner(vie, soin)
    soin = soin or 20
    return math.min(100, vie + soin)
end