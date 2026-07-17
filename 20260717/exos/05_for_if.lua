-- ============================================================
-- Hearts of Iron IV — divisions prêtes
-- ============================================================
-- Chaque division a un niveau d'organisation. Seules celles
-- avec au moins 50 d'orga sont prêtes au combat. Combien ?
--
-- Lance : lua 05_for_if.lua
-- ============================================================

orgas = {72, 31, 55, 18, 90, 44}
pretes = 0

-- Parcours orgas. À chaque tour, si la valeur est >= 50,
-- ajoute 1 à pretes.
--
-- tour 1 : 72 >= 50 ? oui  →  pretes = 0 + 1 = 1
-- tour 2 : 31 >= 50 ? non  →  pretes reste 1
-- tour 3 : 55 >= 50 ? oui  →  pretes = 1 + 1 = 2
-- tour 4 : 18 >= 50 ? non  →  pretes reste 2
-- tour 5 : 90 >= 50 ? oui  →  pretes = 2 + 1 = 3
-- tour 6 : 44 >= 50 ? non  →  pretes reste 3
--
-- Résultat attendu : pretes == 3
--
-- Indice : for + if / end  +  pretes = pretes + 1

-- À toi :
for i, x in ipairs(orgas) do
    if x >= 50 then
        pretes = pretes + 1
    end
end


-- --- Vérification (ne pas modifier) ---
assert(pretes == 3, "Obtenu : " .. pretes .. ", attendu : 3 — compte les orgas >= 50")
print("✅ Correct !")
