-- Exercice 5 — Boucle while (Resident Evil)
--
-- L'infection monte de 10 en 10 tant qu'elle est sous 100.
-- Utilise while. À la fin, infection doit valoir 100.

local infection = 0

-- TODO : while infection < 100 do
--   infection = infection + 10
-- end
while infection < 100 do
    infection = infection + 10
end
-- --- Vérification ---
assert(infection == 100, "Attendu : 100, obtenu : " .. tostring(infection))
print("05_infection OK")
