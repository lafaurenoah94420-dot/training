-- ============================================================
-- Hearts of Iron IV — charges d'obus
-- ============================================================
-- L'artillerie a 4 charges. Chaque tir en consomme 1.
-- Tant qu'il reste des charges, tu tires.
--
-- Lance : lua 05_charges.lua
-- ============================================================

charges = 4
tirs = 0

-- Tant que charges > 0 :
--   tirs = tirs + 1
--   charges = charges - 1
--
-- tour 1 : charges 4 → tirs 1, charges 3
-- tour 2 : charges 3 → tirs 2, charges 2
-- tour 3 : charges 2 → tirs 3, charges 1
-- tour 4 : charges 1 → tirs 4, charges 0
-- arrêt : charges vaut 0
--
-- Résultat attendu : tirs == 4  et  charges == 0
--
-- Indice : while ... do ... end

-- À toi :
while charges > 0 do
    tirs = tirs + 1
    charges = charges - 1
end

-- --- Vérification (ne pas modifier) ---
assert(tirs == 4, "tirs devrait être 4, obtenu : " .. tostring(tirs))
assert(charges == 0, "charges devrait être 0, obtenu : " .. tostring(charges))
print("✅ Correct !")
