-- ============================================================
-- The Last of Us — sac de Joel
-- ============================================================
-- Le sac n'a pas encore de "corde". Tu l'ajoutes avec la valeur 1.
--
-- Lance : lua 02_sac.lua
-- ============================================================

sac = { eau = 2, nourriture = 3 }

-- Ajoute la clé "corde" avec la valeur 1
-- → sac["corde"] = 1
--
-- Résultat attendu : sac["corde"] == 1
--
-- Indice : sac["corde"] = ...

-- À toi :
sac["corde"] = 1

-- --- Vérification (ne pas modifier) ---
assert(sac["corde"] == 1, "sac['corde'] devrait être 1, obtenu : " .. tostring(sac["corde"]))
print("✅ Correct !")
