-- ============================================================
-- Exercice 5/6 — Défaut + deux retours
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260801/projet/05_combo
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260801/projet/05_combo/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function kit(vie, soin)
    soin = soin or 20
    return vie, soin
end