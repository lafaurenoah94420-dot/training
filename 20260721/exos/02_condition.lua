-- ============================================================
-- Project Zomboid — alerte faim
-- ============================================================
-- Si la faim est à 70 ou plus, le jeu affiche "Affame".
-- Sinon, "Ok".
--
-- Lance : lua 02_condition.lua
-- ============================================================

faim = 75
alerte = ""

-- Remplis alerte selon la valeur de faim.
--
-- faim = 75  →  75 >= 70 ? oui  →  alerte = "Affame"
-- faim = 40  →  40 >= 70 ? non  →  alerte = "Ok"
--
-- Résultat attendu : alerte == "Affame"  (car faim vaut 75 ici)
--
-- Indice : if / else / end

-- À toi :
if faim >= 70 then
    alerte = "Affame"
else
    alerte = "Ok"
end

-- --- Vérification (ne pas modifier) ---
assert(alerte == "Affame", "Obtenu : '" .. alerte .. "' — avec faim = 75, attendu : Affame")
print("✅ Correct !")
