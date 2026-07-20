-- ============================================================
-- The Last of Us — nom à l'écran
-- ============================================================
-- L'interface affiche le nom du survivant en minuscules pour
-- le journal de quête. Transforme le nom de Joel.
--
-- Lance : lua 01_string.lua
-- ============================================================

nom = "JOEL MILLER"
nom_affiche = string.lower(nom)

-- Transforme nom en minuscules et stocke le résultat dans nom_affiche.
--
-- "JOEL MILLER"  →  chaque lettre passe en minuscule  →  "joel miller"
--
-- Résultat attendu : nom_affiche == "joel miller"
--
-- Indice : string.lower()

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(nom_affiche == "joel miller", "Obtenu : '" .. nom_affiche .. "'")
print("✅ Correct !")
