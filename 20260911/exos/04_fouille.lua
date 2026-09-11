-- ============================================================
-- Project Zomboid — fouille
-- ============================================================
-- L'inventaire a déjà "lampe". Tu ajoutes "corde" puis "nails"
-- avec table.insert.
--
-- Lance : lua 04_fouille.lua
-- ============================================================

inventaire = { "lampe" }

-- Après : { "lampe", "corde", "nails" }
--
-- Résultat attendu : # == 3, [2] == "corde", [3] == "nails"
--
-- Indice : table.insert(inventaire, "...")

-- À toi :
table.insert(inventaire, "corde")
table.insert(inventaire, "nails")
-- --- Vérification (ne pas modifier) ---
assert(#inventaire == 3, "Il faut 3 objets, obtenu : " .. #inventaire)
assert(inventaire[2] == "corde", "Le 2e doit être corde")
assert(inventaire[3] == "nails", "Le 3e doit être nails")
print("✅ Correct !")
