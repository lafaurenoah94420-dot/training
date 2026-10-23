-- ============================================================
-- Hearts of Iron IV — liste des unités
-- ============================================================
-- Tu récupères toutes les clés de unites dans une liste.
--
-- Lance : lua 05_noms.lua
-- ============================================================

unites = { chars = 10, avions = 4, bateaux = 6 }
noms = {}

-- Parcours unites avec pairs.
-- À chaque tour, table.insert(noms, k)
--
-- Après : noms contient "chars", "avions", "bateaux" (ordre libre)
--
-- Résultat attendu : #noms == 3
--
-- Indice : for k, v in pairs(unites) do
--          table.insert(noms, k)

-- À toi :
for k, v in pairs(unites) do
    table.insert(noms, k)
end

-- --- Vérification (ne pas modifier) ---
assert(#noms == 3, "noms devrait avoir 3 éléments, obtenu : " .. tostring(#noms))
print("✅ Correct !")
