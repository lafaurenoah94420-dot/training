-- ============================================================
-- Exercice 4/6 — Récupérer deux valeurs
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260724/projet/04_unpack
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260724/projet/04_unpack/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function ecart(a, b)
    mn, mx = math.min(a, b), math.max(a, b)
    return mx - mn
end