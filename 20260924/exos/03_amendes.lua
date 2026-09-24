-- ============================================================
-- GTA — total des amendes
-- ============================================================
-- Franklin a pris plusieurs amendes. Tu additionnes tout.
--
-- Lance : lua 03_amendes.lua
-- ============================================================

amendes = { 100, 250, 75, 50 }
total = 0

-- Parcours amendes avec ipairs, ajoute chaque x à total.
--
-- 0+100=100, +250=350, +75=425, +50=475
--
-- Résultat attendu : total == 475
--
-- Indice : for _, x in ipairs(amendes) do
--          total = total + x

-- À toi :
for i, x in ipairs(amendes) do
    total = total + x
end
-- --- Vérification (ne pas modifier) ---
assert(total == 475, "Obtenu : " .. tostring(total) .. ", attendu : 475")
print("✅ Correct !")
