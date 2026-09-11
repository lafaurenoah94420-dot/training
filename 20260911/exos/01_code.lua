-- ============================================================
-- Resident Evil — code clavier
-- ============================================================
-- Le clavier du manoir n'accepte que les codes en majuscules.
-- Tu transformes l'entrée de Leon.
--
-- Lance : lua 01_code.lua
-- ============================================================

entree = "salle-b"
code = string.upper(entree)

-- Mets entree en majuscules dans code.
-- "salle-b" → "SALLE-B"
--
-- Résultat attendu : code == "SALLE-B"
--
-- Indice : string.upper(...) — stocke le résultat

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(code == "SALLE-B", "Obtenu : '" .. tostring(code) .. "'")
print("✅ Correct !")
