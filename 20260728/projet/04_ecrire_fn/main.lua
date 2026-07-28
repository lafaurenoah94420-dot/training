-- ============================================================
-- Exercice 4/6 — Fonction pour écrire
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260728/projet/04_ecrire_fn
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260728/projet/04_ecrire_fn/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function ecrire(chemin, texte)
    f = io.open(chemin, "w")
    f:write(texte)
    f:close()
end