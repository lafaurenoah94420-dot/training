# ============================================================
# Nahla — La journée de Nahla
# ============================================================
# Exemple quand c'est fini (5 jours demandés) :
#
# Combien de jours ? 5
#
# --- Jour 1 ---
# Nahla a mangé.
# Nahla a dormi.
# Nahla a joué.
# Nahla a embêté ma mère.
# --- Jour 2 ---
# (pareil)
# ...
# ============================================================

def manger():
    return "Nahla a mangé"

def dormir():
    return "Nahla a dormis"

def jouer():
    return "Nahla a joué"

def sale_garce():
    return "Nahla a embêté ma mère"

nombre_de_jour = int(input("Combien de jours ? "))

while nombre_de_jour < 1 or nombre_de_jour > 5:
    print("Entrez un nombre de jour entre 0 et 5")
    nombre_de_jour = int(input("Combien de jours ? "))

for i in range(nombre_de_jour):
    print(f"--- Jour {i + 1} ---")
    print(manger())
    print(dormir())
    print(jouer())
    print(sale_garce())
