# ============================================================
# Project Zomboid — ration de conserve
# ============================================================
# Tu as 24 conserves. Chaque jour de survie tu en manges un certain nombre.
# Le script demande combien tu manges par jour, puis calcule combien
# de jours tu tiens avant la rupture (division entière).
#
# Lance : python3 04_input.py
# ============================================================

conserves = 24
# Pour l'exercice, on simule la saisie : imagine que tu tapes 3 au clavier.
# Écris une ligne qui lit un entier avec input() et le convertit avec int().
# Stocke le résultat dans conserves_par_jour.
#
# Exemple si tu tapes 3 :
#   conserves_par_jour = 3
#
# Puis calcule jours_tenus : combien de jours complets avec 24 conserves à 3/jour ?
#   24 // 3 = 8
#
# Résultat attendu : conserves_par_jour == 3  et  jours_tenus == 8
#
# Indice : int(input(...)) puis //




conserves_par_jour = int(input("Combien par jour ? "))

jours_tenus = conserves // conserves_par_jour

# À toi :
# (Pour tester sans taper à la main à chaque fois, tu peux mettre
#  conserves_par_jour = 3 après ton input — mais essaie d'abord avec input.)


# --- Vérification (ne pas modifier) ---
assert conserves_par_jour == 3, f"conserves_par_jour : obtenu {conserves_par_jour}"
assert jours_tenus == 8, f"jours_tenus : obtenu {jours_tenus}, attendu 8 (24 // 3)"
print("✅ Correct !")
