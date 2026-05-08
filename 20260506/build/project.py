# ============================================================
# Resident Evil — trousse et corridors (build)
# ============================================================
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python3 main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — Ligne de briefing radio
# ------------------------------------------------------------
# Leon doit envoyer une ligne radio synthétique avec son nom et le nombre
# d'herbes vertes encore dans la trousse. La chaîne doit suivre exactement le
# format attendu par le central (ponctuation comprise).
#
#   operator_name : nom affiché sur la ligne radio (str)
#   herbs_count   : nombre d'herbes vertes restantes (int)
#
# briefing_line("Leon", 3)   =>   "Agent Leon — herbes : 3."
#
# Indice : f-string avec accolades pour operator_name et herbs_count
# ------------------------------------------------------------
def briefing_line(operator_name, herbs_count):
    return f"Agent {operator_name} — herbes : {herbs_count}."


# ------------------------------------------------------------
# TODO 2 — Présence dans la trousse
# ------------------------------------------------------------
# Claire vérifie si un objet précis est encore listé dans la trousse avant de
# refaire un mélange. Si l'objet apparaît dans la liste, la fonction renvoie
# True ; sinon False.
#
#   item        : nom de l'objet cherché (str)
#   supply_list : liste des articles encore présents (list de str)
#
# inventory_has("spray", ["spray", "herbe verte"])   =>   True
# inventory_has("cartouche", ["spray", "herbe verte"])   =>   False
#
# Indice : mot-clé in
# ------------------------------------------------------------
def inventory_has(item, supply_list):
    if item in supply_list:
        return True
    else:
        return False


# ------------------------------------------------------------
# TODO 3 — Stress du couloir
# ------------------------------------------------------------
# Chaque segment de couloir identique ajoute le même malus de stress.
# Parcourt les segments avec une boucle et accumule le stress total.
#
#   segments : nombre de segments à franchir (int)
#
# Hypothèse du scénario : chaque segment ajoute 10 points de stress.
#
# corridor_stress(4)   =>   40   (4 segments × 10)
#
# Indice : for i in range(segments) puis +=
# ------------------------------------------------------------
def corridor_stress(segments):
    stress_total = 0
    for i in range(segments):
        stress_total += 10
    return stress_total

# ------------------------------------------------------------
# TODO 4 — Trousses complètes
# ------------------------------------------------------------
# Rebecca assemble des trousses complètes à partir de composants : elle ne peut
# fabriquer que des trousses entières (composants au sol : restes ignorés).
#
#   parts          : nombre de composants disponibles (int)
#   parts_per_kit  : composants nécessaires pour une trousse (int)
#
# medkits_from_parts(25, 8)   =>   3   (car 25 // 8)
#
# Indice : opérateur // puis return
# ------------------------------------------------------------
def medkits_from_parts(parts, parts_per_kit):
    return parts // parts_per_kit


# ------------------------------------------------------------
# TODO 5 — Coups pour enfoncer une porte
# ------------------------------------------------------------
# Une porte bloque le passage tant que ses points de structure sont > 0.
# Chaque coup inflige un nombre fixe de dégâts. Compte combien de coups sont
# nécessaires pour faire tomber la structure à 0 ou en dessous (dernier coup
# peut rendre la vie négative).
#
#   door_hp         : résistance restante (int > 0 dans les tests)
#   damage_per_hit  : dégâts par coup (int > 0)
#
# hits_to_destroy(50, 12)   =>   5
#
# Indice : while door_hp > 0 puis -= damage_per_hit et un compteur +=
# ------------------------------------------------------------
def hits_to_destroy(door_hp, damage_per_hit):
    hits = 0
    while door_hp > 0:
        door_hp -= damage_per_hit
        hits += 1
    return hits
