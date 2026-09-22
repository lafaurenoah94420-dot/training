-- ============================================================
-- The Last of Us — places libres
-- ============================================================
-- Le sac d'Ellie a une capacité max de 7. Tu comptes combien
-- d'objets elle porte, puis les places libres.
--
-- Lance : lua 02_places.lua
-- ============================================================

sac = { "corde", "couteau", "briquet", "eau", "bandage" }
capacite = 7
libres = capacite - (#sac)

-- libres = capacite - (#sac)
-- #sac = 5  →  7 - 5 = 2
--
-- Résultat attendu : libres == 2
--
-- Indice : #sac

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(libres == 2, "Obtenu : " .. tostring(libres) .. ", attendu : 2")
print("✅ Correct !")
