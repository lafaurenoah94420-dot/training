-- ============================================================
-- Exercice 4/6 — Sommer une liste
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260729/projet/04_somme
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260729/projet/04_somme/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function total(liste)
    local somme = 0
    for i, x in ipairs(liste) do
        somme = somme + x
end
return somme
end