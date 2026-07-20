-- ============================================================
-- Resident Evil — fiche de Leon
-- ============================================================
-- Le jeu stocke les infos du joueur dans une table avec des
-- clés nommées. Lis la vie, puis mets à jour le statut.
--
-- Lance : lua 02_dict.lua
-- ============================================================

joueur = {
  nom = "Leon",
  vie = 80,
  statut = "ok",
}

vie_lue = 0

-- 1) Lis la vie du joueur et stocke-la dans vie_lue.
-- 2) Change le statut du joueur en "blesse".
--
-- joueur["vie"]      →  80  →  vie_lue = 80
-- joueur["statut"] = "blesse"
--
-- Résultat attendu :
--   vie_lue == 80
--   joueur["statut"] == "blesse"
--
-- Indice : t["cle"] pour lire, t["cle"] = valeur pour écrire
--          (ou t.cle / t.cle = valeur — même chose)

-- À toi :
vie_lue = joueur.vie

joueur.statut = "blesse"

-- --- Vérification (ne pas modifier) ---
assert(vie_lue == 80, "vie_lue doit valoir 80, obtenu : " .. tostring(vie_lue))
assert(joueur["statut"] == "blesse", "statut doit être 'blesse', obtenu : '" .. tostring(joueur["statut"]) .. "'")
print("✅ Correct !")
