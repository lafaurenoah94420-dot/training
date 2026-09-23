-- ============================================================
-- Resident Evil — fichier save
-- ============================================================
-- Le disque affiche "SLOT_A.SAV". Pour le catalogue, le jeu
-- convertit le nom en minuscules.
--
-- Lance : lua 02_minuscules.lua
-- ============================================================

fichier = "SLOT_A.SAV"
catalogue = string.lower(fichier)

-- Mets fichier en minuscules dans catalogue.
-- "SLOT_A.SAV" → "slot_a.sav"
--
-- Résultat attendu : catalogue == "slot_a.sav"
--
-- Indice : string.lower(...)

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(catalogue == "slot_a.sav", "Obtenu : '" .. tostring(catalogue) .. "'")
print("✅ Correct !")
