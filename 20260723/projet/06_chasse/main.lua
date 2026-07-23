-- ============================================================
-- Exercice 6/6 — Boucle de chasse
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260723/projet/06_chasse
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260723/projet/06_chasse/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function chasse(vie, degats)
    coups = 0
    while vie > 0 do
        vie = vie - degats
        coups = coups + 1
    end
    return coups
end