-- ============================================================
-- Resident Evil — fiche zombie
-- ============================================================
-- Le carnet de Leon a une fiche. Tu lis le type, puis tu
-- mets le niveau à 2.
--
-- Lance : lua 03_fiche.lua
-- ============================================================

fiche = { type = "zombie", niveau = 1 }
type_lu = "zombie"
fiche["niveau"] = 2
-- 1) type_lu = la valeur de la clé "type" dans fiche → "zombie"
-- 2) mets fiche["niveau"] à 2
--
-- Résultat attendu : type_lu == "zombie"  et  fiche["niveau"] == 2
--
-- Indice : fiche["type"]  et  fiche["niveau"] = ...

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(type_lu == "zombie", "type_lu devrait être 'zombie', obtenu : '" .. tostring(type_lu) .. "'")
assert(fiche["niveau"] == 2, "fiche['niveau'] devrait être 2, obtenu : " .. tostring(fiche["niveau"]))
print("✅ Correct !")
