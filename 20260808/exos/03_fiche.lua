-- ============================================================
-- The Last of Us — fiche joueur
-- ============================================================
-- Les stats d'Ellie sont dans un dictionnaire. Tu lis son âge,
-- puis tu ajoutes la clé arme avec la valeur "arc".
--
-- Lance : lua 03_fiche.lua
-- ============================================================

ellie = { nom = "Ellie", age = 14 }
age_ellie = ellie.age
ellie.arme = "arc"
-- 1) age_ellie = l'âge dans ellie
-- 2) ajoute ellie.arme = "arc"
--
-- Résultat attendu : age_ellie == 14  et  ellie.arme == "arc"
--
-- Indice : ellie.age   et   ellie.arme = "..."

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(age_ellie == 14, "age_ellie devrait être 14")
assert(ellie.arme == "arc", "ellie.arme devrait être arc")
print("✅ Correct !")
