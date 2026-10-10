-- ============================================================
-- The Last of Us — coup
-- ============================================================
-- Une fonction calcule les PV restants après un coup.
--
-- Lance : lua 04_degats.lua
-- ============================================================

--   vie    : points de vie actuels
--   degats : points perdus
--
-- frapper(80, 25) → 80 - 25 = 55
-- frapper(40, 10) → 40 - 10 = 30
--
-- Résultat attendu : frapper(80, 25) == 55  et  frapper(40, 10) == 30
--
-- Indice : function ... return ... end

function frapper(vie, degats)
    return vie - degats
end

-- --- Vérification (ne pas modifier) ---
assert(frapper(80, 25) == 55, "frapper(80, 25) doit retourner 55")
assert(frapper(40, 10) == 30, "frapper(40, 10) doit retourner 30")
print("✅ Correct !")
