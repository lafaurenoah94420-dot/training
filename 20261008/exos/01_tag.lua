-- ============================================================
-- GTA — tag inventaire
-- ============================================================
-- L'UI affiche les noms d'armes en majuscules.
-- Transforme le nom pour l'écran.
--
-- Lance : lua 01_tag.lua
-- ============================================================

nom = "combat pistol"
tag = ""

-- Transforme nom en majuscules → "COMBAT PISTOL"
--
-- Résultat attendu : tag == "COMBAT PISTOL"
--
-- Indice : string.upper()

-- À toi :
tag = string.upper(nom)

-- --- Vérification (ne pas modifier) ---
assert(tag == "COMBAT PISTOL", "Obtenu : '" .. tostring(tag) .. "'")
print("✅ Correct !")
