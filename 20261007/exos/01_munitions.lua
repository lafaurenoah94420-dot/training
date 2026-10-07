-- ============================================================
-- The Last of Us — munitions
-- ============================================================
-- Joel part avec 35 balles. Il en tire 9. Il en ramasse 6.
-- Combien lui reste-t-il ?
--
-- Lance : lua 01_munitions.lua
-- ============================================================

restantes = 35 - 9 + 6

-- 35 - 9 = 26
-- 26 + 6 = 32
--
-- Résultat attendu : restantes == 32
--
-- Indice : une expression avec - et +

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(restantes == 32, "Recompte : 35 - 9 + 6 = ?")
print("✅ Correct !")
