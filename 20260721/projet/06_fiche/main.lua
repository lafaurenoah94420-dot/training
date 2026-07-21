-- ============================================================
-- Exercice 6/6 — Fiche complète
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260721/projet/06_fiche
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260721/projet/06_fiche/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function creer(nom, vie)
    return {
        nom = nom,
        vie = vie,
    }
end

function get(fiche, cle)
    return fiche[cle]
end

function set(fiche, cle, valeur)
    fiche[cle] = valeur
end

function a_cle(fiche, cle)
    if fiche[cle] ~= nil then
        return true
    else
        return false
    end
end