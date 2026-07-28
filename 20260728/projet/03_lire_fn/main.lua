-- ============================================================
-- Exercice 3/6 — Fonction pour lire
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260728/projet/03_lire_fn
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260728/projet/03_lire_fn/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function lire(chemin)
    f = io.open(chemin, "r")
    local texte = f:read("*a")
    f:close()
    return texte
end