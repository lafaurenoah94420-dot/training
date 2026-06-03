# ============================================================
# Malik — Faut-il sortir Malik ?
# ============================================================
# Température : 38
# Foule : oui
# Verdict : Il sort en jogging — le froid le harden.
# ============================================================
def demander_temperature():
    temperature = int(input("Combien de ° il fait dehors ? "))
    if temperature > 26:
        print("Il fait chaud")
    elif temperature < 0:
        print("Il fait froid")
    else:
        print("Il fait bon chackal")
    return temperature

def demander_foule():
    foule = input("Est ce qu'il y a beacoup de gens ? ") #beaucoup ou peu
    if foule == "beaucoup":
        print("Il y a beaucoup de gens")
    elif foule == "peu":
        print("Il y a peu de gens")
    return foule

def verdict_malik(temperature, foule):
    if temperature < 0 or temperature > 26 and foule == "beaucoup":
        verdict = "Il va carrément pas sortir en faite"
    elif temperature <= 26 and temperature >= 0 and foule == "peu":
        verdict = "C'est le moment parfait pour aller sortir"
    elif temperature > 26 and foule == "peu":
        verdict = "Il y a peu de monde mais il fait chaud, va falloir prendre un jogging"
    elif temperature < 0 and foule == "peu":
        verdict = "Il y a peu de monde mais en SAH il fait froid, faudra prendre un manteau"
    return verdict

temperature = demander_temperature()

foule = demander_foule()

message = verdict_malik(temperature, foule)

print(message)