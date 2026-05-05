# ============================================================
# Resident Evil — état du personnage
# ============================================================
# Les points de vie valent 18. Si pv est strictement supérieur à 0, statut doit
# valoir "En vie". Sinon statut doit valoir "Mort".
#
# Résultat attendu quand tu lances ce fichier :
#   ✅ Correct !
# ============================================================

pv = 18

if pv > 0:
    statut = "En vie"
else:
    statut = "Mort"


# --- Vérification (ne pas modifier) ---
assert statut == "En vie", (
    f"Obtenu : '{statut}' — avec pv > 0, le statut attendu est « En vie »."
)
print("✅ Correct !")
