-- ============================================================
-- Exercice 6/6 — Kit journal de bord
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260728/projet/06_kit
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260728/projet/06_kit/instructions.html
-- 🧪 Tester       : z
-- ============================================================
function lire(chemin)
    f = io.open(chemin, "r")
    local texte = f:read("*a")
    return texte
end

function ecrire(chemin, texte)
    f = io.open(chemin, "w")
    f:write(texte)
    f:close()
end

function ajouter(chemin, texte)
    f = io.open(chemin, "a")
    f:write(texte)
    f:close()
end