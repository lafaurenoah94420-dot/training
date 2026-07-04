# ============================================================
# Project Zomboid — inventaire de fouille
# ============================================================
# Tu fouilles 4 maisons. À chaque maison tu trouves un objet
# que tu ajoutes à ton sac. Liste ce que tu as ramassé.
#
# Lance : python3 05_append.py
# ============================================================

trouvailles = ["crochet", "batterie", "eau", "bandage"]
inventaire = []

# Parcours trouvailles avec for et ajoute chaque objet à inventaire
# avec append.
#
# tour 1 : "crochet"   →  inventaire = ["crochet"]
# tour 2 : "batterie"  →  inventaire = ["crochet", "batterie"]
# tour 3 : "eau"       →  inventaire = [..., "eau"]
# tour 4 : "bandage"   →  inventaire = [..., "bandage"]
#
# Résultat attendu : inventaire == ["crochet", "batterie", "eau", "bandage"]
#
# Indice : for + .append()

# À toi :
for i in trouvailles:
    inventaire.append(i)

# --- Vérification (ne pas modifier) ---
assert inventaire == ["crochet", "batterie", "eau", "bandage"], f"Obtenu : {inventaire}"
assert len(inventaire) == 4, f"Tu dois avoir 4 objets, obtenu : {len(inventaire)}"
print("✅ Correct !")
