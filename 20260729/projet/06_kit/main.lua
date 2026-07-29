-- ============================================================
-- Exercice 6/6 — Kit inventaire
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260729/projet/06_kit
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260729/projet/06_kit/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function creer()
    return {}
end

function ajouter(liste, objet)
    table.insert(liste, objet)
end

function compter(liste, objet)
    compteur = 0
    for i, x in ipairs(liste) do
        if x == objet then
            compteur = compteur + 1
        end
    end
    return compteur
end

function contient(liste, objet)
    for i, x in ipairs(liste) do
        if x == objet then
            return true
        end
    end
    return false
end