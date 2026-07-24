-- ============================================================
-- Hearts of Iron IV — nom de division par défaut
-- ============================================================
-- Si le joueur ne donne pas de nom (nil), on utilise "Division".
--
-- Lance : lua 05_defaut.lua
-- ============================================================

-- nommer("Panzer")  →  "Panzer"
-- nommer(nil)       →  "Division"
--
-- Indice : nom = nom or "Division"  puis  return nom

function nommer(nom)
    nom = nom or "Division"
    return nom
end


-- --- Vérification (ne pas modifier) ---
assert(nommer("Panzer") == "Panzer", "nommer('Panzer') doit retourner 'Panzer'")
assert(nommer(nil) == "Division", "nommer(nil) doit retourner 'Division'")
print("✅ Correct !")
