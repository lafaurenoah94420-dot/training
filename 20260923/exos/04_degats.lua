-- ============================================================
-- Project Zomboid — dégâts
-- ============================================================
-- Fonction qui reçoit base et bonus, retourne leur somme.
--
-- Lance : lua 04_degats.lua
-- ============================================================

-- Écris function degats(base, bonus)  (sans local)
-- Elle retourne base + bonus.
--
-- degats(28, 12) => 40
--
-- Indice : function ... return ... end

-- À toi :
function degats(base, bonus)
    return base + bonus
end
-- --- Vérification (ne pas modifier) ---
assert(type(degats) == "function", "La fonction degats manque")
assert(degats(28, 12) == 40, "degats(28, 12) devrait donner 40")
assert(degats(15, 0) == 15, "degats(15, 0) devrait donner 15")
print("✅ Correct !")
