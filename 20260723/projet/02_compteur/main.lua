-- ============================================================
-- Exercice 2/6 — While dans une fonction
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260723/projet/02_compteur
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260723/projet/02_compteur/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function remplir(depart, plafond, pas)
    while depart < plafond do
        depart = depart + pas
    end
    return depart
end