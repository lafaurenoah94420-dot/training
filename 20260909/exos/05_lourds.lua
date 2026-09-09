-- ============================================================
-- Resident Evil — objets lourds
-- ============================================================
-- L'inventaire liste le poids de chaque objet. Compte combien
-- pèsent strictement plus de 5.
--
-- Lance : lua 05_lourds.lua
-- ============================================================

poids = { 3, 8, 5, 12, 2, 9 }
nb = 0

-- Parcours avec ipairs. Si x > 5, nb = nb + 1.
--
-- 3 non, 8 oui→1, 5 non, 12 oui→2, 2 non, 9 oui→3
--
-- Résultat attendu : nb == 3
--
-- Indice : for _, x in ipairs(poids) do + if x > 5 then
--          nb = nb + 1

-- À toi :
for i, x in ipairs(poids) do
    if x > 5 then
        nb = nb + 1
    end
end
-- --- Vérification (ne pas modifier) ---
assert(nb == 3, "Obtenu : " .. tostring(nb) .. ", attendu : 3")
print("✅ Correct !")
