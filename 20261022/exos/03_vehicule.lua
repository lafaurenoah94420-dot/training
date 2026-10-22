-- ============================================================
-- GTA — fiche véhicule
-- ============================================================
-- Tu lis le modèle, puis tu mets la vitesse à 120.
--
-- Lance : lua 03_vehicule.lua
-- ============================================================

voiture = { modele = "sultan", vitesse = 80 }
modele_lu = voiture["modele"]
voiture["vitesse"] = 120

-- 1) modele_lu = la valeur de la clé "modele" → "sultan"
-- 2) mets voiture["vitesse"] à 120
--
-- Résultat attendu : modele_lu == "sultan"  et  voiture["vitesse"] == 120
--
-- Indice : voiture["modele"]  et  voiture["vitesse"] = ...

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(modele_lu == "sultan", "modele_lu devrait être 'sultan', obtenu : '" .. tostring(modele_lu) .. "'")
assert(voiture["vitesse"] == 120, "voiture['vitesse'] devrait être 120, obtenu : " .. tostring(voiture["vitesse"]))
print("✅ Correct !")
