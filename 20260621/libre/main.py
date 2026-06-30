# ============================================================
# Nahla — Rapport médical quotidien
# ============================================================
# Poids de Nahla (kg) ? 6.8
# Nahla : 6.8 kg
# Diagnostic : obésité morbide féline stade 3
# Recommandation : régime immédiat
# Pronostic : elle s'en fout.
# ============================================================
poids_de_Nahla = int(input("Combien de kilos pèse Nahla ? "))

def rapport_medical_de_Nahla():
    if poids_de_Nahla > 0 and poids_de_Nahla <= 3:
        print(f"Nahla pèse {poids_de_Nahla} kg")
        commentaire = "Nahla est trop maigre"
        recommandation = "Devrais manger un peu plus"
    elif poids_de_Nahla > 3 and poids_de_Nahla <= 6:
        print(f"Nahla pèse {poids_de_Nahla} kg")
        commentaire = "Nahla a un poids normal"
        recommandation = "Devrais éviter de manger de trop gros repas"
    elif poids_de_Nahla > 6:
        print(f"Nahla pèse {poids_de_Nahla} kg")
        commentaire = "Nahla est CHONK"
        recommandation = "Dois maigrir"
    elif poids_de_Nahla <= 0:
        commentaire = "Nahla est... morte ?"
        recommandation = "Enterrer Nahla avec pleins de croquette :("
    
    print(commentaire)
    print(recommandation)
rapport_medical_de_Nahla()
    

