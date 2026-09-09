-- ============================================================
-- Resident Evil — fichier de save
-- ============================================================
-- Le disque affiche "SAVE_01.BIN". Pour le catalogue, le jeu
-- convertit le nom en minuscules.
--
-- Lance : lua 02_minuscules.lua
-- ============================================================

fichier = "SAVE_01.BIN"
catalogue = ""

-- Mets fichier en minuscules dans catalogue.
-- "SAVE_01.BIN" → "save_01.bin"
--
-- Résultat attendu : catalogue == "save_01.bin"
--
-- Indice : string.lower(...)

-- À toi :
catalogue = string.lower(fichier)

-- --- Vérification (ne pas modifier) ---
assert(catalogue == "save_01.bin", "Obtenu : '" .. tostring(catalogue) .. "'")
print("✅ Correct !")
