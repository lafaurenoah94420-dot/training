-- ============================================================
-- Resident Evil — niveau d'infection
-- ============================================================
-- Le jeu affiche un statut selon l'infection :
--   infection >= 80  →  "critique"
--   infection >= 40  →  "eleve"
--   sinon            →  "faible"
--
-- Lance : lua 02_statut.lua
-- ============================================================

infection = 55
statut = ""

-- Détermine statut selon infection (55 ici).
--
-- 55 >= 80 ? non
-- 55 >= 40 ? oui  →  statut = "eleve"
--
-- Résultat attendu : statut == "eleve"
--
-- Indice : if / elseif / else / end   (attention : == pour comparer,
--          et elseif a besoin de then)

-- À toi :
if infection >= 80 then
    statut = "critique"
elseif infection < 80 and infection >= 40 then
    statut = "eleve"
else
    statut = "faible"
end
-- --- Vérification (ne pas modifier) ---
assert(statut == "eleve", "Obtenu : '" .. tostring(statut) .. "' — avec infection=55")
print("✅ Correct !")
