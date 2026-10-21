-- ============================================================
-- GTA — fiche perso
-- ============================================================
-- Tu lis le job de Franklin, puis tu mets son niveau à 10.
--
-- Lance : lua 03_fiche.lua
-- ============================================================

perso = { job = "braqueur", niveau = 4 }
job_lu = perso["job"]
perso["niveau"] = 10
-- 1) job_lu = la valeur de la clé "job" → "braqueur"
-- 2) mets perso["niveau"] à 10
--
-- Résultat attendu : job_lu == "braqueur"  et  perso["niveau"] == 10
--
-- Indice : perso["job"]  et  perso["niveau"] = ...

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(job_lu == "braqueur", "job_lu devrait être 'braqueur', obtenu : '" .. tostring(job_lu) .. "'")
assert(perso["niveau"] == 10, "perso['niveau'] devrait être 10, obtenu : " .. tostring(perso["niveau"]))
print("✅ Correct !")
