-- ============================================================
-- Project Zomboid — bandage
-- ============================================================
-- Une fonction calcule la vie après un soin.
--
-- Lance : lua 04_soin.lua
-- ============================================================

--   vie  : points de vie actuels
--   soin : points récupérés
--
-- soigner(40, 15) → 40 + 15 = 55
-- soigner(70, 10) → 70 + 10 = 80
--
-- Résultat attendu : soigner(40, 15) == 55  et  soigner(70, 10) == 80
--
-- Indice : function ... return ... end

function soigner(vie, soin)
    return vie + soin
end

-- --- Vérification (ne pas modifier) ---
assert(soigner(40, 15) == 55, "soigner(40, 15) doit retourner 55")
assert(soigner(70, 10) == 80, "soigner(70, 10) doit retourner 80")
print("✅ Correct !")
