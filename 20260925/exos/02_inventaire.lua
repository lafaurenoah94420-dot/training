-- ============================================================
-- Resident Evil — inventaire
-- ============================================================
-- Leon ouvre son inventaire. Combien d'objets a-t-il ?
--
-- Lance : lua 02_inventaire.lua
-- ============================================================

objets = { "herb", "ammo", "clé", "map" }
taille = #objets

-- taille = nombre d'éléments dans objets → 4
--
-- Résultat attendu : taille == 4
--
-- Indice : opérateur #

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(taille == 4, "Obtenu : " .. tostring(taille) .. ", attendu : 4")
print("✅ Correct !")
