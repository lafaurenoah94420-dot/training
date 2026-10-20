-- ============================================================
-- Resident Evil — badge inventaire
-- ============================================================
-- L'UI affiche les noms d'objets en majuscules.
-- Transforme le nom pour l'écran.
--
-- Lance : lua 01_badge.lua
-- ============================================================

nom = "first aid"
badge = string.upper(nom)

-- Transforme nom en majuscules → "FIRST AID"
--
-- Résultat attendu : badge == "FIRST AID"
--
-- Indice : string.upper()

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(badge == "FIRST AID", "Obtenu : '" .. tostring(badge) .. "'")
print("✅ Correct !")
