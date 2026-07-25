-- ============================================================
-- Exercice 4/6 — Soigner ou planter
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260725/projet/04_retour
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260725/projet/04_retour/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function soigner(vie, soin)
    if soin < 0 then
        error("soin invalide")
    else
        return vie + soin
    end
end