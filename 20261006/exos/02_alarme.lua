-- ============================================================
-- Resident Evil — alarme
-- ============================================================
-- Si l'intrusion est vraie (intrusion = true), alarme = "on".
-- Sinon alarme = "off".
--
-- Lance : lua 02_alarme.lua
-- ============================================================

intrusion = true
alarme = ""

-- intrusion vaut true ici → alarme = "on"
--
-- Résultat attendu : alarme == "on"
--
-- Indice : if / else / end

-- À toi :
if intrusion == true then
    alarme = "on"
else
    alarme = "off"
end

-- --- Vérification (ne pas modifier) ---
assert(alarme == "on", "Obtenu : '" .. tostring(alarme) .. "'")
print("✅ Correct !")
