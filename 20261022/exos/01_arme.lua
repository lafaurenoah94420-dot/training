-- ============================================================
-- Resident Evil — fiche arme
-- ============================================================
-- Tu lis le nom de l'arme dans la fiche.
--
-- Lance : lua 01_arme.lua
-- ============================================================

arme = { nom = "matilda", balles = 15 }
nom_lu = arme["nom"]

-- nom_lu = la valeur de la clé "nom" → "matilda"
--
-- Résultat attendu : nom_lu == "matilda"
--
-- Indice : arme["nom"]

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(nom_lu == "matilda", "Obtenu : '" .. tostring(nom_lu) .. "'")
print("✅ Correct !")
