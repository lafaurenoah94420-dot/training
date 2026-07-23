-- ============================================================
-- Hearts of Iron IV — divisions prêtes
-- ============================================================
-- Compte combien de divisions ont une orga strictement
-- supérieure à 60.
--
-- Lance : lua 05_for_if.lua
-- ============================================================

orgas = {45, 72, 61, 30, 88}
pretes = 0

-- Parcours orgas. Si x > 60, ajoute 1 à pretes.
--
-- 45 > 60 ? non
-- 72 > 60 ? oui  →  pretes = 1
-- 61 > 60 ? oui  →  pretes = 2
-- 30 > 60 ? non
-- 88 > 60 ? oui  →  pretes = 3
--
-- Résultat attendu : pretes == 3
--
-- Indice : for _, x in ipairs(...) do  +  if x > 60 then
--          Compare x, pas la table entière

-- À toi :
for i, x in ipairs(orgas) do
    if x > 60 then
        pretes = pretes + 1
    end
end

-- --- Vérification (ne pas modifier) ---
assert(pretes == 3, "Obtenu : " .. pretes .. ", attendu : 3")
print("✅ Correct !")
