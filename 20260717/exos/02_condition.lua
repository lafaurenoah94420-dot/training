-- ============================================================
-- Resident Evil — état de santé
-- ============================================================
-- L'écran médical de Leon change selon ses PV :
-- "Critique" en dessous de 30, "Blessé" entre 30 et 69,
-- "Stable" à 70 ou plus.
--
-- Lance : lua 02_condition.lua
-- ============================================================

vie = 45
etat = ""

-- Remplis etat selon la valeur de vie.
--
-- vie = 20  →  20 < 30 ? oui           →  etat = "Critique"
-- vie = 45  →  45 < 30 ? non, 45 < 70 ? oui  →  etat = "Blessé"
-- vie = 80  →  80 < 30 ? non, 80 < 70 ? non  →  etat = "Stable"
--
-- Résultat attendu : etat == "Blessé"  (car vie vaut 45 ici)
--
-- Indice : if / elseif / else / end

-- À toi :
if vie < 30 and vie > 0 then
    etat = "Critique"
elseif vie >= 30 and vie < 70 then
    etat = "Blessé"
else
    etat = "Stable"

end
 

-- --- Vérification (ne pas modifier) ---
assert(etat == "Blessé", "Obtenu : '" .. etat .. "' — avec vie = 45, attendu : Blessé")
print("✅ Correct !")
