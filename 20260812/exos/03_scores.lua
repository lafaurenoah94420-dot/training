-- ============================================================
-- GTA — score de missions
-- ============================================================
-- Franklin enchaîne des missions. Tu additionnes tous les scores.
--
-- Lance : lua 03_scores.lua
-- ============================================================

scores = { 50, 80, 30, 100 }
total = 0

-- Parcours scores avec ipairs, ajoute chaque x à total.
--
-- 0+50=50, +80=130, +30=160, +100=260
--
-- Résultat attendu : total == 260
--
-- Indice : for _, x in ipairs(scores) do
--          total = total + x

-- À toi :
for i, x in ipairs(scores) do
    total = total + x
end
-- --- Vérification (ne pas modifier) ---
assert(total == 260, "Obtenu : " .. tostring(total) .. ", attendu : 260")
print("✅ Correct !")
