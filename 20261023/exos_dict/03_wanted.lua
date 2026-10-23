-- ============================================================
-- GTA — niveau wanted
-- ============================================================
-- Si joueur["etoiles"] >= 3, tu mets joueur["statut"] = "recherché".
-- Sinon joueur["statut"] = "discret".
--
-- Lance : lua 03_wanted.lua
-- ============================================================

joueur = { nom = "Franklin", etoiles = 4, statut = "" }

-- etoiles vaut 4 → 4 >= 3 ? oui → statut = "recherché"
--
-- Résultat attendu : joueur["statut"] == "recherché"
--
-- Indice : if joueur["etoiles"] >= 3 then
--          joueur["statut"] = ...

-- À toi :
if joueur["etoiles"] >= 3 then
    joueur["statut"] = "recherché"
end

-- --- Vérification (ne pas modifier) ---
assert(joueur["statut"] == "recherché", "Obtenu : '" .. tostring(joueur["statut"]) .. "'")
print("✅ Correct !")
