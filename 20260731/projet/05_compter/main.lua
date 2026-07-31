-- ============================================================
-- Exercice 5/6 — Compter les clés
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260731/projet/05_compter
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260731/projet/05_compter/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function compter(fiche)
    compteur = 0
    for i, x in pairs(fiche) do
        compteur = compteur + 1
    end
    return compteur
end