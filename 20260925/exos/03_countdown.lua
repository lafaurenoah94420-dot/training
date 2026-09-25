-- ============================================================
-- GTA — compte à rebours braquage
-- ============================================================
-- Avant le braquage, Franklin compte jusqu'à 3.
-- Affiche "Go 1", "Go 2", "Go 3" (un print par tour).
--
-- Lance : lua 03_countdown.lua
-- ============================================================

-- Boucle for numérique de 1 à 3.
-- À chaque tour, print("Go " .. i)
--
-- tour 1 : i = 1 → affiche Go 1
-- tour 2 : i = 2 → affiche Go 2
-- tour 3 : i = 3 → affiche Go 3
--
-- Résultat attendu : 3 lignes affichées
--
-- Indice : for i = 1, 3 do ... end

-- À toi :
for i = 1, 3 do
    print("Go " .. i)
end

-- --- Vérification (ne pas modifier) ---
print("✅ Correct !")
