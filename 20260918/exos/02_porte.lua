-- ============================================================
-- Resident Evil — porte du labo
-- ============================================================
-- Si Leon a le badge (a_badge = true), statut = "acces".
-- Sinon statut = "refuse".
--
-- Lance : lua 02_porte.lua
-- ============================================================

a_badge = true
statut = ""

-- a_badge vaut true ici → statut = "acces"
--
-- Résultat attendu : statut == "acces"
--
-- Indice : if / else / end

-- À toi :
if a_badge == true then
    statut = "acces"
end

-- --- Vérification (ne pas modifier) ---
assert(statut == "acces", "Obtenu : '" .. tostring(statut) .. "'")
print("✅ Correct !")
