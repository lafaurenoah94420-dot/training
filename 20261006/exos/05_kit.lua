-- ============================================================
-- Resident Evil — chercher un kit
-- ============================================================
-- Leon cherche un "kit" dans son sac.
-- Si il y est, trouve = true.
--
-- Lance : lua 05_kit.lua
-- ============================================================

sac = { "ammo", "herb", "kit", "clé" }
trouve = false

-- Parcours avec ipairs. Si x == "kit", trouve = true.
--
-- Résultat attendu : trouve == true
--
-- Indice : for _, x in ipairs(sac) do + if x == "kit"

-- À toi :
for i, x in ipairs(sac) do
    if x == "kit" then
        trouve = true
    end
end
-- --- Vérification (ne pas modifier) ---
assert(trouve == true, "trouve devrait être true — kit est dans le sac")
print("✅ Correct !")
