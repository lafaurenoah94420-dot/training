-- ============================================================
-- Exercice 5/6 — Deux fonctions
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260717/projet/05_combinaison
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260717/projet/05_combinaison/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function degats(vie, montant)
    total = vie - montant
    return math.max(total, 0)
end

function est_vivant(vie)
    if vie > 0 then
        return true
    else
        return false
    end
end