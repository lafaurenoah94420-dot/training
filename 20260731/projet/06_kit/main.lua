-- ============================================================
-- Exercice 6/6 — Kit personnage
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260731/projet/06_kit
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260731/projet/06_kit/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function creer(nom, vie)
    return { nom = nom, vie = vie }
end

function soigner(perso, soin)
    perso.vie = perso.vie + soin
    if perso.vie > 100 then
        perso.vie = 100
    end
end