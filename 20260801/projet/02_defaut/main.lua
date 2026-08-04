-- ============================================================
-- Exercice 2/6 — Défaut dans une fonction
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260801/projet/02_defaut
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260801/projet/02_defaut/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function soigner(vie, soin)
    soin = soin or 20
    return vie + soin
end