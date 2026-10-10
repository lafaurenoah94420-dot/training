-- ============================================================
-- Resident Evil — fiche ennemi
-- ============================================================
-- Tu lis le type de l'ennemi, puis tu mets sa vie à 50.
--
-- Lance : lua 03_ennemi.lua
-- ============================================================

ennemi = { type = "zombie", vie = 100 }
type_lu = ennemi["type"]
ennemi["vie"] = 50
-- 1) type_lu = la valeur de la clé "type" dans ennemi → "zombie"
-- 2) mets ennemi["vie"] à 50
--
-- Résultat attendu : type_lu == "zombie"  et  ennemi["vie"] == 50
--
-- Indice : ennemi["type"]  et  ennemi["vie"] = ...

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(type_lu == "zombie", "type_lu devrait être 'zombie', obtenu : '" .. tostring(type_lu) .. "'")
assert(ennemi["vie"] == 50, "ennemi['vie'] devrait être 50, obtenu : " .. tostring(ennemi["vie"]))
print("✅ Correct !")
