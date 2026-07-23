-- ============================================================
-- Resident Evil — fiche inventaire
-- ============================================================
-- Lis la quantité d'herbes, puis change le statut du sac.
--
-- Lance : lua 02_dict.lua
-- ============================================================

sac = {
  herbes = 3,
  statut = "leger",
}

herbes_lues = 0

-- 1) Lis sac["herbes"] (ou sac.herbes) → herbes_lues
-- 2) Écris sac["statut"] = "lourd"
--
-- Résultat attendu :
--   herbes_lues == 3
--   sac["statut"] == "lourd"
--
-- Indice : t.cle pour lire, t.cle = valeur pour écrire

-- À toi :
herbes_lues = sac.herbes
sac.statut = "lourd"

-- --- Vérification (ne pas modifier) ---
assert(herbes_lues == 3, "herbes_lues doit valoir 3")
assert(sac["statut"] == "lourd", "statut doit être 'lourd'")
print("✅ Correct !")
