-- ============================================================
-- GTA — plaque normalisée
-- ============================================================
-- Le système stocke les plaques en minuscules.
-- Transforme la plaque saisie.
--
-- Lance : lua 02_plaque.lua
-- ============================================================

brut = "LS-902"
plaque = ""

-- Transforme brut en minuscules → "ls-902"
--
-- Résultat attendu : plaque == "ls-902"
--
-- Indice : string.lower()

-- À toi :
plaque = string.lower(brut)

-- --- Vérification (ne pas modifier) ---
assert(plaque == "ls-902", "Obtenu : '" .. tostring(plaque) .. "'")
print("✅ Correct !")
