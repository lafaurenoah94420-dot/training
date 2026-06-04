# ============================================================
# Project Zomboid — manger des conserves
# ============================================================
# Ton personnage a faim. Chaque conserve mangée enlève 15 de faim.
# Tu manges tant que la faim est encore au-dessus de 20.
#
# Lance : python3 05_while.py
# ============================================================

faim = 65
conserves_mangees = 0

# Boucle while : tant que faim > 20
#   - enlève 15 à faim
#   - ajoute 1 à conserves_mangees
#
# Tour 1 : faim 65 → 50,  conserves_mangees = 1
# Tour 2 : faim 50 → 35,  conserves_mangees = 2
# Tour 3 : faim 35 → 20,  conserves_mangees = 3
# (faim vaut 20, on s'arrête car 20 > 20 est faux)
#
# Résultat attendu : faim == 20,  conserves_mangees == 3
#
# Indice : while faim > 20:

# À toi :
while faim > 20:
    conserves_mangees += 1
    faim -= 15

# --- Vérification (ne pas modifier) ---
assert faim == 20, f"faim doit valoir 20, obtenu : {faim}"
assert conserves_mangees == 3, f"conserves_mangees doit valoir 3, obtenu : {conserves_mangees}"
print("✅ Correct !")
