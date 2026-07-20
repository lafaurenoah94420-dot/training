-- ============================================================
-- Project Zomboid — jet de dés
-- ============================================================
-- Tu fouilles un placard. Le jeu tire un nombre entre 1 et 6
-- pour décider ce que tu trouves. Avec la graine fixe, le jet
-- est toujours le même pour cet exercice.
--
-- Lance : lua 03_random.lua
-- ============================================================

math.randomseed(42)
jet = 0

-- Tire un nombre au hasard entre 1 et 6, stocke-le dans jet.
-- (la graine est déjà fixée au-dessus — ne la change pas)
--
-- Avec cette graine : math.random(1, 6)  →  6
--
-- Résultat attendu : jet == 6
--
-- Indice : math.random(min, max)

-- À toi :
jet = math.random(1, 6)

-- --- Vérification (ne pas modifier) ---
assert(jet == 6, "Obtenu : " .. tostring(jet) .. ", attendu : 6")
print("✅ Correct !")
