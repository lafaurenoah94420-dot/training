-- ============================================================
-- GTA — message radio
-- ============================================================
-- La radio dit "wanted star". Tu remplaces "star" par "level".
-- Il faut stocker le résultat de string.gsub.
--
-- Lance : lua 04_radio.lua
-- ============================================================

brut = "wanted star"
propre = ""

-- Remplace "star" par "level" → "wanted level"
--
-- Résultat attendu : propre == "wanted level"
--
-- Indice : string.gsub(brut, "star", "level")
--          (2e arg = ce que tu cherches, 3e = le remplacement)

-- À toi :
propre = string.gsub(brut, "star", "level")

-- --- Vérification (ne pas modifier) ---
assert(propre == "wanted level", "Obtenu : '" .. tostring(propre) .. "'")
print("✅ Correct !")
