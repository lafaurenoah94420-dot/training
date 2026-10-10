-- ============================================================
-- Project Zomboid — stock de bandages
-- ============================================================
-- Tu as 28 bandages. Tu en utilises 11. Tu en trouves 7.
-- Combien t'en reste-t-il ?
--
-- Lance : lua 01_stock.lua
-- ============================================================

restants = 28 - 11 + 7

-- 28 - 11 = 17
-- 17 + 7  = 24
--
-- Résultat attendu : restants == 24
--
-- Indice : une expression avec - et +

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(restants == 24, "Recompte : 28 - 11 + 7 = ?")
print("✅ Correct !")
