-- ============================================================
-- Exercice 5/6 — Math + texte
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260722/projet/05_combo
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260722/projet/05_combo/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function barre(actuel, max)
    calcul = math.floor(actuel / max * 100)
    return calcul .. "%"
end