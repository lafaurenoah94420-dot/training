-- ============================================================
-- The Last of Us — fiche d'Ellie
-- ============================================================
-- Les stats d'Ellie sont dans un dictionnaire. Tu lis son âge,
-- puis tu ajoutes la clé arme avec "revolver".
--
-- Lance : lua 03_fiche.lua
-- ============================================================

ellie = { nom = "Ellie", age = 14 }
age_ellie = ellie.age
ellie.arme = "revolver"

-- 1) age_ellie = l'âge dans ellie
-- 2) ellie.arme = "revolver"
--
-- Résultat attendu : age_ellie == 14  et  ellie.arme == "revolver"
--
-- Indice : ellie.age   et   ellie.arme = "..."

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(age_ellie == 14, "age_ellie devrait être 14")
assert(ellie.arme == "revolver", "ellie.arme devrait être revolver")
print("✅ Correct !")
