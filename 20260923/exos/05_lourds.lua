-- ============================================================
-- Resident Evil — objets lourds
-- ============================================================
-- L'inventaire liste le poids de chaque objet. Compte combien
-- pèsent strictement plus de 6.
--
-- Lance : lua 05_lourds.lua
-- ============================================================

poids = { 4, 8, 6, 11, 3, 9 }
nb = 0

-- Parcours avec ipairs. Si x > 6, nb = nb + 1.
--
-- 4 non, 8 oui→1, 6 non, 11 oui→2, 3 non, 9 oui→3
--
-- Résultat attendu : nb == 3
--
-- Indice : for _, x in ipairs(poids) do + if x > 6 then
--          nb = nb + 1

-- À toi :
for i, x in ipairs(poids) do
    if x > 6 then
        nb = nb + 1
    end
end

-- --- Vérification (ne pas modifier) ---
assert(nb == 3, "Obtenu : " .. tostring(nb) .. ", attendu : 3")
print("✅ Correct !")
