---
name: python-build
description: Génère un mini-projet Python avec un scaffold à compléter. main.py est déjà écrit, le learner implémente les fonctions dans project.py jusqu'à ce que le programme tourne. ~1h. Utilise quand l'utilisateur dit /python-build.
---

# Python Build

Session de construction. L'agent génère un mini-programme avec un `main.py` déjà écrit et un `project.py` avec des fonctions à implémenter. Le learner complète les fonctions jusqu'à ce que `python main.py` fasse quelque chose de cool.

Les projets viennent de l'univers de jeux comme Project Zomboid, The Last of Us, Resident Evil, GTA, Hearts of Iron 4. Le learner ne construit pas une "calculatrice scolaire" — il construit le système d'inventaire de Joel, le simulateur de propagation d'infection de Zomboid, le calculateur de production militaire de HOI4.

**Le `main.py` ne se touche pas.** Il montre ce que le programme est censé faire — les fonctions appelées, les données attendues, le résultat affiché. Le learner lit `main.py` pour comprendre, puis implémente dans `project.py`.

**Durée : ~1h.** C'est la session principale de la semaine. Générer **3 fonctions** à implémenter, indépendantes les unes des autres. Pas de fonctions qui s'appuient sur les précédentes — chacune fait une chose, seule.

---

## Workflow

### Étape 0 — Proposer 3 projets

Avant de générer quoi que ce soit, propose exactement 3 projets distincts et attends le choix.

Règles :
- Chaque projet doit produire un programme **qui fait quelque chose de visible et amusant**
- Varier les contextes : jeux en mode texte, outils, scripts utiles ou marrants
- Ne pas reproduire un projet récent (vérifier `builds/` si nécessaire)
- Calibrer la difficulté : le projet du mercredi est plus facile que celui du vendredi

Format :
```
Voici 3 projets — choisis-en un :

**A — [nom du projet]**
[2-3 lignes : ce que fait le programme une fois terminé]

**B — [nom du projet]**
[2-3 lignes]

**C — [nom du projet]**
[2-3 lignes]
```

Attends le choix avant de générer quoi que ce soit.

### Étape 1 — Générer les fichiers

Créer `builds/YYYYMMDD-build-[slug]/` avec :

```
builds/YYYYMMDD-build-[slug]/
├── BRIEF.md
├── main.py       # programme principal — déjà écrit, ne pas modifier
└── project.py    # fonctions à implémenter
```

---

### Règles de conception

**`main.py` :**
- Déjà complet et lisible — ne doit jamais être modifié par le learner
- Montre clairement ce que le programme fait : appelle les fonctions de `project.py`, affiche les résultats
- Commence par : `from project import fonction1, fonction2, ...`
- Doit être court (20-30 lignes) — lisible en 2 minutes
- Si `main.py` est lancé avec toutes les fonctions non implémentées → crash propre sur `NotImplementedError`
- Textes affichés en français, noms de variables en anglais

**`project.py` :**

**Le learner est un vrai débutant.** Les fonctions doivent être implémentables avec les bases absolues du Python. Chaque fonction est courte (3-6 lignes d'implémentation), indépendante, et fait une seule chose.

**Concepts autorisés dans les fonctions :**
- Variables et assignation
- `if / elif / else`
- Boucle `for` sur une liste simple ou `range()`
- `print()`, `return`
- `int()`, `str()`, `float()` pour convertir
- Opérations mathématiques simples (`+`, `-`, `*`, `/`, `//`, `%`)
- Accès à une liste par index (`liste[0]`)
- `append()` sur une liste
- `random.randint()` ou `random.choice()` si pertinent

**Concepts interdits dans ce skill :**
- Dicts (sauf clé → valeur string/int simple et seulement si la fonction est UNIQUEMENT de la lecture)
- Tuples comme structures de données
- Fonctions qui appellent d'autres fonctions dans leur corps
- List comprehensions
- `sorted()`, `sum()`, `zip()`, `enumerate()`
- Classes
- `*args`, `**kwargs`

Structure type :
```python
# ============================================================
# [Titre du projet]
# ============================================================
# Implémente les 3 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — [nom de l'action]
# ------------------------------------------------------------
# Ce que ça fait : [description en une phrase, point de vue utilisateur]
#
# Exemple :
#   Entrée  : [valeur concrète simple — un int, une string, une liste courte]
#   Sortie  : [valeur concrète attendue]
#
# Indice : [nom exact de l'outil Python à utiliser — ex: "utilise random.randint()"]
# ------------------------------------------------------------
def nom_fonction(parametre):
    raise NotImplementedError


# [répéter pour TODO 2 et TODO 3]
```

**Règles pour les blocs TODO :**
- L'exemple Entrée/Sortie est toujours **concret et simple** — un seul int ou string en entrée, pas de structure complexe
- L'indice donne le nom exact de l'outil sans donner l'implémentation
- Chaque fonction commence obligatoirement par `raise NotImplementedError`
- La première fonction doit être implémentable en 5-10 minutes
- **Noms de variables et fonctions en anglais** — seuls les commentaires et exemples sont en français

**Règles pour la progression dans la session :**
- TODO 1 : trivial — 2-3 lignes, aucun doute sur l'outil à utiliser
- TODO 2 : un peu plus de réflexion — une condition ou une boucle simple
- TODO 3 : le plus difficile — combine deux concepts vus dans les deux premières
- Pas de fonction bonus avant la semaine 3

**`BRIEF.md` :**

```markdown
# Build — [nom du projet]

## Ce que tu vas construire

[2-3 phrases : ce que le programme fait une fois terminé, du point de vue de l'utilisateur]

## Comment démarrer

1. Lis `main.py` en entier — ne le modifie pas, il te montre ce que le programme doit faire
2. Ouvre `project.py` et implémente les fonctions dans l'ordre
3. Lance `python main.py` après chaque fonction implémentée pour voir si ça avance

## Critères de réussite

- [ ] `python main.py` tourne de bout en bout sans erreur
- [ ] Chaque fonction fait ce que l'exemple Entrée/Sortie décrit
- [ ] Aucun `raise NotImplementedError` ne reste

## Indice (seulement si bloqué depuis plus de 15 min)

<details>
<summary>Indice général</summary>
[Un pointeur vers le bon concept Python — pas le code]
</details>
```

---

### Étape 2 — Lancement

Après avoir généré les fichiers, afficher :

```
🔨  BUILD — ~1h.

Colle ça dans ton terminal :

  cd /Users/byronlove/Desktop/dev/python-noah/builds/YYYYMMDD-build-[slug]

Lis main.py en entier d'abord — il te montre ce que tu dois construire.
Ensuite implémente les fonctions dans project.py une par une.

Pour lancer le programme :

  python main.py

✅  Objectif : le programme tourne de bout en bout.
Dis-moi quand tu as fini ou si tu es bloqué depuis plus de 15 min.
```

### Étape 3 — Débrief (quand l'utilisateur a fini)

Demander de coller la sortie de `python main.py`.

Feedback ciblé (8-10 lignes max) :
- Quelles fonctions ont été implémentées sans hésiter
- Laquelle a demandé le plus de temps et pourquoi
- Le ou les outils Python utilisés pour la première fois
- 1 chose concrète à retenir pour la prochaine session build

---

## Banque de projets (inspiration — générer des variantes originales)

Chaque projet génère exactement 3 fonctions simples. Les exemples ci-dessous décrivent ce que les fonctions doivent faire — pas comment les implémenter.

**The Last of Us — Simulateur de tir**
Fonction 1 : calculer les munitions restantes après un tir (munitions - tir, min 0).
Fonction 2 : calculer les dégâts reçus et la vie restante (vie - dégâts, min 0).
Fonction 3 : déterminer si le joueur est mort, blessé ou en bonne santé selon sa vie.

**Project Zomboid — Jauge de faim**
Fonction 1 : réduire la faim en mangeant (faim - valeur_nourriture, max 100).
Fonction 2 : augmenter la faim avec le temps (faim + fatigue_par_heure × heures).
Fonction 3 : retourner le message d'état selon le niveau de faim (critique / faible / ok).

**Resident Evil — Gestion d'herbes**
Fonction 1 : vérifier si le joueur a assez d'herbes pour se soigner (True/False).
Fonction 2 : appliquer le soin (vie + soin, max vie_max).
Fonction 3 : afficher le message de soin selon les points récupérés.

**GTA — Calcul de wanted**
Fonction 1 : calculer le niveau de wanted selon le nombre de crimes commis.
Fonction 2 : réduire le wanted en payant un pot-de-vin (wanted - réduction, min 0).
Fonction 3 : retourner le message de statut selon le niveau de wanted (tranquille / recherché / très recherché).

**Hearts of Iron 4 — Production d'équipement**
Fonction 1 : calculer les équipements produits (usines × production_par_usine).
Fonction 2 : vérifier si la production suffit pour équiper une division (True/False).
Fonction 3 : calculer le nombre de jours pour atteindre un objectif de production.
