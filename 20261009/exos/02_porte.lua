-- ============================================================
-- Resident Evil — porte blindée
-- ============================================================
-- Si Leon a le badge (a_badge = true), etat = "ouverte".
-- Sinon etat = "fermee".
--
-- Lance : lua 02_porte.lua
-- ============================================================

a_badge = true
etat = ""

-- a_badge vaut true ici → etat = "ouverte"
--
-- Résultat attendu : etat == "ouverte"
--
-- Indice : if / else / end

-- À toi :
if a_badge == true then
    etat = "ouverte"
else
    etat = "fermee"
end

-- --- Vérification (ne pas modifier) ---
assert(etat == "ouverte", "Obtenu : '" .. tostring(etat) .. "'")
print("✅ Correct !")
