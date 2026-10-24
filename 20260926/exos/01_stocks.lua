-- ============================================================
-- The Last of Us — stocks de Joel
-- ============================================================
-- Joel part avec 40 balles. Il en tire 12. Ellie lui en donne 5.
-- Combien lui reste-t-il ?
--
-- Lance : lua 01_stocks.lua
-- ============================================================

restantes = 0

-- 40 - 12 = 28
-- 28 + 5  = 33
--
-- Résultat attendu : restantes == 33
--
-- Indice : une expression avec - et +

-- À toi :
restantes = 40 - 12 + 5

-- --- Vérification (ne pas modifier) ---
assert(restantes == 33, "Recompte : 40 - 12 + 5 = ?")
print("✅ Correct !")
