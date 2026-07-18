-- ============================================================
-- GTA — inventaire de butin
-- ============================================================
-- Franklin ramasse 3 objets pendant une mission. Il les ajoute
-- un par un dans son inventaire.
--
-- Lance : lua 04_insert.lua
-- ============================================================

inventaire = {}

-- Ajoute ces 3 objets dans inventaire, dans cet ordre :
-- "cle", "montre", "diamant"
--
-- Après insert 1 : inventaire a 1 élément  →  #inventaire == 1
-- Après insert 2 : inventaire a 2 éléments →  #inventaire == 2
-- Après insert 3 : inventaire a 3 éléments →  #inventaire == 3
--
-- Résultat attendu :
--   #inventaire == 3
--   inventaire[1] == "cle"
--   inventaire[2] == "montre"
--   inventaire[3] == "diamant"
--
-- Indice : table.insert(inventaire, "...")

-- À toi :
table.insert(inventaire, "cle")
table.insert(inventaire, "montre")
table.insert(inventaire, "diamant")

-- --- Vérification (ne pas modifier) ---
assert(#inventaire == 3, "Obtenu " .. #inventaire .. " objets, attendu : 3")
assert(inventaire[1] == "cle", "inventaire[1] doit être 'cle'")
assert(inventaire[2] == "montre", "inventaire[2] doit être 'montre'")
assert(inventaire[3] == "diamant", "inventaire[3] doit être 'diamant'")
print("✅ Correct !")
