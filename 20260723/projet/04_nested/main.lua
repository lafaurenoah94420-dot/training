-- ============================================================
-- Exercice 4/6 — Boucles imbriquées
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260723/projet/04_nested
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260723/projet/04_nested/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function grille(lignes, colonnes)
    total = 0
    for i = 1, lignes do
        for j = 1, colonnes do
            total = total + 1
        end
    end
    return total
end