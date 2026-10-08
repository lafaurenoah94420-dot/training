-- ============================================================
-- The Last of Us — taille de l'équipe
-- ============================================================
-- Combien de survivants sont dans le groupe ?
--
-- Lance : lua 02_equipe.lua
-- ============================================================

groupe = { "Joel", "Ellie", "Tommy", "Maria" }
taille = 0

-- taille = nombre d'éléments dans groupe → 4
--
-- Résultat attendu : taille == 4
--
-- Indice : opérateur #

-- À toi :
taille = #groupe

-- --- Vérification (ne pas modifier) ---
assert(taille == 4, "Obtenu : " .. tostring(taille) .. ", attendu : 4")
print("✅ Correct !")
