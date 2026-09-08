-- ============================================================
-- GTA — étages du building
-- ============================================================
-- Franklin monte du 1er au 4e étage. Affiche chaque étage,
-- puis stocke le dernier dans dernier_etage.
--
-- Lance : lua 03_etages.lua
-- ============================================================

dernier_etage = nil

-- Boucle for de 1 à 4 :
--   print("Étage " .. i)
-- À la fin : dernier_etage == 4
--
-- Résultat attendu : dernier_etage == 4
--
-- Indice : for i = 1, 4 do ... end
--          (pas ipairs — tu comptes, tu ne parcours pas une liste)

-- À toi :
for i = 1, 4 do
    print("Étage " .. i)
    dernier_etage = i
end

-- --- Vérification (ne pas modifier) ---
assert(dernier_etage == 4, "Obtenu : " .. tostring(dernier_etage) .. ", attendu : 4")
print("✅ Correct !")
