-- ============================================================
-- Resident Evil — coffre
-- ============================================================
-- Si Leon a la clé (a_cle = true), etat = "ouvert".
-- Sinon etat = "ferme".
--
-- Lance : lua 02_coffre.lua
-- ============================================================

a_cle = false
etat = ""

-- a_cle vaut false ici → etat = "ferme"
--
-- Résultat attendu : etat == "ferme"
--
-- Indice : if / else / end

-- À toi :
if a_cle == false then
    etat = "ferme"
else
    etat = "ouvert"
end

-- --- Vérification (ne pas modifier) ---
assert(etat == "ferme", "Obtenu : '" .. tostring(etat) .. "'")
print("✅ Correct !")
