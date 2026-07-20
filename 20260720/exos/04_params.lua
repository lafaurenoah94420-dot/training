-- ============================================================
-- GTA — gain de mission
-- ============================================================
-- Franklin finit une mission. La récompense = base + bonus.
-- La fonction calcule le total.
--
-- Lance : lua 04_params.lua
-- ============================================================

--   base   : argent de base de la mission
--   bonus  : prime supplémentaire
--
-- gagner(500, 200)  →  500 + 200 = 700  →  retourne 700
-- gagner(100, 50)   →  100 + 50  = 150  →  retourne 150
--
-- Résultat attendu : gagner(500, 200) == 700  et  gagner(100, 50) == 150
--
-- Indice : function ... end  +  return  +  les deux paramètres

function gagner(base, bonus)
    return base + bonus
end


-- --- Vérification (ne pas modifier) ---
assert(gagner(500, 200) == 700, "gagner(500, 200) doit retourner 700")
assert(gagner(100, 50) == 150, "gagner(100, 50) doit retourner 150")
print("✅ Correct !")
