-- ============================================================
-- Exercice 4/6 — Compter et sommer
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260718/projet/04_compter
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260718/projet/04_compter/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function taille(liste)
    return #liste
end

function somme(nombres)
    total = 0
    for position, valeur in ipairs(nombres) do
        total = total + valeur
    end
    return total
end