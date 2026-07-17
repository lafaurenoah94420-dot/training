-- ============================================================
-- The Last of Us — message de statut
-- ============================================================
-- L'interface affiche le statut de Ellie avec son nom et ses PV.
-- Il faut coller les morceaux en une seule phrase.
--
-- Lance : lua 01_concat.lua
-- ============================================================

nom = "Ellie"
vie = 72
message = nom .." a ".. vie .. " PV"

-- Construis le message en collant le nom, le texte et la vie.
--
-- "Ellie" .. " a " .. 72 .. " PV"
--   →  "Ellie a 72 PV"
--
-- Résultat attendu : message == "Ellie a 72 PV"
--
-- Indice : opérateur ..  (colle deux morceaux)

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(message == "Ellie a 72 PV", "Obtenu : '" .. message .. "'")
print("✅ Correct !")
