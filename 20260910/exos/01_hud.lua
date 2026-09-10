-- ============================================================
-- The Last of Us — statut HUD
-- ============================================================
-- L'écran affiche le nom du joueur et ses PV. Tu construis
-- le texte exact attendu.
--
-- Lance : lua 01_hud.lua
-- ============================================================

nom = "Joel"
vie = 72
hud = ""

-- hud = nom + " - " + vie + " PV"
-- → "Joel - 72 PV"
--
-- Résultat attendu : hud == "Joel - 72 PV"
--
-- Indice : opérateur ..

-- À toi :
hud = nom .. " - " .. vie .. " PV"

-- --- Vérification (ne pas modifier) ---
assert(hud == "Joel - 72 PV", "Obtenu : '" .. tostring(hud) .. "'")
print("✅ Correct !")
