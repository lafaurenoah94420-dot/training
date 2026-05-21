# ============================================================
# Resident Evil — porte verrouillée
# ============================================================
# Leon arrive devant une porte. Si le niveau d'accès est au moins 3,
# la porte s'ouvre. Sinon elle reste fermée.
#
# Lance : python3 02_condition.py
# ============================================================

niveau_acces = 3
etat_porte = ""

# Détermine etat_porte selon niveau_acces.
#
# niveau_acces = 3  →  3 >= 3 ? oui  →  etat_porte = "Ouverte"
# niveau_acces = 1  →  1 >= 3 ? non  →  etat_porte = "Fermée"
#
# Résultat attendu : etat_porte == "Ouverte"  (car niveau_acces vaut 3 ici)
#
# Indice : if / else

# À toi :
if niveau_acces == 3:
    etat_porte = 'Ouverte'
else:
    etat_porte = 'Fermée'

# --- Vérification (ne pas modifier) ---
assert etat_porte == "Ouverte", f"Obtenu : '{etat_porte}'"
print("✅ Correct !")
