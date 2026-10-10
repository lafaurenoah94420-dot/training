-- ============================================================
-- Hearts of Iron IV — unités d'élite
-- ============================================================
-- Tu comptes combien d'unités ont plus de 70 de force.
--
-- Lance : lua 05_elites.lua
-- ============================================================

forces = { 45, 82, 60, 91, 75 }
elites = 0

-- Parcours forces avec ipairs.
-- Si x > 70, elites = elites + 1
--
-- 45 → non
-- 82 → oui → 1
-- 60 → non
-- 91 → oui → 2
-- 75 → oui → 3
--
-- Résultat attendu : elites == 3
--
-- Indice : for _, x in ipairs(forces) do + if x > 70

-- À toi :
for _, x in ipairs(forces) do
    if x > 70 then
        elites = elites + 1
    end
end

-- --- Vérification (ne pas modifier) ---
assert(elites == 3, "Obtenu : " .. tostring(elites) .. ", attendu : 3")
print("✅ Correct !")
