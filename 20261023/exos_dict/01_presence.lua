-- ============================================================
-- Resident Evil — objet présent ?
-- ============================================================
-- Tu vérifies si le sac contient une clé "herb".
-- Si oui, trouve = true.
--
-- Lance : lua 01_presence.lua
-- ============================================================

sac = { ammo = 20, herb = 1, cle = 1 }
trouve = false

-- Si sac["herb"] n'est pas nil → l'objet existe → trouve = true
--
-- Résultat attendu : trouve == true
--
-- Indice : if sac["herb"] ~= nil then

-- À toi :
if sac["herb"] ~= nil then
    trouve = true
end

-- --- Vérification (ne pas modifier) ---
assert(trouve == true, "trouve devrait être true — herb est dans le sac")
print("✅ Correct !")
