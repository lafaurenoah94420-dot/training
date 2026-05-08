# ============================================================
# Hearts of Iron IV — caisse avant embarquement
# ============================================================
# La caisse indique fusils et cartouches avant chargement. On enlève ce qui part
# avec le premier convoi pour mettre à jour les stocks écrits dans le dictionnaire.
#
# Lance : python3 05_dict.py
# ============================================================

stock = {
        "fusils": 8, 
        "cartouches": 120
    }

stock["fusils"] -= 2

stock["cartouches"] -= 20


# Retire 2 fusils et 20 cartouches en modifiant stock avec les clés "fusils" et
# "cartouches".
#
# Déroulé :
#   départ : fusils 8, cartouches 120
#   après envoi : fusils 6, cartouches 100
#
# Résultat attendu : stock["fusils"] == 6 et stock["cartouches"] == 100
#
# Indice : stock["fusils"] -= ... puis pareil pour cartouches

# À toi :


# --- Vérification (ne pas modifier) ---
assert stock["fusils"] == 6, f"Fusils obtenus : {stock['fusils']} — attendu : 6."
assert stock["cartouches"] == 100, (
    f"Cartouches obtenues : {stock['cartouches']} — attendu : 100."
)
print("✅ Correct !")
