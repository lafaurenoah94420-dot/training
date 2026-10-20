-- ============================================================
-- Project Zomboid — loot
-- ============================================================
-- Tu trouves une clé. Tu l'ajoutes dans le coffre.
--
-- Lance : lua 04_loot.lua
-- ============================================================

coffre = { "conserve", "eau" }

-- Ajoute "clé" à la fin de coffre.
-- Après : coffre a 3 éléments, le dernier est "clé"
--
-- Résultat attendu : coffre[3] == "clé"
--
-- Indice : table.insert()

-- À toi :
table.insert(coffre, "clé")

-- --- Vérification (ne pas modifier) ---
assert(coffre[3] == "clé", "coffre[3] devrait être 'clé', obtenu : '" .. tostring(coffre[3]) .. "'")
print("✅ Correct !")
