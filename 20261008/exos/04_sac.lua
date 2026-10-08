-- ============================================================
-- Project Zomboid — sac à dos
-- ============================================================
-- Tu trouves une lampe. Tu l'ajoutes dans le sac.
--
-- Lance : lua 04_sac.lua
-- ============================================================

sac = { "eau", "conserve" }

-- Ajoute "lampe" à la fin de sac.
-- Après : sac a 3 éléments, le dernier est "lampe"
--
-- Résultat attendu : sac[3] == "lampe"
--
-- Indice : table.insert()

-- À toi :
table.insert(sac, "lampe")

-- --- Vérification (ne pas modifier) ---
assert(sac[3] == "lampe", "sac[3] devrait être 'lampe', obtenu : '" .. tostring(sac[3]) .. "'")
print("✅ Correct !")
