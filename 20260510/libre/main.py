# ============================================================
# Malik — Palier de chaos du soir
# ============================================================
# Exemple d'exécutation attendu (à reproduire avec ton code) :
#
# Niveau du soir (0-5) ? 3
# Malik : il parle au micro-ondes.
# Risque : élevé — filmer recommandé.
# ============================================================

Niveau_du_soir = int(input("Niveau du soir (0-5) ? "))


if Niveau_du_soir >= 3 and Niveau_du_soir <= 5:
    print("ALERTE MALIK EST FOU")
    print("RISQUE ÉLEVÉ")
elif Niveau_du_soir < 3:
    print("Malik est calme (pour l'instant)")
    print("Risque bas")
elif Niveau_du_soir > 5:
    print("Une tempete approche...")
    print("RISQUE CONTINENTAL")
elif Niveau_du_soir < 0:
    print("L'ame de Malik est appaisée")