-- ============================================================
-- The Last of Us — radio
-- ============================================================
-- Le message radio s'affiche en majuscules sur l'écran.
-- Transforme le texte pour l'affichage.
--
-- Lance : lua 01_radio.lua
-- ============================================================

texte = "jackson secure"
affiche = string.upper(texte)

-- Transforme texte en majuscules → "JACKSON SECURE"
--
-- Résultat attendu : affiche == "JACKSON SECURE"
--
-- Indice : string.upper()

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(affiche == "JACKSON SECURE", "Obtenu : '" .. tostring(affiche) .. "'")
print("✅ Correct !")
