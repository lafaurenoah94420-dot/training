-- ============================================================
-- Resident Evil — nom d'arme
-- ============================================================
-- L'inventaire affiche l'arme en majuscules.
--
-- Lance : lua 04_upper.lua
-- ============================================================

arme = "matilda"
label = ""

-- Transforme arme en majuscules → label.
--
-- "matilda"  →  "MATILDA"
--
-- Résultat attendu : label == "MATILDA"
--
-- Indice : string.upper() — range le résultat

-- À toi :
label = string.upper(arme)

-- --- Vérification (ne pas modifier) ---
assert(label == "MATILDA", "Obtenu : '" .. label .. "'")
print("✅ Correct !")
