-- ============================================================
-- The Last of Us — places dans le sac
-- ============================================================
-- Le sac d'Ellie contient déjà des objets. Capacité max = 6.
-- Combien de places libres reste-t-il ?
--
-- Lance : lua 02_places.lua
-- ============================================================

sac = { "corde", "couteau", "briquet", "eau" }
capacite = 6
libres = nil

-- libres = capacite - (#sac)
-- #sac = 4  →  6 - 4 = 2
--
-- Résultat attendu : libres == 2
--
-- Indice : #sac

-- À toi :
libres = capacite - #sac

-- --- Vérification (ne pas modifier) ---
assert(libres == 2, "Obtenu : " .. tostring(libres) .. ", attendu : 2")
print("✅ Correct !")
