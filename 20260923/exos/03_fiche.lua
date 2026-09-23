-- ============================================================
-- The Last of Us — fiche de Joel
-- ============================================================
-- Les infos de Joel sont dans un dictionnaire. Tu lis son âge,
-- puis tu ajoutes la clé ville avec "Texas".
--
-- Lance : lua 03_fiche.lua
-- ============================================================

joel = { nom = "Joel", age = 52 }
age_joel = joel.age
joel.ville = "Texas"
-- 1) age_joel = l'âge dans joel
-- 2) joel.ville = "Texas"
--
-- Résultat attendu : age_joel == 52  et  joel.ville == "Texas"
--
-- Indice : joel.age   et   joel.ville = "..."

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(age_joel == 52, "age_joel devrait être 52")
assert(joel.ville == "Texas", "joel.ville devrait être Texas")
print("✅ Correct !")
