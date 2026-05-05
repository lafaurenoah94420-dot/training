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

# Détermine le statut selon les PV
#
# avec pv = 18  =>  statut == "En vie"
# avec pv = 0   =>  statut == "Mort"
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
