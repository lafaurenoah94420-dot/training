-- ============================================================
-- Resident Evil — charge batterie
-- ============================================================
-- La batterie monte de 20 en 20 tant qu'elle est strictement
-- sous 80. À la fin elle doit valoir 80.
--
-- Lance : lua 05_batterie.lua
-- ============================================================

charge = 0

while charge < 80 do
   charge = charge + 20
end
--
-- 0→20→40→60→80 puis stop
--
-- Résultat attendu : charge == 80
--
-- Indice : while ... do ... end

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(charge == 80, "Obtenu : " .. tostring(charge) .. ", attendu : 80")
print("✅ Correct !")
