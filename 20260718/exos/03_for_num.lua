-- ============================================================
-- Resident Evil — salles du commissariat
-- ============================================================
-- Leon explore les salles numérotées de 1 à 5. Le jeu compte
-- combien de salles il a traversées.
--
-- Lance : lua 03_for_num.lua
-- ============================================================

salles = 0

-- Boucle de 1 à 5. À chaque tour, ajoute 1 à salles.
--
-- tour i = 1  →  salles = 0 + 1 = 1
-- tour i = 2  →  salles = 1 + 1 = 2
-- tour i = 3  →  salles = 2 + 1 = 3
-- tour i = 4  →  salles = 3 + 1 = 4
-- tour i = 5  →  salles = 4 + 1 = 5
--
-- Résultat attendu : salles == 5
--
-- Indice : for i = 1, 5 do ... end
--          et salles = salles + 1  (pas de += en Lua)

-- À toi :
for i = 1, 5 do
    salles = salles + 1
end

-- --- Vérification (ne pas modifier) ---
assert(salles == 5, "Obtenu : " .. salles .. ", attendu : 5")
print("✅ Correct !")
