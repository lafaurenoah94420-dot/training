-- ============================================================
-- GTA — plaque d'immatriculation
-- ============================================================
-- Le jeu affiche la longueur de la plaque. Combien de caractères
-- dans "LS-4821" ?
--
-- Lance : lua 02_longueur.lua
-- ============================================================

plaque = "LS-4821"
longueur = 0

-- Stocke dans longueur le nombre de caractères de plaque.
--
-- "LS-4821"  →  7 caractères
--
-- Résultat attendu : longueur == 7
--
-- Indice : opérateur #

-- À toi :
longueur = #plaque

-- --- Vérification (ne pas modifier) ---
assert(longueur == 7, "Obtenu : " .. longueur .. ", attendu : 7")
print("✅ Correct !")
