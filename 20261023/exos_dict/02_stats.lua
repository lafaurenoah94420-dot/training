-- ============================================================
-- The Last of Us — stats imbriquées
-- ============================================================
-- La vie est dans un dictionnaire à l'intérieur de joueur.
-- Tu lis joueur["stats"]["vie"].
--
-- Lance : lua 02_stats.lua
-- ============================================================

joueur = {
    nom = "Ellie",
    stats = { vie = 80, stamina = 50 }
}
vie_lue = joueur["stats"]["vie"]
-- vie_lue = joueur["stats"]["vie"] → 80
--
-- Résultat attendu : vie_lue == 80
--
-- Indice : joueur["stats"]["vie"]

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(vie_lue == 80, "Obtenu : " .. tostring(vie_lue) .. ", attendu : 80")
print("✅ Correct !")
