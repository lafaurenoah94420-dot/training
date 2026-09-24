-- ============================================================
-- Resident Evil — chercher une map
-- ============================================================
-- Leon cherche une "map" dans son inventaire.
-- Si elle y est, trouve = true.
--
-- Lance : lua 05_map.lua
-- ============================================================

inventaire = { "herb", "ammo", "map", "clé" }
trouve = false

-- Parcours avec ipairs. Si x == "map", trouve = true.
--
-- Résultat attendu : trouve == true
--
-- Indice : for _, x in ipairs(inventaire) do + if x == "map"

-- À toi :
for i, x in ipairs(inventaire) do
    if x == "map" then
        trouve = true
    end
end
-- --- Vérification (ne pas modifier) ---
assert(trouve == true, "trouve devrait être true — map est dans l'inventaire")
print("✅ Correct !")
