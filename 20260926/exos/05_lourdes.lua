-- ============================================================
-- Hearts of Iron IV — divisions lourdes
-- ============================================================
-- Tu comptes combien de divisions ont plus de 50 de force.
--
-- Lance : lua 05_lourdes.lua
-- ============================================================

forces = { 40, 72, 55, 30, 90 }
lourdes = 0

-- Parcours forces avec ipairs.
-- Si x > 50, lourdes = lourdes + 1
--
-- 40 → non
-- 72 → oui → 1
-- 55 → oui → 2
-- 30 → non
-- 90 → oui → 3
--
-- Résultat attendu : lourdes == 3
--
-- Indice : for _, x in ipairs(...) do + if x > 50

-- À toi :
for i, x in ipairs(...) do
    if x > 50 then
        lourdes + 1
    end
end
-- --- Vérification (ne pas modifier) ---
assert(lourdes == 3, "Obtenu : " .. tostring(lourdes) .. ", attendu : 3")
print("✅ Correct !")
