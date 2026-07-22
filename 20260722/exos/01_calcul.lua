-- ============================================================
-- Resident Evil — stock de munitions
-- ============================================================
-- Leon a 24 balles. Il en tire 9, puis en trouve 6 dans un tiroir.
-- Combien lui en reste-t-il ?
--
-- Lance : lua 01_calcul.lua
-- ============================================================

balles = 0

-- Calcule les balles restantes avec une seule expression.
--
-- 24 - 9 = 15
-- 15 + 6 = 21
--
-- Résultat attendu : balles == 21
--
-- Indice : une expression avec - et +

-- À toi :
balles = 0 + 24 - 9 + 6

-- --- Vérification (ne pas modifier) ---
assert(balles == 21, "Recompte : 24 - 9 + 6 = ?")
print("✅ Correct !")
