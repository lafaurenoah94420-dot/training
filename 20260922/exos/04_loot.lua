-- ============================================================
-- Project Zomboid — loot
-- ============================================================
-- L'inventaire a déjà "visseuse". Tu ajoutes "bois" puis
-- "clous" avec table.insert.
--
-- Lance : lua 04_loot.lua
-- ============================================================

inventaire = { "visseuse" }

-- Après : { "visseuse", "bois", "clous" }
--
-- Résultat attendu : # == 3, [2] == "bois", [3] == "clous"
--
-- Indice : table.insert(inventaire, "...")

-- À toi :
table.insert(inventaire, "bois")
table.insert(inventaire, "clous")

-- --- Vérification (ne pas modifier) ---
assert(#inventaire == 3, "Il faut 3 objets, obtenu : " .. #inventaire)
assert(inventaire[2] == "bois", "Le 2e doit être bois")
assert(inventaire[3] == "clous", "Le 3e doit être clous")
print("✅ Correct !")
