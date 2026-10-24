-- ============================================================
-- Hearts of Iron IV — qui a 12 usines ?
-- ============================================================
-- Tu cherches la clé dont la valeur est 12.
--
-- Lance : lua 05_chercher.lua
-- ============================================================

usines = { chars = 8, avions = 12, bateaux = 5 }
trouve = ""

-- Parcours usines avec pairs.
-- Si v == 12, trouve = k
--
-- chars=8  → non
-- avions=12 → oui → trouve = "avions"
-- bateaux=5 → non
--
-- Résultat attendu : trouve == "avions"
--
-- Indice : for k, v in pairs(usines) do + if v == 12

-- À toi :
for k, v in pairs(usines) do
    if v == 12 then
        trouve = "avions"
    end
end

-- --- Vérification (ne pas modifier) ---
assert(trouve == "avions", "Obtenu : '" .. tostring(trouve) .. "', attendu : 'avions'")
print("✅ Correct !")
