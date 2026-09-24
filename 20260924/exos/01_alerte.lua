-- ============================================================
-- The Last of Us — alerte camp
-- ============================================================
-- La radio annonce le camp et le nombre de places libres.
-- Tu construis le message exact.
--
-- Lance : lua 01_alerte.lua
-- ============================================================

camp = "Jackson"
places = 2
alerte = camp .. " : " ..  places .. " places"

-- alerte = camp + " : " + places + " places"
-- → "Jackson : 2 places"
--
-- Résultat attendu : alerte == "Jackson : 2 places"
--
-- Indice : opérateur ..

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(alerte == "Jackson : 2 places", "Obtenu : '" .. tostring(alerte) .. "'")
print("✅ Correct !")
