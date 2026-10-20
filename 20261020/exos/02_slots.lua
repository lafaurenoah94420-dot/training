-- ============================================================
-- The Last of Us — places dans le sac
-- ============================================================
-- Combien d'objets Ellie a-t-elle dans son sac ?
--
-- Lance : lua 02_slots.lua
-- ============================================================

sac = { "corde", "couteau", "briquet", "photo" }
places = # sac

-- places = nombre d'éléments dans sac → 4
--
-- Résultat attendu : places == 4
--
-- Indice : opérateur #

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(places == 4, "Obtenu : " .. tostring(places) .. ", attendu : 4")
print("✅ Correct !")
