-- ============================================================
-- Project Zomboid — ramasser du loot
-- ============================================================
-- L'inventaire a déjà "couteau". Tu ajoutes "bandage" puis
-- "conserve" avec table.insert.
--
-- Lance : lua 04_loot.lua
-- ============================================================

inventaire = { "couteau" }

-- Après : { "couteau", "bandage", "conserve" }
--
-- Résultat attendu : # == 3, [2] == "bandage", [3] == "conserve"
--
-- Indice : table.insert(inventaire, "...")

-- À toi :
table.insert(inventaire, "bandage")
table.insert(inventaire, "conserve")

-- --- Vérification (ne pas modifier) ---
assert(#inventaire == 3, "Il faut 3 objets, obtenu : " .. #inventaire)
assert(inventaire[2] == "bandage", "Le 2e doit être bandage")
assert(inventaire[3] == "conserve", "Le 3e doit être conserve")
print("✅ Correct !")
