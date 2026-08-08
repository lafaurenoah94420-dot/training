-- ============================================================
-- Resident Evil — balles lourdes
-- ============================================================
-- Le chargeur liste le calibre de chaque balle (un nombre).
-- Compte combien sont strictement plus grandes que 9.
--
-- Lance : lua 05_lourdes.lua
-- ============================================================

calibres = { 9, 12, 9, 45, 9, 12 }
nb = 0

-- Parcours avec ipairs. Si x > 9, nb = nb + 1.
--
-- 9 non, 12 oui→1, 9 non, 45 oui→2, 9 non, 12 oui→3
--
-- Résultat attendu : nb == 3
--
-- Indice : for _, x in ipairs(calibres) do + if x > 9 then
--          nb = nb + 1  (pas nb = 0)

-- À toi :
for i, x in ipairs(calibres) do
    if x > 9 then
        nb = nb + 1
    end
end

-- --- Vérification (ne pas modifier) ---
assert(nb == 3, "Obtenu : " .. tostring(nb) .. ", attendu : 3")
print("✅ Correct !")
