-- ============================================================
-- Project Zomboid — soin
-- ============================================================
-- Fonction qui reçoit vie et soin, retourne leur somme.
--
-- Lance : lua 04_soin.lua
-- ============================================================

-- Écris function soigner(vie, soin)  (sans local)
-- Elle retourne vie + soin.
--
-- soigner(60, 25) => 85
--
-- Indice : function ... return ... end

-- À toi :
function soigner(vie, soin)
    return vie + soin
end

-- --- Vérification (ne pas modifier) ---
assert(type(soigner) == "function", "La fonction soigner manque")
assert(soigner(60, 25) == 85, "soigner(60, 25) devrait donner 85")
assert(soigner(40, 0) == 40, "soigner(40, 0) devrait donner 40")
print("✅ Correct !")
