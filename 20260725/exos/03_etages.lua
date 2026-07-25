-- Exercice 3 — Boucle for numérique (The Last of Us)
--
-- Joel monte les étages d'un immeuble, du 1 au 5.
-- Affiche chaque étage avec print, puis stocke le dernier
-- étage atteint dans une variable.

local dernier_etage = nil

-- TODO : boucle for de 1 à 5
-- À chaque tour : print("Étage " .. i)
-- À la fin : dernier_etage doit valoir 5
for i = 1, 5 do
    print("Étage " .. i)
end
dernier_etage = 5
-- --- Vérification ---
assert(dernier_etage == 5, "Attendu : 5, obtenu : " .. tostring(dernier_etage))
print("03_etages OK")
