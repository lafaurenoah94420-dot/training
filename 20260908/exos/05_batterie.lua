-- ============================================================
-- Resident Evil — charge batterie
-- ============================================================
-- La batterie monte de 20 en 20 tant qu'elle est strictement
-- sous 100. À la fin elle doit valoir 100.
--
-- Lance : lua 05_batterie.lua
-- ============================================================

charge = 0

-- while charge < 100 do
--   charge = charge + 20
-- end
--
-- 0→20→40→60→80→100 puis stop
--
-- Résultat attendu : charge == 100
--
-- Indice : while ... do ... end

-- À toi :
while charge < 100 do
    charge = charge + 20
end

-- --- Vérification (ne pas modifier) ---
assert(charge == 100, "Obtenu : " .. tostring(charge) .. ", attendu : 100")
print("✅ Correct !")
