-- ============================================================
-- Project Zomboid — panneau d'alerte
-- ============================================================
-- Le panneau dit "alerte horde". Tu remplaces "horde" par
-- "menace". Il faut stocker le résultat de string.gsub.
--
-- Lance : lua 04_panneau.lua
-- ============================================================

brut = "alerte horde"
propre = string.gsub(brut, "horde", "menace")

-- Remplace "horde" par "menace" → "alerte menace"
--
-- Résultat attendu : propre == "alerte menace"
--
-- Indice : string.gsub(brut, "horde", "menace")
--          (2e arg = ce que tu cherches, 3e = le remplacement)

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(propre == "alerte menace", "Obtenu : '" .. tostring(propre) .. "'")
print("✅ Correct !")
