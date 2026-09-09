-- ============================================================
-- GTA — cash après course
-- ============================================================
-- Franklin gagne 2500 $. Il paie 400 $ de réparations, puis
-- trouve 150 $ dans la boîte à gants. Combien lui reste-t-il ?
--
-- Lance : lua 01_cash.lua
-- ============================================================

cash = 0

-- 2500 - 400 = 2100
-- 2100 + 150 = 2250
--
-- Résultat attendu : cash == 2250
--
-- Indice : une expression avec - et +

-- À toi :
cash = 2500 - 400 + 150

-- --- Vérification (ne pas modifier) ---
assert(cash == 2250, "Recompte : 2500 - 400 + 150 = ?")
print("✅ Correct !")
