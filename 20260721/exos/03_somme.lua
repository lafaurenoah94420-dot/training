-- ============================================================
-- The Last of Us — munitions ramassées
-- ============================================================
-- Joel fouille plusieurs cadavres. Chaque valeur est un nombre
-- de balles trouvées. Calcule le total.
--
-- Lance : lua 03_somme.lua
-- ============================================================

balles = {4, 12, 3, 8}
total = 0

-- Parcours balles et additionne chaque valeur dans total.
--
-- tour 1 : x = 4   →  total = 0 + 4  = 4
-- tour 2 : x = 12  →  total = 4 + 12 = 16
-- tour 3 : x = 3   →  total = 16 + 3 = 19
-- tour 4 : x = 8   →  total = 19 + 8 = 27
--
-- Résultat attendu : total == 27
--
-- Indice : for _, x in ipairs(...) do ... end
--          et total = total + x

-- À toi :
for i, x in ipairs(balles) do
    total = total + x
end

-- --- Vérification (ne pas modifier) ---
assert(total == 27, "Obtenu : " .. total .. ", attendu : 27")
print("✅ Correct !")
