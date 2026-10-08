-- ============================================================
-- Hearts of Iron IV — carburant
-- ============================================================
-- Le convoi a 4 unités de fuel. Chaque trajet en consomme 1.
-- Tant qu'il reste du fuel, tu avances d'un trajet.
--
-- Lance : lua 05_fuel.lua
-- ============================================================

fuel = 4
trajets = 0

-- Tant que fuel > 0 :
--   trajets = trajets + 1
--   fuel = fuel - 1
--
-- tour 1 : fuel 4 → trajets 1, fuel 3
-- tour 2 : fuel 3 → trajets 2, fuel 2
-- tour 3 : fuel 2 → trajets 3, fuel 1
-- tour 4 : fuel 1 → trajets 4, fuel 0
-- arrêt : fuel vaut 0
--
-- Résultat attendu : trajets == 4  et  fuel == 0
--
-- Indice : while ... do ... end

-- À toi :
while fuel > 0 do
    trajets = trajets + 1
    fuel = fuel - 1
end

-- --- Vérification (ne pas modifier) ---
assert(trajets == 4, "trajets devrait être 4, obtenu : " .. tostring(trajets))
assert(fuel == 0, "fuel devrait être 0, obtenu : " .. tostring(fuel))
print("✅ Correct !")
