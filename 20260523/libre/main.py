# ============================================================
# Malik — Prédicteur de comportement
# ============================================================
# Situation : il fait 35°C dehors
# Prédiction : Malik sort en jogging et crie que le froid le harden.
# ============================================================
import random

def vie_de_Malik():
    continuer = "oui"
    while continuer == "oui":
        degrés = random.randint(0, 50)
        if degrés >= 35:
            print(f"situation : il fait {degrés}°C")
            print("Malik sort en jogging et crie que le froid le harden")
        elif degrés >= 15 and degrés < 35:
            print(f"situation : il fait {degrés}°C")
            print("Malik sort en mode BONHOMME")
        elif degrés >= 0 and degrés < 15:
            print(f"situation : il fait {degrés}°C")
            print("Malik ne sort pas il fait trop froid wsh")
        continuer = input("Continuer ? ") #oui ou non

vie_de_Malik()