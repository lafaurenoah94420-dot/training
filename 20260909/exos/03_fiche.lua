-- ============================================================
-- The Last of Us — fiche de Joel
-- ============================================================
-- Les infos de Joel sont dans un dictionnaire. Tu lis son âge,
-- puis tu ajoutes la clé ville avec "Austin".
--
-- Lance : lua 03_fiche.lua
-- ============================================================

joel = { nom = "Joel", age = 52 }
age_joel = nil

-- 1) age_joel = l'âge dans joel
-- 2) joel.ville = "Austin"
--
-- Résultat attendu : age_joel == 52  et  joel.ville == "Austin"
--
-- Indice : joel.age   et   joel.ville = "..."

-- À toi :
age_joel = joel.age
joel.ville = "Austin"

-- --- Vérification (ne pas modifier) ---
assert(age_joel == 52, "age_joel devrait être 52")
assert(joel.ville == "Austin", "joel.ville devrait être Austin")
print("✅ Correct !")
