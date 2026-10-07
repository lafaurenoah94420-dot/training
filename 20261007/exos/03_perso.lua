-- ============================================================
-- GTA — fiche perso
-- ============================================================
-- Tu lis le nom du perso, puis tu mets son niveau à 5.
--
-- Lance : lua 03_perso.lua
-- ============================================================

perso = { nom = "Franklin", niveau = 3 }
nom_lu = perso["nom"]
perso["niveau"] = 5
-- 1) nom_lu = la valeur de la clé "nom" dans perso → "Franklin"
-- 2) mets perso["niveau"] à 5
--
-- Résultat attendu : nom_lu == "Franklin"  et  perso["niveau"] == 5
--
-- Indice : perso["nom"]  et  perso["niveau"] = ...

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(nom_lu == "Franklin", "nom_lu devrait être 'Franklin', obtenu : '" .. tostring(nom_lu) .. "'")
assert(perso["niveau"] == 5, "perso['niveau'] devrait être 5, obtenu : " .. tostring(perso["niveau"]))
print("✅ Correct !")
