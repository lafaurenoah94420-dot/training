-- ============================================================
-- Project Zomboid — censurer le chat
-- ============================================================
-- Le serveur remplace chaque "zombie" par "menace" dans les
-- messages. string.gsub renvoie le nouveau texte — il faut
-- le stocker, sinon rien ne change.
--
-- Lance : lua 04_censurer.lua
-- ============================================================

brut = "un zombie près du zombie shop"
propre = ""

-- Remplace toutes les occurrences de "zombie" par "menace"
-- et mets le résultat dans propre.
--
-- "un zombie près du zombie shop"
-- → "un menace près du menace shop"
--
-- Résultat attendu : propre == "un menace près du menace shop"
--
-- Indice : string.gsub(brut, "zombie", "menace")
--          → stocke le résultat dans propre

-- À toi :
propre = string.gsub(brut, "zombie", "menace")

-- --- Vérification (ne pas modifier) ---
assert(propre == "un menace près du menace shop",
  "Obtenu : '" .. tostring(propre) .. "'")
print("✅ Correct !")
