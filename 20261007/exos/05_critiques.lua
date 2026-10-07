-- ============================================================
-- Hearts of Iron IV — coups critiques
-- ============================================================
-- Tu comptes combien de tirs font plus de 20 de dégâts.
--
-- Lance : lua 05_critiques.lua
-- ============================================================

tirs = { 12, 25, 8, 30, 22 }
critiques = 0

-- Parcours tirs avec ipairs.
-- Si x > 20, critiques = critiques + 1
--
-- 12 → non
-- 25 → oui → 1
-- 8  → non
-- 30 → oui → 2
-- 22 → oui → 3
--
-- Résultat attendu : critiques == 3
--
-- Indice : for _, x in ipairs(tirs) do + if x > 20

-- À toi :
for i, x in ipairs(tirs) do
    if x > 20 then
        critiques = critiques + 1
    end
end

-- --- Vérification (ne pas modifier) ---
assert(critiques == 3, "Obtenu : " .. tostring(critiques) .. ", attendu : 3")
print("✅ Correct !")
