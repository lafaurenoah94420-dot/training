-- ============================================================
-- Exercice 6/6 — Kit de survie
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260717/projet/06_kit_survie
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260717/projet/06_kit_survie/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function soigner(vie, soin)
    total = vie + soin
    return math.min(total, 100)
end

function degats(vie, montant)
    total = vie - montant
    return math.max(total, 0)
end

function statut(vie)
    if vie < 30 then
        return "Critique"
    elseif vie >= 30 and vie < 70 then
        return "Blessé"
    else
        return "Stable"
    end
end