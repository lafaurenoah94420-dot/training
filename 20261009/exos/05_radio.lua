-- ============================================================
-- Hearts of Iron IV — chercher une radio
-- ============================================================
-- Tu cherches une "radio" dans le convoi.
-- Si elle y est, trouve = true.
--
-- Lance : lua 05_radio.lua
-- ============================================================

convoi = { "chars", "fuel", "radio", "munitions" }
trouve = false

-- Parcours avec ipairs. Si x == "radio", trouve = true.
--
-- Résultat attendu : trouve == true
--
-- Indice : for _, x in ipairs(convoi) do + if x == "radio"

-- À toi :
for i, x in ipairs(convoi) do
    if x == "radio" then
        trouve = true
    end
end
-- --- Vérification (ne pas modifier) ---
assert(trouve == true, "trouve devrait être true — radio est dans le convoi")
print("✅ Correct !")
