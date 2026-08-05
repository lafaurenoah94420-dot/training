-- ============================================================
-- Resident Evil — code d'accès
-- ============================================================
-- Le clavier du manoir n'accepte que les codes en majuscules.
-- Tu transformes l'entrée du joueur.
--
-- Lance : lua 01_majuscules.lua
-- ============================================================

code = "porte-ouest"
affiche = ""

-- Mets code en majuscules dans affiche.
-- "porte-ouest" → "PORTE-OUEST"
--
-- Résultat attendu : affiche == "PORTE-OUEST"
--
-- Indice : string.upper(...) — stocke le résultat

-- À toi :
affiche = string.upper(code)

-- --- Vérification (ne pas modifier) ---
assert(affiche == "PORTE-OUEST", "Obtenu : '" .. tostring(affiche) .. "'")
print("✅ Correct !")
