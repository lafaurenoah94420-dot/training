-- ============================================================
-- Project Zomboid — stock de bandages
-- ============================================================
-- Tu as 14 bandages. Tu en utilises 5 sur des blessures,
-- puis tu en trouves 3 dans une pharmacie. Combien en reste-t-il ?
--
-- Lance : lua 01_calcul.lua
-- ============================================================

bandages = 0

-- Calcule les bandages restants avec une seule expression.
--
-- 14 - 5 = 9   (après les soins)
-- 9 + 3 = 12   (après la pharmacie)
--
-- Résultat attendu : bandages == 12
--
-- Indice : une expression avec - et +

-- À toi :
bandages = 14 - 5 + 3

-- --- Vérification (ne pas modifier) ---
assert(bandages == 12, "Recompte : 14 - 5 + 3 = ?")
print("✅ Correct !")
