-- ============================================================
-- Exercice 6/6 — Inventaire complet
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260718/projet/06_inventaire
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260718/projet/06_inventaire/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function creer()
    return {}
end

function ajouter(sac, objet)
    table.insert(sac, objet)
end

function taille(sac)
    return #sac
end

function contient(sac, objet)
    for position, valeur in ipairs(sac) do
        if valeur == objet then
            return true
        end
    end
    return false
end