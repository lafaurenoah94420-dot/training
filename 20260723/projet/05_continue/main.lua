-- ============================================================
-- Exercice 5/6 — Sauter des tours
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260723/projet/05_continue
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260723/projet/05_continue/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function somme_positifs(nombres)
    total = 0
    for i, x in ipairs(nombres) do
        if x > 0 then
            total = total + x
        end
    end
    return total
end