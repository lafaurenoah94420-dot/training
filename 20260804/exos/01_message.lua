-- ============================================================
-- The Last of Us — message HUD
-- ============================================================
-- L'écran affiche le nom du joueur et sa vie restante après un
-- combat. Tu dois construire le texte exact attendu par le HUD.
--
-- Lance : lua 01_message.lua
-- ============================================================

nom = "Ellie"
vie = 47
message = ""

-- Construis message ainsi :
--   "Ellie" + " : " + 47 + " PV"
-- → "Ellie : 47 PV"
--
-- Attention : la vie est un nombre — Lua le convertit avec ..
--
-- Résultat attendu : message == "Ellie : 47 PV"
--
-- Indice : opérateur ..

-- À toi :
message = nom .. " : " .. vie .. " PV"

-- --- Vérification (ne pas modifier) ---
assert(message == "Ellie : 47 PV", "Obtenu : '" .. tostring(message) .. "'")
print("✅ Correct !")
