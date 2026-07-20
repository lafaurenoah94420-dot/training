-- ============================================================
-- Exercice 6/6 — Badge joueur
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260720/projet/06_badge
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260720/projet/06_badge/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function badge(nom, niveau)
    nom = string.upper(nom)
    return "[" .. nom .. "] — niv." .. niveau
end