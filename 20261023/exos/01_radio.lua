-- ============================================================
-- The Last of Us — fréquence radio
-- ============================================================
-- Tu lis la fréquence stockée dans la radio.
--
-- Lance : lua 01_radio.lua
-- ============================================================

radio = { frequence = "92.1", volume = 5 }
freq = radio["frequence"]

-- freq = la valeur de la clé "frequence" → "92.1"
--
-- Résultat attendu : freq == "92.1"
--
-- Indice : radio["frequence"]

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(freq == "92.1", "Obtenu : '" .. tostring(freq) .. "'")
print("✅ Correct !")
