-- ============================================================
-- Resident Evil — chercher une carte
-- ============================================================
-- Leon fouille son inventaire pour la "carte".
-- Si elle y est, trouve = true.
--
-- Lance : lua 05_carte.lua
-- ============================================================

inventaire = { "herb", "ammo", "carte", "clé" }
trouve = false

-- Parcours avec ipairs. Si x == "carte", trouve = true.
--
-- Résultat attendu : trouve == true
--
-- Indice : for _, x in ipairs(inventaire) do + if x == "carte"

-- À toi :
for _, x in ipairs(inventaire) do
    if x == "carte" then
        trouve = true
    end
end
-- --- Vérification (ne pas modifier) ---
assert(trouve == true, "trouve devrait être true — la carte est dans l'inventaire")
print("✅ Correct !")
