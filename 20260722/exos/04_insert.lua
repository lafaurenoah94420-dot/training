-- ============================================================
-- The Last of Us — sac de Joel
-- ============================================================
-- Joel ramasse 3 objets et les ajoute à son sac, dans l'ordre.
--
-- Lance : lua 04_insert.lua
-- ============================================================

sac = {}

-- Ajoute dans sac, dans cet ordre : "corde", "briquet", "kit"
--
-- Résultat attendu :
--   #sac == 3
--   sac[1] == "corde"
--   sac[2] == "briquet"
--   sac[3] == "kit"
--
-- Indice : table.insert(sac, "...")

-- À toi :
table.insert(sac, "corde")
table.insert(sac, "briquet")
table.insert(sac, "kit")
-- --- Vérification (ne pas modifier) ---
assert(#sac == 3, "Obtenu " .. #sac .. " objets, attendu : 3")
assert(sac[1] == "corde", "sac[1] doit être 'corde'")
assert(sac[2] == "briquet", "sac[2] doit être 'briquet'")
assert(sac[3] == "kit", "sac[3] doit être 'kit'")
print("✅ Correct !")
