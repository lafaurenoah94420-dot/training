# ============================================================
# The Last of Us — salves qui comptent vraiment
# ============================================================
# Joel note les dégâts infligés à plusieurs infectés. Tu dois compter combien
# de fois le dépasse un seuil pour débloquer une médaille « carnage ».
#
# Lance : python3 04_for_if.py
# ============================================================

degats = [22, 65, 38, 71, 40]

seuil = 40

count_elite = 0

# Parcourt degats : si la valeur est strictement supérieure à seuil, ajoute 1 à count_elite.
#
# 22 > 40 ? non  →  count_elite reste 0
# 65 > 40 ? oui  →  count_elite = 1
# 38 > 40 ? non  →  reste 1
# 71 > 40 ? oui  →  count_elite = 2
# 40 > 40 ? non (égal ne compte pas)  →  reste 2
#
# Résultat attendu : count_elite == 2
#
# Indice : boucle for sur degats, avec if à l'intérieur et += sur count_elite

# À toi :
for i in degats:
    if i > seuil:
        count_elite += 1

# --- Vérification (ne pas modifier) ---
assert count_elite == 2, (
    f"Obtenu : {count_elite} — seuls 65 et 71 dépassent strictement 40."
)
print("✅ Correct !")
