-- ============================================================
-- GTA — plaque normalisée
-- ============================================================
-- Le système de police stocke les plaques en minuscules.
-- Transforme la plaque saisie.
--
-- Lance : lua 02_plaque.lua
-- ============================================================

brut = "LS-441"
plaque = string.lower(brut)

-- Transforme brut en minuscules → "ls-441"
--
-- Résultat attendu : plaque == "ls-441"
--
-- Indice : string.lower()

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(plaque == "ls-441", "Obtenu : '" .. tostring(plaque) .. "'")
print("✅ Correct !")
