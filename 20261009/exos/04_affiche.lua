-- ============================================================
-- Project Zomboid — affiche
-- ============================================================
-- L'affiche dit "zone safe". Tu remplaces "safe" par "morte".
-- Il faut stocker le résultat de string.gsub.
--
-- Lance : lua 04_affiche.lua
-- ============================================================

brut = "zone safe"
propre = string.gsub(brut, "safe", "morte")

-- Remplace "safe" par "morte" → "zone morte"
--
-- Résultat attendu : propre == "zone morte"
--
-- Indice : string.gsub(brut, "safe", "morte")
--          (2e arg = ce que tu cherches, 3e = le remplacement)

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(propre == "zone morte", "Obtenu : '" .. tostring(propre) .. "'")
print("✅ Correct !")
