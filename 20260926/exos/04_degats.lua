-- ============================================================
-- Project Zomboid — dégâts
-- ============================================================
-- Une fonction calcule les PV restants après un coup.
--
-- Lance : lua 04_degats.lua
-- ============================================================

--   vie    : points de vie actuels
--   degats : points perdus
--
-- frapper(50, 20) → 50 - 20 = 30
-- frapper(10, 3)  → 10 - 3  = 7
--
-- Résultat attendu : frapper(50, 20) == 30  et  frapper(10, 3) == 7
--
-- Indice : function ... return ... end

function frapper(vie, degats)
        return vie - degats
end

-- --- Vérification (ne pas modifier) ---
assert(frapper(50, 20) == 30, "frapper(50, 20) doit retourner 30")
assert(frapper(10, 3) == 7, "frapper(10, 3) doit retourner 7")
print("✅ Correct !")
