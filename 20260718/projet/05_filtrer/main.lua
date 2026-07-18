-- ============================================================
-- Exercice 5/6 — Compter avec condition
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260718/projet/05_filtrer
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260718/projet/05_filtrer/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function compter_grands(valeurs, seuil)
    total = 0
    for position, x in ipairs(valeurs) do
        if x > seuil then
            total = total + 1
        end
    end
    return total
end