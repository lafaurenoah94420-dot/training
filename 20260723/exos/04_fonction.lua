-- ============================================================
-- GTA — distance de mission
-- ============================================================
-- Franklin calcule le temps de trajet : distance / vitesse.
-- La fonction retourne le temps (sans arrondi).
--
-- Lance : lua 04_fonction.lua
-- ============================================================

--   distance  : kilomètres
--   vitesse   : km/h
--
-- temps(120, 40)  →  120 / 40 = 3  →  retourne 3
-- temps(90, 30)   →  90 / 30 = 3   →  retourne 3
--
-- Résultat attendu : temps(120, 40) == 3  et  temps(90, 30) == 3
--
-- Indice : function ... end  +  return distance / vitesse

function temps(distance, vitesse)
    return distance / vitesse
end


-- --- Vérification (ne pas modifier) ---
assert(temps(120, 40) == 3, "temps(120, 40) doit retourner 3")
assert(temps(90, 30) == 3, "temps(90, 30) doit retourner 3")
print("✅ Correct !")
