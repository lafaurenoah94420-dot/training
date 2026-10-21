-- ============================================================
-- Resident Evil — niveau d'alerte
-- ============================================================
-- Le système d'alerte est à 1. Tu le passes à 3.
--
-- Lance : lua 02_ecrire.lua
-- ============================================================

systeme = { alerte = 1, zone = "labo" }

-- Mets systeme["alerte"] à 3
--
-- Résultat attendu : systeme["alerte"] == 3
--
-- Indice : systeme["alerte"] = ...

-- À toi :
systeme["alerte"] = 3

-- --- Vérification (ne pas modifier) ---
assert(systeme["alerte"] == 3, "systeme['alerte'] devrait être 3, obtenu : " .. tostring(systeme["alerte"]))
print("✅ Correct !")
