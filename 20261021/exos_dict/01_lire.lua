-- ============================================================
-- The Last of Us — fiche survivant
-- ============================================================
-- Tu lis le nom stocké dans la fiche de Joel.
--
-- Lance : lua 01_lire.lua
-- ============================================================

fiche = { nom = "Joel", age = 52 }
nom_lu = ""

-- nom_lu = la valeur de la clé "nom" dans fiche → "Joel"
--
-- Résultat attendu : nom_lu == "Joel"
--
-- Indice : fiche["nom"]

-- À toi :
nom_lu = fiche["nom"]

-- --- Vérification (ne pas modifier) ---
assert(nom_lu == "Joel", "Obtenu : '" .. tostring(nom_lu) .. "'")
print("✅ Correct !")
