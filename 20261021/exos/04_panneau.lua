-- ============================================================
-- Project Zomboid — panneau
-- ============================================================
-- Le panneau dit "ville safe". Tu remplaces "safe" par "perdue".
-- Il faut stocker le résultat de string.gsub.
--
-- Lance : lua 04_panneau.lua
-- ============================================================

brut = "ville safe"
propre = ""

-- Remplace "safe" par "perdue" → "ville perdue"
--
-- Résultat attendu : propre == "ville perdue"
--
-- Indice : string.gsub(brut, "safe", "perdue")
--          (2e arg = ce que tu cherches, 3e = le remplacement)

-- À toi :
propre = string.gsub(brut, "safe", "perdue")

-- --- Vérification (ne pas modifier) ---
assert(propre == "ville perdue", "Obtenu : '" .. tostring(propre) .. "'")
print("✅ Correct !")
