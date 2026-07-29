-- ============================================================
-- Exercice 5/6 — Filtrer les gros
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260729/projet/05_filtrer
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260729/projet/05_filtrer/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function filtrer_gros(liste)
    local resultat = {}
    for i, x in ipairs(liste) do
        if x > 5 then
            table.insert(resultat, x)
        end
    end
    return resultat
end