-- ============================================================
-- Exercice 3/6 — Remplacer du texte
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260720/projet/03_remplacer
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260720/projet/03_remplacer/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function censurer(phrase)
    return string.gsub(phrase, "secret", "******")
  end