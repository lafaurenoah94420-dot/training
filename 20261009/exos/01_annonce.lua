-- ============================================================
-- The Last of Us — annonce camp
-- ============================================================
-- La radio annonce le camp et le nombre de survivants.
-- Tu construis le message exact.
--
-- Lance : lua 01_annonce.lua
-- ============================================================

camp = "Jackson"
survivants = 12
annonce = ""

-- annonce = camp + " : " + survivants + " survivants"
-- → "Jackson : 12 survivants"
--
-- Résultat attendu : annonce == "Jackson : 12 survivants"
--
-- Indice : opérateur ..

-- À toi :
annonce = camp .. " : " .. survivants .." survivants"

-- --- Vérification (ne pas modifier) ---
assert(annonce == "Jackson : 12 survivants", "Obtenu : '" .. tostring(annonce) .. "'")
print("✅ Correct !")
