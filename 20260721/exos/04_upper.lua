-- ============================================================
-- Resident Evil — label d'objet
-- ============================================================
-- L'inventaire affiche les noms d'objets en majuscules.
-- Transforme le nom de l'herb.
--
-- Lance : lua 04_upper.lua
-- ============================================================

objet = "herb verte"
label = ""

-- Transforme objet en majuscules et stocke le résultat dans label.
--
-- "herb verte"  →  "HERB VERTE"
--
-- Résultat attendu : label == "HERB VERTE"
--
-- Indice : string.upper() — n'oublie pas de ranger le résultat

-- À toi :
label = string.upper(objet)

-- --- Vérification (ne pas modifier) ---
assert(label == "HERB VERTE", "Obtenu : '" .. label .. "'")
print("✅ Correct !")
