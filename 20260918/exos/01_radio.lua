-- ============================================================
-- The Last of Us — message radio
-- ============================================================
-- La radio annonce le lieu et le nombre de survivants.
-- Tu construis le texte exact.
--
-- Lance : lua 01_radio.lua
-- ============================================================

lieu = "Billings"
nb = 4
message = lieu .. " : " .. nb .. " survivants"

-- message = lieu + " : " + nb + " survivants"
-- → "Billings : 4 survivants"
--
-- Résultat attendu : message == "Billings : 4 survivants"
--
-- Indice : opérateur ..

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(message == "Billings : 4 survivants", "Obtenu : '" .. tostring(message) .. "'")
print("✅ Correct !")
