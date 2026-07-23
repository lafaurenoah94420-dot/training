-- ============================================================
-- Exercice 3/6 — Break
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260723/projet/03_break
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260723/projet/03_break/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function trouver(liste, cible)
    for i, x in ipairs(liste) do
        if x == cible then
            return i
        end
    end
    return 0
end