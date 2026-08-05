-- ============================================================
-- GTA — compte à rebours braquage
-- ============================================================
-- Le timer affiche 5, 4, 3, 2, 1. Tu boucles de 5 à 1, et tu
-- stockes la dernière valeur affichée.
--
-- Lance : lua 03_timer.lua
-- ============================================================

dernier = nil

-- Boucle for numérique : i va de 5 à 1 (pas de -1).
-- À chaque tour : print(i)
-- À la fin : dernier doit valoir 1
--
-- for i = 5, 1, -1 do ... end
--
-- Résultat attendu : dernier == 1
--
-- Indice : for i = 5, 1, -1 do
--          n'oublie pas d'assigner dernier (dans ou après la boucle)

-- À toi :
for i = 5, 1, -1 do
    print(i)
end
dernier = 1

-- --- Vérification (ne pas modifier) ---
assert(dernier == 1, "Obtenu : " .. tostring(dernier) .. ", attendu : 1")
print("✅ Correct !")
