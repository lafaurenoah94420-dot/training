-- ============================================================
-- Resident Evil — recherche
-- ============================================================
-- Le terminal affiche "HERB.TXT". Pour chercher, le jeu convertit
-- en minuscules.
--
-- Lance : lua 01_minuscules.lua
-- ============================================================

fichier = "HERB.TXT"
recherche = ""

-- Mets fichier en minuscules dans recherche.
-- "HERB.TXT" → "herb.txt"
--
-- Résultat attendu : recherche == "herb.txt"
--
-- Indice : string.lower(...)

-- À toi :
recherche = string.lower(fichier)

-- --- Vérification (ne pas modifier) ---
assert(recherche == "herb.txt", "Obtenu : '" .. tostring(recherche) .. "'")
print("✅ Correct !")
