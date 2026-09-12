-- ============================================================
-- Resident Evil — calibres lourds
-- ============================================================
-- Le chargeur liste des calibres. Compte combien sont
-- strictement plus grands que 10.
--
-- Lance : lua 05_calibres.lua
-- ============================================================

calibres = { 9, 12, 45, 9, 12, 5 }
nb = 0

-- Parcours avec ipairs. Si x > 10, nb = nb + 1.
--
-- 9 non, 12 oui→1, 45 oui→2, 9 non, 12 oui→3, 5 non
--
-- Résultat attendu : nb == 3
--
-- Indice : for _, x in ipairs(calibres) do + if x > 10 then
--          nb = nb + 1

-- À toi :
for i, x in ipairs(calibres) do
    if x > 10 then
        nb = nb + 1
    end
end
-- --- Vérification (ne pas modifier) ---
assert(nb == 3, "Obtenu : " .. tostring(nb) .. ", attendu : 3")
print("✅ Correct !")
