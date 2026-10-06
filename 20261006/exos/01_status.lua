-- ============================================================
-- The Last of Us — status radio
-- ============================================================
-- L'écran affiche le nom du survivant et sa vie.
-- Tu construis le message exact.
--
-- Lance : lua 01_status.lua
-- ============================================================

nom = "Ellie"
vie = 80
status = nom .. " : " .. vie .. " PV"

-- status = nom + " : " + vie + " PV"
-- → "Ellie : 80 PV"
--
-- Résultat attendu : status == "Ellie : 80 PV"
--
-- Indice : opérateur ..

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(status == "Ellie : 80 PV", "Obtenu : '" .. tostring(status) .. "'")
print("✅ Correct !")
