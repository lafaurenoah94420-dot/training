-- ============================================================
-- Resident Evil — code d'accès
-- ============================================================
-- Le clavier enregistre les codes en minuscules.
-- Transforme le code saisi.
--
-- Lance : lua 02_code.lua
-- ============================================================

brut = "ALPHA-7"
code = string.lower(brut)

-- Transforme brut en minuscules → "alpha-7"
--
-- Résultat attendu : code == "alpha-7"
--
-- Indice : string.lower()

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(code == "alpha-7", "Obtenu : '" .. tostring(code) .. "'")
print("✅ Correct !")
