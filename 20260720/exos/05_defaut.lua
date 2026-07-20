-- ============================================================
-- Hearts of Iron IV — nom de division
-- ============================================================
-- Si le joueur ne donne pas de nom, la division s'appelle
-- "Division" par défaut. La fonction utilise `or` pour ça.
--
-- Lance : lua 05_defaut.lua
-- ============================================================

--   nom  : le nom choisi, ou nil s'il n'y en a pas
--
-- nommer("Panzer")  →  retourne "Panzer"
-- nommer(nil)       →  retourne "Division"  (valeur par défaut)
--
-- Résultat attendu : nommer("Panzer") == "Panzer"
--                    et nommer(nil) == "Division"
--
-- Indice : param = param or "Division"  puis  return param

function nommer(nom)
    param = nom or "Division"
    return param
end



-- --- Vérification (ne pas modifier) ---
assert(nommer("Panzer") == "Panzer", "nommer('Panzer') doit retourner 'Panzer'")
assert(nommer(nil) == "Division", "nommer(nil) doit retourner 'Division'")
print("✅ Correct !")
