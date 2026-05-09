
# ============================================================
# Nahla — Sac de croquettes (libre)
# ============================================================

Croquettes_restantes = int(input("Combien de croquettes restantes ? "))
Nahla_mange_un_crot = 15

if Croquettes_restantes <= 0:
    print("il n'y a déjà plus rien")
else:
    while Croquettes_restantes > 0:
        print("Nahla n'a pas fini de manger")
        Croquettes_restantes -= Nahla_mange_un_crot
        if Croquettes_restantes <= 0:
            print("Nahla a fini de manger")
            break
