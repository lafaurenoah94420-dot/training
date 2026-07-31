-- ============================================================
-- GTA — dégâts
-- ============================================================
-- Fonction qui additionne base + bonus.
--
-- Lance : lua 03_degats.lua
-- ============================================================

-- Écris function degats(base, bonus) qui retourne base + bonus.
-- (sans local devant function)
--
-- degats(30, 10) => 40
--
-- Indice : function ... return ... end

-- À toi :
function degats(base, bonus)
    return base + bonus
end

-- --- Vérification (ne pas modifier) ---
assert(type(degats) == "function", "La fonction degats manque")
assert(degats(30, 10) == 40, "degats(30, 10) devrait donner 40")
assert(degats(5, 5) == 10, "degats(5, 5) devrait donner 10")
print("✅ Correct !")
