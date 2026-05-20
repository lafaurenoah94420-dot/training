# ============================================================
# Hearts of Iron IV — mobilisation
# ============================================================
# Le général peut appeler des divisions. Sans précision, le jeu
# en mobilise 10 par défaut. Avec un ordre urgent, tu peux en demander plus.
#
# Lance : python3 05_defaut.py
# ============================================================

#   n  : nombre de divisions demandées (optionnel)
#
# mobiliser()           →  pas d'argument  →  retourne 10
# mobiliser(25)         →  n vaut 25       →  retourne 25
#
# Résultat attendu : mobiliser() == 10  et  mobiliser(25) == 25
#
# Indice : def mobiliser(n=10): puis return n

def mobiliser(n=10):
    return n



# --- Vérification (ne pas modifier) ---
assert mobiliser() == 10, "mobiliser() sans argument doit retourner 10"
assert mobiliser(25) == 25, "mobiliser(25) doit retourner 25"
print("✅ Correct !")
