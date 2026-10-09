-- ============================================================
-- GTA — total des points
-- ============================================================
-- Franklin additionne les points de chaque mission.
--
-- Lance : lua 03_points.lua
-- ============================================================

scores = { 50, 80, 30, 40 }
total = 0

-- Parcours scores avec ipairs, ajoute chaque x à total.
--
-- 0+50=50, +80=130, +30=160, +40=200
--
-- Résultat attendu : total == 200
--
-- Indice : for _, x in ipairs(scores) do
--          total = total + x

-- À toi :
for i, x in ipairs(scores) do
    total = total + x
end
-- --- Vérification (ne pas modifier) ---
assert(total == 200, "Obtenu : " .. tostring(total) .. ", attendu : 200")
print("✅ Correct !")
