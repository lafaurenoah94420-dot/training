# ============================================================
# Nahla — Coût total des croquettes
# ============================================================
# Âge de Nahla (années) : 4
# Sacs par an : 12  →  total sacs : 4 × 12 = 48 sacs
# Prix d'un sac : 15 €  →  Prix total : 48 × 15 = 720 €
# Verdict : t'aurais pu prendre une manette. Nahla s'en fout.
# ============================================================

age_de_Nahla = int(input("Quel est l'age de Nahla ? "))

prix_d_un_sac = int(input("Quel est le prix d'un sac ? "))

sacs_par_ans = int(input("Combien de sacs par ans ? "))

nombre_total = age_de_Nahla * sacs_par_ans

prix_total = nombre_total * prix_d_un_sac

print(f"Nahla a {age_de_Nahla}, le prix des sacs et de {prix_d_un_sac}€, on achète {sacs_par_ans} sacs par ans. Donc au total il y a {nombre_total} sacs, et ils coutent aux  totals {prix_total}")