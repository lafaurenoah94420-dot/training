-- ============================================================
-- Project Zomboid — objets utiles
-- ============================================================
-- Compte combien d'objets ont un poids > 4.
--
-- Lance : lua 04_utiles.lua
-- ============================================================

poids = { 2, 6, 1, 9, 4 }
nb = 0

-- Parcours poids avec ipairs. Si x > 4, nb = nb + 1.
--
-- 2 non, 6 oui→1, 1 non, 9 oui→2, 4 non (pas strictement >)
--
-- Résultat attendu : nb == 2
--
-- Indice : for _, x in ipairs(poids) do + if x > 4 then

-- À toi :
for i, x in ipairs(poids) do
    if x > 4 then
        nb = nb + 1
    end
end

-- --- Vérification (ne pas modifier) ---
assert(nb == 2, "Obtenu : " .. tostring(nb) .. ", attendu : 2")
print("✅ Correct !")
