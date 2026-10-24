-- ============================================================
-- The Last of Us — soigner les stats
-- ============================================================
-- Tu écris dans le dictionnaire imbriqué : tu mets la vie à 100.
--
-- Lance : lua 03_imbrique.lua
-- ============================================================

joueur = {
    nom = "Joel",
    stats = { vie = 40, stamina = 60 }
}

-- Mets joueur["stats"]["vie"] à 100
--
-- Résultat attendu : joueur["stats"]["vie"] == 100
--
-- Indice : joueur["stats"]["vie"] = 100

-- À toi :
joueur["stats"]["vie"] = 100

-- --- Vérification (ne pas modifier) ---
assert(joueur["stats"]["vie"] == 100, "Obtenu : " .. tostring(joueur["stats"]["vie"]))
assert(joueur["stats"]["stamina"] == 60, "ne touche pas stamina")
print("✅ Correct !")
