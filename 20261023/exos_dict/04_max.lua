-- ============================================================
-- Project Zomboid — meilleur loot
-- ============================================================
-- Tu trouves la plus grande valeur dans loot.
--
-- Lance : lua 04_max.lua
-- ============================================================

loot = { conserve = 3, eau = 7, bois = 2, metal = 5 }
meilleur = 0

-- Parcours loot avec pairs.
-- Si v > meilleur, meilleur = v
--
-- conserve=3 → meilleur 3
-- eau=7     → meilleur 7
-- bois=2    → (2 < 7, inchangé)
-- métal=5   → (5 < 7, inchangé)
--
-- Résultat attendu : meilleur == 7
--
-- Indice : for k, v in pairs(loot) do + if v > meilleur

-- À toi :
for k, v in pairs(loot) do
    if v > meilleur then
        meilleur = v
    end
end

-- --- Vérification (ne pas modifier) ---
assert(meilleur == 7, "Obtenu : " .. tostring(meilleur) .. ", attendu : 7")
print("✅ Correct !")
