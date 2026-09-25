-- ============================================================
-- Project Zomboid — coffre
-- ============================================================
-- Tu trouves une hache. Tu l'ajoutes dans le coffre.
--
-- Lance : lua 04_coffre.lua
-- ============================================================

coffre = { "conserve", "bandage" }

-- Ajoute "hache" à la fin de coffre.
-- Après : coffre a 3 éléments, le dernier est "hache"
--
-- Résultat attendu : coffre[3] == "hache"
--
-- Indice : table.insert()

-- À toi :
table.insert(coffre, "hache")

-- --- Vérification (ne pas modifier) ---
assert(coffre[3] == "hache", "coffre[3] devrait être 'hache', obtenu : '" .. tostring(coffre[3]) .. "'")
print("✅ Correct !")
