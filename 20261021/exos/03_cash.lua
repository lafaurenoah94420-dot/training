-- ============================================================
-- GTA — total du braquage
-- ============================================================
-- Franklin additionne le cash de chaque sac.
--
-- Lance : lua 03_cash.lua
-- ============================================================

sacs = { 200, 150, 80, 70 }
total = 0

-- Parcours sacs avec ipairs, ajoute chaque x à total.
--
-- 0+200=200, +150=350, +80=430, +70=500
--
-- Résultat attendu : total == 500
--
-- Indice : for _, x in ipairs(sacs) do
--          total = total + x

-- À toi :
for i, x in ipairs(sacs) do
    total = total + x
end

-- --- Vérification (ne pas modifier) ---
assert(total == 500, "Obtenu : " .. tostring(total) .. ", attendu : 500")
print("✅ Correct !")
