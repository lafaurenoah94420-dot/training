-- ============================================================
-- Project Zomboid — dégâts d'arme
-- ============================================================
-- Une arme inflige des dégâts de base, multipliés par un
-- modificateur (tête = 2, corps = 1). La fonction calcule le total.
--
-- Lance : lua 04_fonction.lua
-- ============================================================

--   base   : dégâts de base de l'arme
--   multi  : multiplicateur (tête, corps…)
--
-- degats(15, 2)  →  15 * 2 = 30  →  retourne 30
-- degats(20, 1)  →  20 * 1 = 20  →  retourne 20
--
-- Résultat attendu : degats(15, 2) == 30  et  degats(20, 1) == 20
--
-- Indice : function ... end  +  return

function degats(base, multi)
    total = base * multi
    return total
end


-- --- Vérification (ne pas modifier) ---
assert(degats(15, 2) == 30, "degats(15, 2) doit retourner 30")
assert(degats(20, 1) == 20, "degats(20, 1) doit retourner 20")
print("✅ Correct !")
