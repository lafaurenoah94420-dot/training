-- ============================================================
-- Project Zomboid — kit de soin
-- ============================================================
-- Si joueur["vie"] < 50, tu lui ajoutes 20 de vie.
-- Sinon tu ne changes rien.
--
-- Lance : lua 04_soin.lua
-- ============================================================

joueur = { nom = "Kate", vie = 30 }

-- joueur["vie"] vaut 30 → 30 < 50 ? oui → vie = 30 + 20 = 50
--
-- Résultat attendu : joueur["vie"] == 50
--
-- Indice : if joueur["vie"] < 50 then
--          joueur["vie"] = joueur["vie"] + 20

-- À toi :
if joueur["vie"] < 50 then
    joueur["vie"] = joueur["vie"] + 20
end
-- --- Vérification (ne pas modifier) ---
assert(joueur["vie"] == 50, "Obtenu : " .. tostring(joueur["vie"]) .. ", attendu : 50")
print("✅ Correct !")
