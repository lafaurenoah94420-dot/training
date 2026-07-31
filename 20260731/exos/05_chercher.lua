-- ============================================================
-- Resident Evil — inventaire
-- ============================================================
-- Cherche si "herb" est dans la liste. Si oui, trouve = true.
--
-- Lance : lua 05_chercher.lua
-- ============================================================

inventaire = { "ammo", "herb", "map" }
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
assert(trouve == true, "trouve devrait être true")
print("✅ Correct !")
