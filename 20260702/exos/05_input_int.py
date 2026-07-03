# ============================================================
# Hearts of Iron IV — niveau de menace
# ============================================================
# Le général entre le niveau de tension mondiale (un nombre).
# Le programme affiche le niveau de menace correspondant.
#
# Lance : python3 05_input_int.py
# ============================================================

# Simule une entrée utilisateur (ne pas modifier cette ligne)
import io
import sys
sys.stdin = io.StringIO("75\n")

tension = int(input("Niveau de tension (0-100) : "))
niveau = ""

# Détermine le niveau selon la tension.
#
# tension = 75  →  75 >= 50 ? oui  →  niveau = "Critique"
# tension = 30  →  30 >= 50 ? non  →  30 >= 20 ? oui  →  niveau = "Modéré"
# tension = 10  →  10 >= 20 ? non  →  niveau = "Faible"
#
# Règles :
#   50 ou plus  →  "Critique"
#   20 à 49     →  "Modéré"
#   moins de 20 →  "Faible"
#
# Résultat attendu ici : niveau == "Critique"  (car tension vaut 75)
#
# Indice : if / elif / else

# À toi :
if tension >= 50:
    niveau = "Critique"
elif tension < 50 and tension >= 20:
    niveau = "Modéré"
else:
    niveau = "Faible"

# --- Vérification (ne pas modifier) ---
assert niveau == "Critique", f"Obtenu : '{niveau}', attendu : 'Critique'"
print("✅ Correct !")
