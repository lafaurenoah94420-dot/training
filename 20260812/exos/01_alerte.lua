-- ============================================================
-- The Last of Us — alerte radio
-- ============================================================
-- La radio annonce le lieu et le nombre d'infectés repérés.
-- Tu construis le message exact.
--
-- Lance : lua 01_alerte.lua
-- ============================================================

lieu = "Jackson"
nb = 3
alerte = lieu .. " : " .. nb .. " infectés"

-- alerte = lieu + " : " + nb + " infectés"
-- → "Jackson : 3 infectés"
--
-- Résultat attendu : alerte == "Jackson : 3 infectés"
--
-- Indice : opérateur ..

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(alerte == "Jackson : 3 infectés", "Obtenu : '" .. tostring(alerte) .. "'")
print("✅ Correct !")
