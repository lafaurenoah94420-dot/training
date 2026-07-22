-- ============================================================
-- Hearts of Iron IV — moral qui remonte
-- ============================================================
-- Le moral d'une division part à 10. Tant qu'il est strictement
-- inférieur à 50, il gagne 10. Quelle valeur finale ?
--
-- Lance : lua 05_while.lua
-- ============================================================

moral = 10

-- Tant que moral < 50, ajoute 10.
--
-- 10 → 20 → 30 → 40 → 50  puis stop (50 < 50 ? non)
--
-- Résultat attendu : moral == 50
--
-- Indice : while ... do ... end
--          et moral = moral + 10

-- À toi :
while moral < 50 do
    moral = moral + 10
end
-- --- Vérification (ne pas modifier) ---
assert(moral == 50, "Obtenu : " .. moral .. ", attendu : 50")
print("✅ Correct !")
