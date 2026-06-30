# ============================================================
# Resident Evil — Herbes dans la mallette
# ============================================================
# Leon trouve une herbe verte et met à jour son inventaire.
# L'inventaire est un dictionnaire : nom de l'objet → quantité.
#
# Lance : python3 02_dict_ecriture.py
# ============================================================

inventaire = {
    "herbe_verte": 2,
    "spray": 1,
}

# Ajoute 1 herbe verte à l'inventaire.
#
# inventaire["herbe_verte"] vaut 2 au départ
# 2 + 1 = 3
# inventaire["herbe_verte"] = 3
#
# Résultat attendu : inventaire["herbe_verte"] == 3
#
# Indice : dict["cle"] = nouvelle_valeur

# À toi :
inventaire["herbe_verte"] += 1

# --- Vérification (ne pas modifier) ---
assert inventaire["herbe_verte"] == 3, (
    f"herbe_verte : obtenu {inventaire['herbe_verte']}, attendu 3"
)
print("✅ Correct !")
