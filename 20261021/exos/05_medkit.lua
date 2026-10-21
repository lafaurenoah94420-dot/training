-- ============================================================
-- Resident Evil — chercher un medkit
-- ============================================================
-- Leon cherche un "medkit" dans son inventaire.
-- Si il y est, trouve = true.
--
-- Lance : lua 05_medkit.lua
-- ============================================================

inventaire = { "ammo", "herb", "medkit", "clé" }
trouve = false

-- Parcours avec ipairs. Si x == "medkit", trouve = true.
--
-- Résultat attendu : trouve == true
--
-- Indice : for _, x in ipairs(inventaire) do + if x == "medkit"

-- À toi :
for i, x in ipairs(inventaire) do
    if x == "medkit" then
        trouve = true
    end
end

-- --- Vérification (ne pas modifier) ---
assert(trouve == true, "trouve devrait être true — medkit est dans l'inventaire")
print("✅ Correct !")
