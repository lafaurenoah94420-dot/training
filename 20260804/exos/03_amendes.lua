-- ============================================================
-- GTA — total des amendes
-- ============================================================
-- Franklin a pris plusieurs amendes. Le jeu additionne tout
-- pour afficher la dette totale.
--
-- Lance : lua 03_amendes.lua
-- ============================================================

amendes = { 120, 80, 200, 50 }
total = 0

-- Parcours amendes avec ipairs. À chaque tour, ajoute x à total.
--
-- tour 1 : 0 + 120 = 120
-- tour 2 : 120 + 80 = 200
-- tour 3 : 200 + 200 = 400
-- tour 4 : 400 + 50 = 450
--
-- Résultat attendu : total == 450
--
-- Indice : for _, x in ipairs(amendes) do
--          total = total + x   (pas total = x)

-- À toi :
for i, x in ipairs(amendes) do
    total = total + x
end
-- --- Vérification (ne pas modifier) ---
assert(total == 450, "Obtenu : " .. tostring(total) .. ", attendu : 450")
print("✅ Correct !")
