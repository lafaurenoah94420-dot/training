# ============================================================
# Resident Evil — statut médical
# ============================================================
# Dans le labo Umbrella, chaque survivant a un écran médical.
# L'écran affiche "En vie" si les PV sont strictement supérieurs à 0,
# "Mort" sinon. Leon vient d'être touché — vérifie son statut.
#
# Lance : python 02_condition.py
# ============================================================

pv = 18

# Détermine le statut selon les PV.
# Si pv est strictement supérieur à 0, statut vaut "En vie".
# Sinon (pv vaut 0 ou moins), statut vaut "Mort".
#
# pv = 18  →  18 > 0 ? oui  →  statut = "En vie"
# pv = 0   →  0 > 0  ? non  →  statut = "Mort"
#
# Résultat attendu : statut == "En vie"  (car pv vaut 18 ici)
#
# Indice : if / else

if pv > 0:
    statut = "En vie"
else:
    statut = "Mort"


# --- Vérification (ne pas modifier) ---
assert statut == "En vie", (
    f"Obtenu : '{statut}' — avec pv > 0, le statut attendu est « En vie »."
)
print("✅ Correct !")
