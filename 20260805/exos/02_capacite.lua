-- ============================================================
-- The Last of Us — inventaire plein ?
-- ============================================================
-- Le sac d'Ellie a une capacité max. Tu comptes combien d'objets
-- elle porte déjà avec #.
--
-- Lance : lua 02_capacite.lua
-- ============================================================

sac = { "corde", "couteau", "briquet", "bandage", "eau" }
capacite_max = 8
places_libres = nil

-- places_libres = capacite_max - (nombre d'objets dans sac)
-- #sac = 5  →  8 - 5 = 3
--
-- Résultat attendu : places_libres == 3
--
-- Indice : #sac

-- À toi :
places_libres = capacite_max - #sac

-- --- Vérification (ne pas modifier) ---
assert(places_libres == 3, "Obtenu : " .. tostring(places_libres) .. ", attendu : 3")
print("✅ Correct !")
