-- ============================================================
-- GTA — compte à rebours
-- ============================================================
-- Le timer affiche 3, 2, 1. Tu boucles de 3 à 1, et tu stockes
-- la dernière valeur dans dernier.
--
-- Lance : lua 03_timer.lua
-- ============================================================

dernier = nil

-- Boucle for de 3 à 1 avec pas -1 :
--   print(i)
-- À la fin : dernier == 1
--
-- for i = 3, 1, -1 do ... end
--
-- Résultat attendu : dernier == 1
--
-- Indice : for i = 3, 1, -1 do
--          assigne dernier (dans ou après la boucle)

-- À toi :
for i = 3, 1, -1 do
    print(i)
end
dernier = 1
-- --- Vérification (ne pas modifier) ---
assert(dernier == 1, "Obtenu : " .. tostring(dernier) .. ", attendu : 1")
print("✅ Correct !")
