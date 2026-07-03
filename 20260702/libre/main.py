# ============================================================
# Nahla — Tribunal des croquettes
# ============================================================
# Croquettes volées : 3
# → Verdict : petite voleuse tranquille.
# Croquettes volées : 9
# → Verdict : criminelle féline, prison canapé.
# ============================================================
croquettes_volées = int(input("Combien de croquettes ont été volées ? "))

verdict = ""

if croquettes_volées == 0:
    verdict = "Nahla a été faussement accusé, elle est donc libéré"
elif croquettes_volées > 0 and croquettes_volées <= 20:
    verdict = "Nahla a volé beaucoup de croquettes. Sentence : Une semaine sans croquettes"
elif croquettes_volées > 20:
    verdict = "Nahla a volé énormément de croquettes. Sentence : UN MOIS SANS CROQUETTES !"

print(verdict)