-- ============================================================
-- Resident Evil — porte verrouillée
-- ============================================================
-- Si Leon a la clé (a_cle = true), message = "ouverte".
-- Sinon message = "fermee".
--
-- Lance : lua 02_porte.lua
-- ============================================================

a_cle = true
message = ""

-- a_cle vaut true ici → message = "ouverte"
--
-- Résultat attendu : message == "ouverte"
--
-- Indice : if / else / end   (compare avec == si tu testes une valeur)

-- À toi :
if a_cle == true then
    message = "ouverte"
end

-- --- Vérification (ne pas modifier) ---
assert(message == "ouverte", "Obtenu : '" .. tostring(message) .. "'")
print("✅ Correct !")
