-- ============================================================
-- Resident Evil — kit de soin optionnel
-- ============================================================
-- soigner(vie, soin) : si soin n'est pas donné, utilise 25.
-- Retourne la nouvelle vie (sans plafond ici).
--
-- Lance : lua 05_soigner.lua
-- ============================================================

-- Écris function soigner(vie, soin)  (sans local)
--
-- soigner(40)      →  soin vaut nil  →  utilise 25  →  65
-- soigner(40, 10)  →  50
--
-- Indice : soin = soin or 25   puis   return vie + soin
--          (guillemets inutiles : 25 est un nombre)

-- À toi :
function soigner(vie, soin)
    soin = soin or 25
    return vie + soin
end

-- --- Vérification (ne pas modifier) ---
assert(type(soigner) == "function", "La fonction soigner manque")
assert(soigner(40) == 65, "soigner(40) devrait donner 65 (défaut 25)")
assert(soigner(40, 10) == 50, "soigner(40, 10) devrait donner 50")
assert(soigner(90, 0) == 90, "soigner(90, 0) : 0 n'est pas nil, garde 0 → 90")
print("✅ Correct !")
