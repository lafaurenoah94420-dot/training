-- ============================================================
-- Project Zomboid — panneau
-- ============================================================
-- Le panneau dit "danger bite". Tu remplaces "bite" par
-- "infecte". Il faut stocker le résultat de string.gsub.
--
-- Lance : lua 04_panneau.lua
-- ============================================================

brut = "danger bite"
propre = ""

-- Remplace "bite" par "infecte" → "danger infecte"
--
-- Résultat attendu : propre == "danger infecte"
--
-- Indice : string.gsub(brut, "bite", "infecte")
--          (2e arg = ce que tu cherches, 3e = le remplacement)

-- À toi :
propre = string.gsub(brut, "bite", "infecte")

-- --- Vérification (ne pas modifier) ---
assert(propre == "danger infecte", "Obtenu : '" .. tostring(propre) .. "'")
print("✅ Correct !")
