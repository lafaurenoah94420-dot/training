-- ============================================================
-- GTA — total des pots-de-vin
-- ============================================================
-- Franklin a versé plusieurs pots-de-vin. Tu additionnes tout.
--
-- Lance : lua 03_pots.lua
-- ============================================================

pots = { 200, 150, 300, 50 }
total = 0

-- Parcours pots avec ipairs, ajoute chaque x à total.
--
-- 0+200=200, +150=350, +300=650, +50=700
--
-- Résultat attendu : total == 700
--
-- Indice : for _, x in ipairs(pots) do
--          total = total + x

-- À toi :
for i, x in ipairs(pots) do
    total = total + x
end
-- --- Vérification (ne pas modifier) ---
assert(total == 700, "Obtenu : " .. tostring(total) .. ", attendu : 700")
print("✅ Correct !")
