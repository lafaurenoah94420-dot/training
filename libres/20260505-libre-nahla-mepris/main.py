# ============================================================
# Nahla — Planning officiel du mépris
# ============================================================
# Exemple d'exécution attendu (à reproduire avec ton code) :
#
# Heure ? 9
# 09h — Nahla : réunion stratégique avec le radiateur. Priorité : chaleur. Toi : tu es du décor.
# Croquettes : pas maintenant, elle teste ta patience.
# ============================================================
texte =  input("Heure ? ")
hours = int(texte)

hours = max(0, hours)
hours = min(24, hours)

if hours <= 8:
    print("Nahla dort comme un gros chat")

if hours >= 9 and hours <= 19:
    print("Nahla vit sa best life")

if hours >= 20 and hours <= 21:
    print("Nahla veut son pater (ce gros lard)")

if hours >= 22:
    print("Nahla fait sa vie ou elle dort")

