-- ============================================================
-- GTA — butin après braquage
-- ============================================================
-- L'équipe part avec 5000 $. Elle dépense 1200 en pots-de-vin,
-- puis trouve 800 $ dans un coffre. Combien reste-t-il ?
--
-- Lance : lua 01_butin.lua
-- ============================================================

butin = 0

-- 5000 - 1200 = 3800
-- 3800 + 800 = 4600
--
-- Résultat attendu : butin == 4600
--
-- Indice : une expression avec - et +

-- À toi :
butin = 5000 - 1200 + 800

-- --- Vérification (ne pas modifier) ---
assert(butin == 4600, "Recompte : 5000 - 1200 + 800 = ?")
print("✅ Correct !")
