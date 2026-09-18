-- ============================================================
-- GTA — points de missions
-- ============================================================
-- Franklin enchaîne des missions. Tu additionnes tous les scores.
--
-- Lance : lua 03_points.lua
-- ============================================================

points = { 40, 70, 25, 90 }
total = 0

-- Parcours points avec ipairs, ajoute chaque x à total.
--
-- 0+40=40, +70=110, +25=135, +90=225
--
-- Résultat attendu : total == 225
--
-- Indice : for _, x in ipairs(points) do
--          total = total + x

-- À toi :
for i, x in ipairs(points) do
    total = total + x
end
-- --- Vérification (ne pas modifier) ---
assert(total == 225, "Obtenu : " .. tostring(total) .. ", attendu : 225")
print("✅ Correct !")
