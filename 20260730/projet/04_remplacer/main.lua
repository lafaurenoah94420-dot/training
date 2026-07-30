-- ============================================================
-- Exercice 4/6 — Remplacer un mot
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260730/projet/04_remplacer
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260730/projet/04_remplacer/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function remplacer(texte)
    return string.gsub(texte, "zombie", "infecté")
end