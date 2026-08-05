-- ============================================================
-- Resident Evil — tension électrique
-- ============================================================
-- La tension monte de 15 en 15 tant qu'elle est strictement
-- inférieure à 60. À la fin elle doit valoir 60.
--
-- Lance : lua 05_tension.lua
-- ============================================================

tension = 0

-- while tension < 60 do
--   tension = tension + 15
-- end
--
-- tour : 0→15, 15→30, 30→45, 45→60  puis stop
--
-- Résultat attendu : tension == 60
--
-- Indice : while ... do ... end
--          attention à ne pas faire une boucle infinie

-- À toi :
while tension < 60 do
    tension = tension + 15
end

-- --- Vérification (ne pas modifier) ---
assert(tension == 60, "Obtenu : " .. tostring(tension) .. ", attendu : 60")
print("✅ Correct !")
