# ============================================================
# Nahla — Réétiquetage Whiskas
# ============================================================
# Exemple d'exécution visée :
#
# Sac au placard : Gourmet — 2 sacs
# Nahla refuse Gourmet. Réétiquetage en Whiskas...
# Sac au placard : Whiskas — 2 sacs
# ============================================================
marque = "Gourmet"
nombre_de_sacs = int(input("Combien de sacs ? "))

for i in range(3):
    nombre_de_sacs += 1
    
whiskas = True

if whiskas == True:
    marque = marque.replace("Gourmet", "Whiskas")

total_sacs = f"Il y a {nombre_de_sacs} sacs de la marque {marque}"
print(total_sacs)

if nombre_de_sacs > 5:
    print("Nahla va devenir grosse avec tout ça")
print(nombre_de_sacs)