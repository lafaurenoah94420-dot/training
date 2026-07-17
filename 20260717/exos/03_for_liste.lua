-- ============================================================
-- GTA — butin de braquage
-- ============================================================
-- Franklin vient de finir un braquage. Chaque sac contient une
-- somme. Le jeu doit additionner tout le butin.
--
-- Lance : lua 03_for_liste.lua
-- ============================================================

sacs = {1200, 800, 450, 2100}
total = 0

-- Parcours la table sacs et additionne chaque valeur dans total.
--
-- tour 1 : x = 1200  →  total = 0 + 1200 = 1200
-- tour 2 : x = 800   →  total = 1200 + 800 = 2000
-- tour 3 : x = 450   →  total = 2000 + 450 = 2450
-- tour 4 : x = 2100  →  total = 2450 + 2100 = 4550
--
-- Résultat attendu : total == 4550
--
-- Indice : for _, x in ipairs(...) do ... end
--          et total = total + x  (pas de += en Lua)

-- À toi :
for i, x in ipairs(sacs) do
    total = total + x
end

-- --- Vérification (ne pas modifier) ---
assert(total == 4550, "Obtenu : " .. total .. ", attendu : 4550")
print("✅ Correct !")
