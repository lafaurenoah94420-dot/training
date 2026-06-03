# ============================================================
# Project Zomboid — Munitions lourdes
# ============================================================
# Tu inventories les munitions trouvées. Tu ne comptes que celles
# dont le calibre vaut "12" ET la quantité est au moins 5.
#
# Lance : python3 04_for_if_and.py
# ============================================================

paquets = [
    {"calibre": "9", "quantite": 20},
    {"calibre": "12", "quantite": 3},
    {"calibre": "12", "quantite": 8},
    {"calibre": "12", "quantite": 12},
    {"calibre": "45", "quantite": 6},
]

total_12_gros_paquets = 0

# Parcours paquets avec for.
# Si calibre == "12" ET quantite >= 5, ajoute quantite à total_12_gros_paquets.
#
# paquet 2 : 12 mais 3 < 5  →  ignoré
# paquet 3 : 12 et 8 >= 5   →  total = 8
# paquet 4 : 12 et 12 >= 5  →  total = 20
#
# Résultat attendu : total_12_gros_paquets == 20
#
# Indice : for p in paquets:  puis  if p["calibre"] == "12" and ...

# À toi :
for p in paquets:
    if p["calibre"] == "12" and p["quantite"] >= 5:
        total_12_gros_paquets += p["quantite"]

# --- Vérification (ne pas modifier) ---
assert total_12_gros_paquets == 20, f"Obtenu : {total_12_gros_paquets}, attendu : 20"
print("✅ Correct !")
