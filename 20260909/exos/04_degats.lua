-- ============================================================
-- Project Zomboid — dégâts d'arme
-- ============================================================
-- Fonction qui reçoit puissance et bonus, retourne leur somme.
--
-- Lance : lua 04_degats.lua
-- ============================================================

-- Écris function degats(puissance, bonus)  (sans local)
-- Elle retourne puissance + bonus.
--
-- degats(35, 10) => 45
--
-- Indice : function ... return ... end

-- À toi :
function degats(puissance, bonus)
    return puissance + bonus
end

-- --- Vérification (ne pas modifier) ---
assert(type(degats) == "function", "La fonction degats manque")
assert(degats(35, 10) == 45, "degats(35, 10) devrait donner 45")
assert(degats(20, 0) == 20, "degats(20, 0) devrait donner 20")
print("✅ Correct !")
