-- Exercice 4 — Ajouter à une liste (Project Zomboid)
--
-- Tu as un inventaire presque vide.
-- Ajoute "conserve" puis "bandage" avec table.insert.

local inventaire = { "couteau" }

-- TODO : ajoute "conserve", puis "bandage"
table.insert(inventaire, "conserve")
table.insert(inventaire, "bandage")
-- --- Vérification ---
assert(#inventaire == 3, "L'inventaire doit avoir 3 objets")
assert(inventaire[2] == "conserve", "Le 2e objet doit être conserve")
assert(inventaire[3] == "bandage", "Le 3e objet doit être bandage")
print("04_inventaire OK")
