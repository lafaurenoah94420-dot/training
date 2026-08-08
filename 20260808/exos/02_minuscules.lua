-- ============================================================
-- Resident Evil — nom de fichier
-- ============================================================
-- Le journal affiche "ANTIDOTE.DAT". Pour la recherche interne,
-- le jeu convertit en minuscules.
--
-- Lance : lua 02_minuscules.lua
-- ============================================================

fichier = "ANTIDOTE.DAT"
recherche = string.lower(fichier)

-- Mets fichier en minuscules dans recherche.
-- "ANTIDOTE.DAT" → "antidote.dat"
--
-- Résultat attendu : recherche == "antidote.dat"
--
-- Indice : string.lower(...)

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(recherche == "antidote.dat", "Obtenu : '" .. tostring(recherche) .. "'")
print("✅ Correct !")
