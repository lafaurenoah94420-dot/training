-- ============================================================
-- Resident Evil — infection
-- ============================================================
-- L'infection monte de 25 en 25 tant qu'elle est strictement
-- sous 100. À la fin elle doit valoir 100.
--
-- Lance : lua 05_infection.lua
-- ============================================================

infection = 0

-- while infection < 100 do
--   infection = infection + 25
-- end
--
-- 0→25→50→75→100 puis stop
--
-- Résultat attendu : infection == 100
--
-- Indice : while ... do ... end

-- À toi :
while infection < 100 do
    infection = infection + 25
end

-- --- Vérification (ne pas modifier) ---
assert(infection == 100, "Obtenu : " .. tostring(infection) .. ", attendu : 100")
print("✅ Correct !")
