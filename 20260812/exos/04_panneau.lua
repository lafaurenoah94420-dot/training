-- ============================================================
-- Project Zomboid — corriger le panneau
-- ============================================================
-- Un panneau dit "DANGER zombie". Tu remplaces "zombie" par
-- "infecté". Il faut stocker le résultat de string.gsub.
--
-- Lance : lua 04_panneau.lua
-- ============================================================

brut = "DANGER zombie"
propre = ""

-- Remplace "zombie" par "infecté" → "DANGER infecté"
--
-- Résultat attendu : propre == "DANGER infecté"
--
-- Indice : string.gsub(brut, "zombie", "infecté")

-- À toi :
propre = string.gsub(brut, "zombie", "infecté")

-- --- Vérification (ne pas modifier) ---
assert(propre == "DANGER infecté", "Obtenu : '" .. tostring(propre) .. "'")
print("✅ Correct !")
