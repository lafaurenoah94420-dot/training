-- ============================================================
-- GTA — cash après braquage
-- ============================================================
-- Franklin gagne 3200 $. Il paie 600 $ de pots-de-vin, puis
-- trouve 250 $ dans un tiroir. Combien lui reste-t-il ?
--
-- Lance : lua 01_cash.lua
-- ============================================================

cash = 0

-- 3200 - 600 = 2600
-- 2600 + 250 = 2850
--
-- Résultat attendu : cash == 2850
--
-- Indice : une expression avec - et +

-- À toi :
cash = 3200 - 600 + 250

-- --- Vérification (ne pas modifier) ---
assert(cash == 2850, "Recompte : 3200 - 600 + 250 = ?")
print("✅ Correct !")
