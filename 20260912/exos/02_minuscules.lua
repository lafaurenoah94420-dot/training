-- ============================================================
-- Resident Evil — nom de fichier
-- ============================================================
-- Le terminal affiche "MAP_WEST.TXT". Pour la recherche, le jeu
-- convertit en minuscules.
--
-- Lance : lua 02_minuscules.lua
-- ============================================================

fichier = "MAP_WEST.TXT"
recherche = string.lower(fichier)

-- Mets fichier en minuscules dans recherche.
-- "MAP_WEST.TXT" → "map_west.txt"
--
-- Résultat attendu : recherche == "map_west.txt"
--
-- Indice : string.lower(...)

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(recherche == "map_west.txt", "Obtenu : '" .. tostring(recherche) .. "'")
print("✅ Correct !")
