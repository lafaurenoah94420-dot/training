-- ============================================================
-- Exercice 2/6 — Défaut dans une fonction
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260724/projet/02_defaut_fn
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260724/projet/02_defaut_fn/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function soigner(vie, soin)
    soin = soin or 20
    return vie + soin
end