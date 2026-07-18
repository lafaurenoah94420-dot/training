-- ============================================================
-- The Last of Us — longueur du code radio
-- ============================================================
-- Joel doit entrer un code radio. L'interface affiche combien
-- de caractères contient le code avant de valider.
--
-- Lance : lua 02_longueur.lua
-- ============================================================

code = "FREQ-441"
longueur = #code

-- Stocke dans longueur le nombre de caractères de code.
--
-- "FREQ-441"  →  F R E Q - 4 4 1  →  8 caractères
--
-- Résultat attendu : longueur == 8
--
-- Indice : opérateur #  (ex. #texte)

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(longueur == 8, "Obtenu : " .. longueur .. ", attendu : 8")
print("✅ Correct !")
