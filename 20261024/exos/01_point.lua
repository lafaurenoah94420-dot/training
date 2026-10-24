-- ============================================================
-- GTA — notation point
-- ============================================================
-- Tu lis le nom du perso avec la notation point (pas ["..."]).
--
-- Lance : lua 01_point.lua
-- ============================================================

perso = { nom = "Michael", job = "braqueur" }
nom_lu = perso["nom"]

-- nom_lu = perso.nom → "Michael"
-- (c'est la même chose que perso["nom"], juste une autre écriture)
--
-- Résultat attendu : nom_lu == "Michael"
--
-- Indice : perso.nom

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(nom_lu == "Michael", "Obtenu : '" .. tostring(nom_lu) .. "'")
print("✅ Correct !")
