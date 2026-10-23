-- ============================================================
-- GTA — fiche mission
-- ============================================================
-- Tu lis le nom de la mission, puis tu mets le statut à "finie".
--
-- Lance : lua 03_mission.lua
-- ============================================================

mission = { nom = "fleeca", statut = "en cours" }
nom_lu = "fleeca"
mission["statut"] = "finie"

-- 1) nom_lu = la valeur de la clé "nom" → "fleeca"
-- 2) mets mission["statut"] à "finie"
--
-- Résultat attendu : nom_lu == "fleeca"  et  mission["statut"] == "finie"
--
-- Indice : mission["nom"]  et  mission["statut"] = ...

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(nom_lu == "fleeca", "nom_lu devrait être 'fleeca', obtenu : '" .. tostring(nom_lu) .. "'")
assert(mission["statut"] == "finie", "mission['statut'] devrait être 'finie', obtenu : '" .. tostring(mission["statut"]) .. "'")
print("✅ Correct !")
