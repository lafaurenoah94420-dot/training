-- ============================================================
-- Exercice 6/6 — Kit manoir
-- ============================================================
-- 📁 Dossier      : cd /Users/noah/Desktop/Lua/20260725/projet/06_kit
-- 📄 Instructions : open /Users/noah/Desktop/Lua/20260725/projet/06_kit/instructions.html
-- 🧪 Tester       : lua tester.lua
-- ============================================================
function verrou(code)
    if code == 314 then
        return true
    else
        error("mauvais code")
    end
end

function entrer(code)
    local ok, res = pcall(verrou, code)
    if ok then
        return "entree"
    else
        return "bloque"
    end
end

function dose(infection, antidote)
    if antidote <= 0 then
        error("antidote vide")
    end
    local reste = infection - antidote
    if reste < 0 then
        return 0
    else
        return reste
    end
end