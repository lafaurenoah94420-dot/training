-- ============================================================
-- Hearts of Iron IV — équipement manquant
-- ============================================================
-- Tu cherches si "artillerie" est dans la liste d'équipement.
-- Si oui, trouve = true. Sinon, trouve = false.
--
-- Lance : lua 05_presence.lua
-- ============================================================

equipement = {"infanterie", "chars", "artillerie", "avions"}
trouve = false

-- Parcours equipement. Si un élément est égal à "artillerie",
-- mets trouve à true.
--
-- tour 1 : "infanterie" == "artillerie" ? non
-- tour 2 : "chars" == "artillerie" ? non
-- tour 3 : "artillerie" == "artillerie" ? oui  →  trouve = true
-- tour 4 : (tu peux continuer ou t'arrêter)
--
-- Résultat attendu : trouve == true
--
-- Indice : for + if  +  trouve = true
--          (compare x, pas la table entière)

-- À toi :
for i, x in ipairs (equipement) do
    if x == "artillerie" then
        trouve = true 
    end
end

-- --- Vérification (ne pas modifier) ---
assert(trouve == true, "trouve doit être true — 'artillerie' est dans la liste")
print("✅ Correct !")
