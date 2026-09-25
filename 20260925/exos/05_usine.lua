-- ============================================================
-- Hearts of Iron IV — usine
-- ============================================================
-- L'usine a 3 créneaux libres. Chaque tour, elle produit 1 char
-- et consomme 1 créneau.
--
-- Lance : lua 05_usine.lua
-- ============================================================

creneaux = 3
chars = 0

-- Tant que creneaux > 0 :
--   chars = chars + 1
--   creneaux = creneaux - 1
--
-- tour 1 : creneaux 3 → chars 1, creneaux 2
-- tour 2 : creneaux 2 → chars 2, creneaux 1
-- tour 3 : creneaux 1 → chars 3, creneaux 0
-- arrêt : creneaux vaut 0
--
-- Résultat attendu : chars == 3  et  creneaux == 0
--
-- Indice : while ... do ... end

-- À toi :
while creneaux > 0 do
    chars = chars + 1
    creneaux = creneaux - 1
end

-- --- Vérification (ne pas modifier) ---
assert(chars == 3, "chars devrait être 3, obtenu : " .. tostring(chars))
assert(creneaux == 0, "creneaux devrait être 0, obtenu : " .. tostring(creneaux))
print("✅ Correct !")
