-- ============================================================
-- Exercice 5/6 — Défaut + double return
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260724/projet/05_combo
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260724/projet/05_combo/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function stats(vie, armure)
    armure = armure or 0
    return vie, armure
end