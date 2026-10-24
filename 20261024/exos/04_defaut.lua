-- ============================================================
-- Resident Evil — kit manquant
-- ============================================================
-- Tu lis le nombre de kits. S'il n'y en a pas (nil), tu prends 0.
--
-- Lance : lua 04_defaut.lua
-- ============================================================

inventaire = { ammo = 30, herb = 2 }
kits = inventaire["kit"] or 0

-- inventaire["kit"] n'existe pas → nil
-- kits = inventaire["kit"] or 0  → 0
--
-- Résultat attendu : kits == 0
--
-- Indice : inventaire["kit"] or 0
--          (si la gauche est nil, Lua prend la droite)

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(kits == 0, "Obtenu : " .. tostring(kits) .. ", attendu : 0")
print("✅ Correct !")
