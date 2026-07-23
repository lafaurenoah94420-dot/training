-- ============================================================
-- The Last of Us — tag de quête
-- ============================================================
-- Le journal affiche les tags en minuscules. Transforme le tag.
--
-- Lance : lua 01_lower.lua
-- ============================================================

tag = "SURVIE"
affiche = ""

-- Transforme tag en minuscules et stocke le résultat dans affiche.
--
-- "SURVIE"  →  "survie"
--
-- Résultat attendu : affiche == "survie"
--
-- Indice : string.lower() — range le résultat

-- À toi :
affiche = string.lower(tag)

-- --- Vérification (ne pas modifier) ---
assert(affiche == "survie", "Obtenu : '" .. affiche .. "'")
print("✅ Correct !")
