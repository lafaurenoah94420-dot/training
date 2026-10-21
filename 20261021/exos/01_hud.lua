-- ============================================================
-- The Last of Us — HUD
-- ============================================================
-- L'écran affiche le nom du survivant et sa vie.
-- Tu construis le message exact.
--
-- Lance : lua 01_hud.lua
-- ============================================================

nom = "Joel"
vie = 65
hud = nom .. " : " .. vie .. " PV"

-- hud = nom + " : " + vie + " PV"
-- → "Joel : 65 PV"
--
-- Résultat attendu : hud == "Joel : 65 PV"
--
-- Indice : opérateur ..

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(hud == "Joel : 65 PV", "Obtenu : '" .. tostring(hud) .. "'")
print("✅ Correct !")
