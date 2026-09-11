-- ============================================================
-- The Last of Us — chargeur
-- ============================================================
-- Combien de balles reste-t-il dans le chargeur d'Ellie ?
-- Utilise # pour compter.
--
-- Lance : lua 02_chargeur.lua
-- ============================================================

chargeur = { "9mm", "9mm", "9mm", "9mm", "9mm", "9mm" }
nb_balles = #chargeur

-- Compte les éléments de chargeur.
--
-- Résultat attendu : nb_balles == 6
--
-- Indice : #chargeur

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(nb_balles == 6, "Obtenu : " .. tostring(nb_balles) .. ", attendu : 6")
print("✅ Correct !")
