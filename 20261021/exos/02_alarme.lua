-- ============================================================
-- Resident Evil — alarme labo
-- ============================================================
-- Si l'intrusion est vraie (intrusion = true), alarme = "active".
-- Sinon alarme = "off".
--
-- Lance : lua 02_alarme.lua
-- ============================================================

intrusion = false
alarme = ""

-- intrusion vaut false ici → alarme = "off"
--
-- Résultat attendu : alarme == "off"
--
-- Indice : if / else / end

-- À toi :
if intrusion == false then
    alarme = "off"
else
    alarme = "true"
end
-- --- Vérification (ne pas modifier) ---
assert(alarme == "off", "Obtenu : '" .. tostring(alarme) .. "'")
print("✅ Correct !")
