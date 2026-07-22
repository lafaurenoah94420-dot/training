-- ============================================================
-- Exercice 4/6 — Fonction texte
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260722/projet/04_string_fn
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260722/projet/04_string_fn/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function nettoyer(texte)
    propre = string.gsub(texte, " ", "")
    return string.lower(propre)
end