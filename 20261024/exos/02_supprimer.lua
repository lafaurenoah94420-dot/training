-- ============================================================
-- Project Zomboid — jeter un objet
-- ============================================================
-- Tu jettes la "lampe" du sac. Pour supprimer une clé,
-- tu la mets à nil.
--
-- Lance : lua 02_supprimer.lua
-- ============================================================

sac = { eau = 2, lampe = 1, conserve = 3 }

-- Supprime la clé "lampe" → sac["lampe"] = nil
--
-- Résultat attendu : sac["lampe"] == nil
--
-- Indice : sac["lampe"] = nil

-- À toi :
sac["lampe"] = nil

-- --- Vérification (ne pas modifier) ---
assert(sac["lampe"] == nil, "sac['lampe'] devrait être nil")
assert(sac["eau"] == 2, "ne touche pas aux autres clés")
print("✅ Correct !")
