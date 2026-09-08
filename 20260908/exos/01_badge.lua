-- ============================================================
-- Resident Evil — badge d'accès
-- ============================================================
-- Le scanner n'accepte que les badges en majuscules.
-- Tu transformes le nom entré par Leon.
--
-- Lance : lua 01_badge.lua
-- ============================================================

entree = "leon s."
badge = ""

-- Mets entree en majuscules dans badge.
-- "leon s." → "LEON S."
--
-- Résultat attendu : badge == "LEON S."
--
-- Indice : string.upper(...) — stocke le résultat

-- À toi :
badge = string.upper(entree)

-- --- Vérification (ne pas modifier) ---
assert(badge == "LEON S.", "Obtenu : '" .. tostring(badge) .. "'")
print("✅ Correct !")
