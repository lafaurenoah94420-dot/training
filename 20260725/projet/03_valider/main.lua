-- ============================================================
-- Exercice 3/6 — Refuser une mauvaise entrée
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260725/projet/03_valider
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260725/projet/03_valider/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function charger(balles)
    if balles <= 0 then
        error("chargeur vide")
    else
        return balles
    end
end