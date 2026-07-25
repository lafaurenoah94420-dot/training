-- Exercice 1 — Calcul (GTA)
--
-- Tu as une arme avec une puissance de base, et un multiplicateur
-- selon le type de munition.
-- Calcule les dégâts totaux : puissance * multiplicateur.

local puissance = 40
local multiplicateur = 1.5

-- TODO : calcule les dégâts totaux
local degats = puissance * multiplicateur

-- --- Vérification ---
assert(degats == 60, "Attendu : 60, obtenu : " .. tostring(degats))
print("01_degats OK")
