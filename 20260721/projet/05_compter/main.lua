-- ============================================================
-- Exercice 5/6 — Parcourir avec pairs
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260721/projet/05_compter
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260721/projet/05_compter/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function somme_valeurs(stats)
    total = 0
    for i, x in pairs(stats) do
        total = total + x
    end
    return total
end

function nombre_cles(stats)
    n = 0
    for i, x in pairs(stats) do
        n = n + 1
    end
    return n
end

