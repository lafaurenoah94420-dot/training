-- ============================================================
-- The Last of Us — porte verrouillée
-- ============================================================
-- Si Joel a la clé, le message est "Ouverte". Sinon "Fermee".
--
-- Lance : lua 02_condition.lua
-- ============================================================

a_cle = true
etat = ""

-- Remplis etat selon a_cle.
--
-- a_cle = true   →  etat = "Ouverte"
-- a_cle = false  →  etat = "Fermee"
--
-- Résultat attendu : etat == "Ouverte"  (car a_cle vaut true ici)
--
-- Indice : if / else / end

-- À toi :
if a_cle == true then
    etat = "Ouverte"
else
    etat = "Fermee"
end

-- --- Vérification (ne pas modifier) ---
assert(etat == "Ouverte", "Obtenu : '" .. etat .. "'")
print("✅ Correct !")
