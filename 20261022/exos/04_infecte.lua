-- ============================================================
-- Project Zomboid — infection
-- ============================================================
-- Si infection["niveau"] >= 50, etat = "critique".
-- Sinon etat = "stable".
--
-- Lance : lua 04_infecte.lua
-- ============================================================

infection = { niveau = 72, zone = "bras" }
etat = ""

-- infection["niveau"] vaut 72 → 72 >= 50 ? oui → etat = "critique"
--
-- Résultat attendu : etat == "critique"
--
-- Indice : if infection["niveau"] >= 50 then ... else ... end

-- À toi :
if infection["niveau"] >= 50 then
    etat = "critique"
else
    etat = "stable"
end
-- --- Vérification (ne pas modifier) ---
assert(etat == "critique", "Obtenu : '" .. tostring(etat) .. "'")
print("✅ Correct !")
