-- ============================================================
-- Hearts of Iron IV — total des stocks
-- ============================================================
-- Tu additionnes toutes les valeurs du dictionnaire stocks.
--
-- Lance : lua 05_total.lua
-- ============================================================

stocks = { chars = 20, avions = 15, bateaux = 10 }
total = 0

-- Parcours stocks avec pairs.
-- À chaque tour, ajoute la valeur v à total.
--
-- chars=20 → total 20
-- avions=15 → total 35
-- bateaux=10 → total 45
--
-- Résultat attendu : total == 45
--
-- Indice : for k, v in pairs(stocks) do
--          total = total + v

-- À toi :
for k, v in pairs(stocks) do
    total = total + v
end
-- --- Vérification (ne pas modifier) ---
assert(total == 45, "Obtenu : " .. tostring(total) .. ", attendu : 45")
print("✅ Correct !")
