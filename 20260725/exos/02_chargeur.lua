-- Exercice 2 — Longueur d'une liste (Resident Evil)
--
-- Tu as un chargeur avec plusieurs balles.
-- Combien y en a-t-il ? Utilise # pour compter.

local chargeur = { "9mm", "9mm", "9mm", "9mm", "9mm", "9mm", "9mm" }

-- TODO : compte le nombre de balles
local nb_balles = #chargeur


-- --- Vérification ---
assert(nb_balles == 7, "Attendu : 7, obtenu : " .. tostring(nb_balles))
print("02_chargeur OK")
