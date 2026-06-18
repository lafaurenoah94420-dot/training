# ============================================================
# Nahla — Qui a été ignoré ?
# ============================================================
# Humain ignoré : Malik
# Humain ignoré : Kays
# Humain ignoré : stop
# Nahla a ignoré 2 humains : ['Malik', 'Kays']
# Verdict : journée productive.
# ============================================================
def ignoré_comme_un_boufon():
    continué = "oui"
    while continué == "oui":
        Kays_ignoré = input("Kays a t'il été ignoré ? ").lower() # oui ou non
        Malik_ignoré = input("Malik a t'il été ignoré ? ").lower() # oui oou non
        if Kays_ignoré == "oui" and Malik_ignoré == "oui":
            print("Nahla est en mode racaille aujourd'hui")
        elif Kays_ignoré == "non" and Malik_ignoré == "oui":
            print("Nahla est raciste des arabes")
        elif Kays_ignoré == "oui" and Malik_ignoré == "non":
            print("Nahla s'est embrouillé avec Kays")
        elif Kays_ignoré == "non" and Malik_ignoré == "non":
            print("Nahla veut des papouilles")
        else:
            print("Quoi ?")
        continué = input("Continué ? ").lower() # oui ou non
ignoré_comme_un_boufon()



