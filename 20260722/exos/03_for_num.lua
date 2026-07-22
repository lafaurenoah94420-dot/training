-- ============================================================
-- Project Zomboid — jours de survie
-- ============================================================
-- Tu comptes les jours de 1 à 7. À chaque jour, ajoute 1 au compteur.
--
-- Lance : lua 03_for_num.lua
-- ============================================================

jours = 0

-- Boucle de 1 à 7. À chaque tour, ajoute 1 à jours.
--
-- tour i = 1  →  jours = 1
-- ...
-- tour i = 7  →  jours = 7
--
-- Résultat attendu : jours == 7
--
-- Indice : for i = 1, 7 do ... end
--          et jours = jours + 1

-- À toi :
for i = 1, 7 do
    jours = jours + 1
end
-- --- Vérification (ne pas modifier) ---
assert(jours == 7, "Obtenu : " .. jours .. ", attendu : 7")
print("✅ Correct !")
