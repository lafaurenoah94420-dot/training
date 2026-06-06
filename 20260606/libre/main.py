# ============================================================
# Nahla — Rapport médical
# ============================================================
# Exemple d'exécution :
#   Poids de Nahla (kg) ? 6.2
#   Diagnostic : obésité féline confirmée.
#   Recommandation : régime strict.
#   Verdict de Nahla : je m'en fous, donne les croquettes.
# ============================================================
Poids_de_Nahla = float(input("Poids de Nahla :"))

def rapport_médical():
    if Poids_de_Nahla <= 2:
        Diagnostic = "Maigre"
        Recomendation = "Dois manger plus"
        Verdict_de_Nahla = "Je dois grossir... DONNE MOI DES CROQUETTES"
        print(Diagnostic)
        print(Recomendation)
        print(Verdict_de_Nahla)
    elif Poids_de_Nahla > 2 and Poids_de_Nahla <= 5 :
        Diagnostic = "Risque de grossir"
        Recomendation = "Éviter les gros repats"
        Verdict_de_Nahla = "Je m'en fous, donne les croquettes"
        print(Diagnostic)
        print(Recomendation)
        print(Verdict_de_Nahla)
    elif Poids_de_Nahla > 5:
        Diagnostic = "!ALERTE! NAHLA EST OBÈSE"
        Recomendation = "DOIS FAIRE UN RÉGIME EN URGENCE"
        Verdict_de_Nahla = "JE SUIS LA REINE DES GROS CHATS"
        print(Diagnostic)
        print(Recomendation)
        print(Verdict_de_Nahla)
rapport_médical()