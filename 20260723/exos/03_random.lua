-- ============================================================
-- Project Zomboid — loot aléatoire
-- ============================================================
-- Tu ouvres un placard. Le jeu tire un nombre entre 1 et 10.
-- Avec la graine fixe, le jet est toujours le même ici.
--
-- Lance : lua 03_random.lua
-- ============================================================

math.randomseed(7)
loot = 0

-- Tire un nombre entre 1 et 10, stocke-le dans loot.
--
-- Avec cette graine : math.random(1, 10)  →  8
--
-- Résultat attendu : loot == 8
--
-- Indice : math.random(min, max)

-- À toi :
loot = math.random(1, 10)

-- --- Vérification (ne pas modifier) ---
assert(loot == 8, "Obtenu : " .. tostring(loot) .. ", attendu : 8")
print("✅ Correct !")
