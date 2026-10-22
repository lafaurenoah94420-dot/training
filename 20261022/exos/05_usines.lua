-- ============================================================
-- Hearts of Iron IV — usines actives
-- ============================================================
-- Tu comptes combien de valeurs dans usines sont > 5.
--
-- Lance : lua 05_usines.lua
-- ============================================================

usines = { chars = 8, avions = 3, bateaux = 12, trains = 2 }
actives = 0

-- Parcours usines avec pairs.
-- Si v > 5, actives = actives + 1
--
-- chars=8  → oui → 1
-- avions=3 → non
-- bateaux=12 → oui → 2
-- trains=2 → non
--
-- Résultat attendu : actives == 2
--
-- Indice : for k, v in pairs(usines) do + if v > 5

-- À toi :
for k, v in pairs(usines) do
    if v > 5 then
        actives = actives + 1
    end
end
-- --- Vérification (ne pas modifier) ---
assert(actives == 2, "Obtenu : " .. tostring(actives) .. ", attendu : 2")
print("✅ Correct !")
