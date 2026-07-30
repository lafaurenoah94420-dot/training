-- ============================================================
-- Exercice 5/6 — Prendre le début
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260730/projet/05_tronquer
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260730/projet/05_tronquer/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function debut(texte, n)
    return string.sub(texte, 1, n)
end