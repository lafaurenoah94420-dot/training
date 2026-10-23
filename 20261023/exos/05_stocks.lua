-- ============================================================
-- Hearts of Iron IV — stocks utiles
-- ============================================================
-- Tu additionnes seulement les valeurs > 10 dans stocks.
--
-- Lance : lua 05_stocks.lua
-- ============================================================

stocks = { chars = 25, avions = 8, bateaux = 18, trains = 5 }
total = 0

-- Parcours stocks avec pairs.
-- Si v > 10, total = total + v
--
-- chars=25  → oui → 25
-- avions=8  → non
-- bateaux=18 → oui → 43
-- trains=5  → non
--
-- Résultat attendu : total == 43
--
-- Indice : for k, v in pairs(stocks) do + if v > 10

-- À toi :
for k, v in pairs(stocks) do 
    if v > 10 then
        total = total + v
    end
end
-- --- Vérification (ne pas modifier) ---
assert(total == 43, "Obtenu : " .. tostring(total) .. ", attendu : 43")
print("✅ Correct !")
