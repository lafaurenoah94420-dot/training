# ============================================================
# Project Zomboid — générateur bricolé à la main
# ============================================================
# Tu tires une poignée de levier jusqu’à ce que la jauge d’électricité dépasse
# un minimum pour rallumer un radiateur. Tu augmentes la jauge de +18 à chaque essai.
#
# Lance : python3 05_while.py
# ============================================================

electricite = 9

# Répète des tours tant que electricite est strictement inférieure à 60.
# À chaque tour : ajoute 18 à electricite.
#
# départ : 9
# tour 1 : 9 + 18 = 27   (27 < 60 → continue)
# tour 2 : 27 + 18 = 45  (45 < 60 → continue)
# tour 3 : 45 + 18 = 63  (63 < 60 ? non → arrêt)
#
# Résultat attendu : electricite == 63
#
# Indice : while ... : puis += dans la boucle

# À toi :
while electricite < 60:
    electricite += 18

# --- Vérification (ne pas modifier) ---
assert electricite == 63, (
    f"Obtenu : {electricite} — après trois ajouts de 18 depuis 9, on attend 63."
)
print("✅ Correct !")
