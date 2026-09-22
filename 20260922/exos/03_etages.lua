-- ============================================================
-- GTA — étages
-- ============================================================
-- Franklin monte du 1er au 3e étage. Affiche chaque étage,
-- puis stocke le dernier dans dernier_etage.
--
-- Lance : lua 03_etages.lua
-- ============================================================

dernier_etage = nil

-- Boucle for de 1 à 3 :
--   print("Étage " .. i)
-- À la fin : dernier_etage == 3
--
-- Résultat attendu : dernier_etage == 3
--
-- Indice : for i = 1, 3 do ... end
--          (pas ipairs — tu comptes, tu ne parcours pas une liste)
--          n'oublie pas d'assigner dernier_etage

-- À toi :
for i = 1, 3 do
    print("Étage " .. i)
end
dernier_etage = 3
-- --- Vérification (ne pas modifier) ---
assert(dernier_etage == 3, "Obtenu : " .. tostring(dernier_etage) .. ", attendu : 3")
print("✅ Correct !")
