-- ============================================================
-- GTA — message de score
-- ============================================================
-- Franklin finit une course. L'écran affiche son pseudo et
-- son score en une seule phrase.
--
-- Lance : lua 01_concat.lua
-- ============================================================

pseudo = "Franklin"
score = 8500
message = pseudo .. " : " .. score .. " $"

-- Colle le pseudo, le texte et le score dans message.
--
-- "Franklin" .. " : " .. 8500 .. " $"
--   →  "Franklin : 8500 $"
--
-- Résultat attendu : message == "Franklin : 8500 $"
--
-- Indice : opérateur ..

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(message == "Franklin : 8500 $", "Obtenu : '" .. message .. "'")
print("✅ Correct !")
