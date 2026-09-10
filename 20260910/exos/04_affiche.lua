-- ============================================================
-- Project Zomboid — corriger l'affiche
-- ============================================================
-- L'affiche dit "zone zombie". Tu remplaces "zombie" par
-- "contaminee". Il faut stocker le résultat de string.gsub.
--
-- Lance : lua 04_affiche.lua
-- ============================================================

brut = "zone zombie"
propre = ""

-- Remplace "zombie" par "contaminee" → "zone contaminee"
--
-- Résultat attendu : propre == "zone contaminee"
--
-- Indice : string.gsub(brut, "zombie", "contaminee")
--          (2e arg = ce que tu cherches, 3e = le remplacement)

-- À toi :
propre = string.gsub(brut, "zombie", "contaminee")

-- --- Vérification (ne pas modifier) ---
assert(propre == "zone contaminee", "Obtenu : '" .. tostring(propre) .. "'")
print("✅ Correct !")
