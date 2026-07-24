-- ============================================================
-- Project Zomboid — message d'alerte
-- ============================================================
-- L'écran affiche le lieu et le nombre de zombies en une phrase.
--
-- Lance : lua 01_concat.lua
-- ============================================================

lieu = "entrepot"
zombies = 12
message = ""

-- Colle lieu, le texte et zombies dans message.
--
-- "entrepot" .. " : " .. 12 .. " zombies"
--   →  "entrepot : 12 zombies"
--
-- Résultat attendu : message == "entrepot : 12 zombies"
--
-- Indice : opérateur ..

-- À toi :
message = lieu .. " : "  .. zombies .. " zombies"

-- --- Vérification (ne pas modifier) ---
assert(message == "entrepot : 12 zombies", "Obtenu : '" .. message .. "'")
print("✅ Correct !")
