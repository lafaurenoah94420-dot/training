-- ============================================================
-- Resident Evil — inventaire
-- ============================================================
-- Leon cherche une "herb" dans son inventaire.
-- Si elle y est, trouve = true.
--
-- Lance : lua 05_chercher.lua
-- ============================================================

inventaire = { "ammo", "map", "herb", "clé" }
trouve = false

-- Parcours avec ipairs. Si x == "herb", trouve = true.
--
-- Résultat attendu : trouve == true
--
-- Indice : for _, x in ipairs(inventaire) do + if x == "herb"

-- À toi :
for i, x in ipairs(inventaire) do
    if x == "herb" then
        trouve = true
    end
end
-- --- Vérification (ne pas modifier) ---
assert(trouve == true, "trouve devrait être true — herb est dans l'inventaire")
print("✅ Correct !")
