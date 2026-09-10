-- ============================================================
-- Resident Evil — coffre ouvert ?
-- ============================================================
-- Si Leon a le code (a_code = true), etat = "ouvert".
-- Sinon etat = "verrouille".
--
-- Lance : lua 02_coffre.lua
-- ============================================================

a_code = false
etat = ""

-- a_code vaut false ici → etat = "verrouille"
--
-- Résultat attendu : etat == "verrouille"
--
-- Indice : if / else / end

-- À toi :
if a_code == false then
    etat = "verrouille"
end

-- --- Vérification (ne pas modifier) ---
assert(etat == "verrouille", "Obtenu : '" .. tostring(etat) .. "'")
print("✅ Correct !")
