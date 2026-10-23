-- ============================================================
-- Resident Evil — recharge
-- ============================================================
-- Leon a 8 balles. Il en ramasse 5 — tu ajoutes 5 à balles.
--
-- Lance : lua 02_balles.lua
-- ============================================================

inventaire = { balles = 8, herb = 2 }

-- inventaire["balles"] doit passer de 8 à 13
-- → ajoute 5 à la valeur actuelle
--
-- 8 + 5 = 13
--
-- Résultat attendu : inventaire["balles"] == 13
--
-- Indice : inventaire["balles"] = inventaire["balles"] + 5

-- À toi :
inventaire["balles"] = inventaire["balles"] + 5

-- --- Vérification (ne pas modifier) ---
assert(inventaire["balles"] == 13, "Obtenu : " .. tostring(inventaire["balles"]) .. ", attendu : 13")
print("✅ Correct !")
