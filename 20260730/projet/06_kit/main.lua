-- ============================================================
-- Exercice 6/6 — Kit message
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260730/projet/06_kit
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260730/projet/06_kit/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function etiquette(nom, vie)
    texte = string.upper(nom) .. " a " .. vie .. " PV"
    return texte
end

function nettoyer(texte)
    return string.gsub(texte, "Zombie", "Infecté")
end