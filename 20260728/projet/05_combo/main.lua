-- ============================================================
-- Exercice 5/6 — Copier un fichier
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260728/projet/05_combo
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260728/projet/05_combo/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function copier(source, destination)
    f = io.open(source, "r")
    resultat = f:read("*a")
    f:close()
    d = io.open(destination, "w")
    ecrire = d:write(resultat)
    d:close()
end