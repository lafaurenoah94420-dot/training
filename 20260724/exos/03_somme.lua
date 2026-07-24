-- ============================================================
-- GTA — pourboires de mission
-- ============================================================
-- Franklin a reçu plusieurs pourboires. Calcule le total.
--
-- Lance : lua 03_somme.lua
-- ============================================================

tips = {50, 20, 100, 30}
total = 0

-- Parcours tips et additionne chaque valeur dans total.
--
-- 50 + 20 + 100 + 30 = 200
--
-- Résultat attendu : total == 200
--
-- Indice : for _, x in ipairs(tips) do  +  total = total + x

-- À toi :
for i, x in ipairs(tips) do
    total = total + x
end

-- --- Vérification (ne pas modifier) ---
assert(total == 200, "Obtenu : " .. total .. ", attendu : 200")
print("✅ Correct !")
