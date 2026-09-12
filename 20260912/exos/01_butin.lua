-- ============================================================
-- GTA — butin de mission
-- ============================================================
-- Franklin gagne 1800 $. Il dépense 350 $ en essence, puis
-- récupère 90 $ dans un portefeuille. Combien reste-t-il ?
--
-- Lance : lua 01_butin.lua
-- ============================================================

butin = 1800 - 350 + 90

-- 1800 - 350 = 1450
-- 1450 + 90 = 1540
--
-- Résultat attendu : butin == 1540
--
-- Indice : une expression avec - et +

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(butin == 1540, "Recompte : 1800 - 350 + 90 = ?")
print("✅ Correct !")
