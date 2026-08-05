-- ============================================================
-- Project Zomboid — loot
-- ============================================================
-- Tu fouilles un placard. L'inventaire a déjà "tournevis".
-- Tu ajoutes "conserve" puis "batterie" avec table.insert.
--
-- Lance : lua 04_loot.lua
-- ============================================================

inventaire = { "tournevis" }

-- Après les ajouts : {"tournevis", "conserve", "batterie"}
--
-- Résultat attendu : #inventaire == 3, inventaire[2] == "conserve",
--                    inventaire[3] == "batterie"
--
-- Indice : table.insert(inventaire, "...")

-- À toi :
table.insert(inventaire, "conserve")
table.insert(inventaire, "batterie")

-- --- Vérification (ne pas modifier) ---
assert(#inventaire == 3, "Il faut 3 objets, obtenu : " .. #inventaire)
assert(inventaire[2] == "conserve", "Le 2e doit être conserve")
assert(inventaire[3] == "batterie", "Le 3e doit être batterie")
print("✅ Correct !")
