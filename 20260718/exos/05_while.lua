-- ============================================================
-- Hearts of Iron IV — organisation qui remonte
-- ============================================================
-- Une division a 20 d'orga. Elle récupère 15 par tour tant qu'elle
-- est en dessous de 80. Combien d'orga après la remontée ?
--
-- Lance : lua 05_while.lua
-- ============================================================

orga = 20

-- Tant que orga est strictement inférieur à 80, ajoute 15.
--
-- départ : orga = 20
-- tour 1 : 20 < 80 ? oui  →  orga = 20 + 15 = 35
-- tour 2 : 35 < 80 ? oui  →  orga = 35 + 15 = 50
-- tour 3 : 50 < 80 ? oui  →  orga = 50 + 15 = 65
-- tour 4 : 65 < 80 ? oui  →  orga = 65 + 15 = 80
-- tour 5 : 80 < 80 ? non  →  stop
--
-- Résultat attendu : orga == 80
--
-- Indice : while ... do ... end
--          et orga = orga + 15

-- À toi :
while orga < 80 do
    orga = orga + 15
end

-- --- Vérification (ne pas modifier) ---
assert(orga == 80, "Obtenu : " .. orga .. ", attendu : 80")
print("✅ Correct !")
