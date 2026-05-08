# ============================================================
# Hearts of Iron IV — rationnement de division
# ============================================================
# Tu sais combien de caisses il reste et combien une division consomme par jour.
# Tu veux le nombre entier de jours avant rupture totale (division entière).
#
# Lance : python3 04_fonction.py
# ============================================================


def jours_avant_rupture(caisses_restantes, consommation_par_jour):
    return caisses_restantes // consommation_par_jour


# Implémente la fonction pour qu'elle retourne caisses_restantes // consommation_par_jour.
#
# Exemple d'appel avec les valeurs réelles du test :
#   jours_avant_rupture(100, 15)
#
# Déroulé :
#   100 divisé par 15 → quotient entier 6 (reste ignoré)
#
# Donc jours_avant_rupture(100, 15) doit renvoyer 6.
#
# Indice : opérateur // dans le return

# À toi : remplace raise NotImplementedError par ton code



# --- Vérification (ne pas modifier) ---
assert jours_avant_rupture(100, 15) == 6, "100 // 15 doit donner 6 jours complets."
assert jours_avant_rupture(80, 20) == 4, "80 // 20 doit donner 4."
print("✅ Correct !")
