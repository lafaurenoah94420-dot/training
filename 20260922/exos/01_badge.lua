-- ============================================================
-- Resident Evil — badge scanner
-- ============================================================
-- Le scanner n'accepte que les badges en majuscules.
-- Tu transformes le nom entré par Leon.
--
-- Lance : lua 01_badge.lua
-- ============================================================

entree = "labo-est"
badge = string.upper(entree)

-- Mets entree en majuscules dans badge.
-- "labo-est" → "LABO-EST"
--
-- Résultat attendu : badge == "LABO-EST"
--
-- Indice : string.upper(...) — stocke le résultat

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(badge == "LABO-EST", "Obtenu : '" .. tostring(badge) .. "'")
print("✅ Correct !")
