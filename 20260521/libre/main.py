# ============================================================
# Nahla — Compteur de mépris matinal
# ============================================================
# Combien d'appels ? 10
# Verdict : mépris standard. Elle te considère comme un meuble bruyant.
# ============================================================


def mépris_de_Nahla():
    continuer = "oui"
    while continuer == "oui":
        nombre_d_appels = int(input("Nombre d'appels ? "))
        réponse_de_Nahla = nombre_d_appels // 5

        print("réponse de Nahla : ", réponse_de_Nahla)

        if nombre_d_appels <= 2:
            print("Nahla est un bon chat")
        elif nombre_d_appels > 2 and nombre_d_appels <= 6:
            print("Nahla est insolente mais obéissante")
        elif nombre_d_appels > 6 and nombre_d_appels <= 9:
            print("Nahla est mal élevée est doit etre corrigée sur le champ")
        elif nombre_d_appels >= 10:
            print("NAHLA VIENT PAR LÀ")
        else:
            print("Koi ?")
        continuer = input("Continuer ? ")
mépris_de_Nahla()