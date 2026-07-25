-- ============================================================
-- Exercice 5/6 — Tenter un soin en sécurité
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260725/projet/05_combo
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260725/projet/05_combo/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function appliquer_soin(vie, soin)
    if soin < 0 then
        error("soin invalide")
    else
        return vie + soin
    end
end

function soin_sur(vie, soin)
    local ok, res = pcall(appliquer_soin, vie, soin)
    if ok then
        return res
    else
        return vie
    end
end