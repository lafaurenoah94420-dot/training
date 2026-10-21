-- ============================================================
-- Project Zomboid — statut joueur
-- ============================================================
-- Si la vie du joueur est > 0, statut = "vivant".
-- Sinon statut = "mort".
--
-- Lance : lua 04_statut.lua
-- ============================================================

joueur = { nom = "Kate", vie = 40 }
statut = ""

-- joueur["vie"] vaut 40 ici → 40 > 0 ? oui → statut = "vivant"
--
-- Résultat attendu : statut == "vivant"
--
-- Indice : if joueur["vie"] > 0 then ... else ... end

-- À toi :
if joueur["vie"] > 0 then
    statut = "vivant"
else
    statut = "mort"
end

-- --- Vérification (ne pas modifier) ---
assert(statut == "vivant", "Obtenu : '" .. tostring(statut) .. "'")
print("✅ Correct !")
