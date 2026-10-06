-- ============================================================
-- Project Zomboid — total du loot
-- ============================================================
-- Tu additionnes le poids de chaque objet ramassé.
--
-- Lance : lua 03_loot.lua
-- ============================================================

poids = { 2, 5, 1, 4 }
total = 0

-- Parcours poids avec ipairs, ajoute chaque x à total.
--
-- 0+2=2, +5=7, +1=8, +4=12
--
-- Résultat attendu : total == 12
--
-- Indice : for _, x in ipairs(...) do
--          total = total + x

-- À toi :
for i, x in ipairs(poids) do
    total = total + x
end
-- --- Vérification (ne pas modifier) ---
assert(total == 12, "Obtenu : " .. tostring(total) .. ", attendu : 12")
print("✅ Correct !")
