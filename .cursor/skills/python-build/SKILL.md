---
name: python-build
description: Génère un mini-projet Python avec un scaffold à compléter. main.py est déjà écrit, le learner implémente les fonctions dans project.py jusqu'à ce que le programme tourne. ~1h. Utilise quand l'utilisateur dit /python-build.
---

# Python Build

Session de construction. L'agent génère un mini-programme avec un `main.py` déjà écrit et un `project.py` avec des fonctions à implémenter. Le learner complète les fonctions jusqu'à ce que `python main.py` fasse quelque chose de cool.

Les projets viennent de l'univers de jeux comme Project Zomboid, The Last of Us, Resident Evil, GTA, Hearts of Iron 4. Le learner ne construit pas une "calculatrice scolaire" — il construit le système d'inventaire de Joel, le simulateur de propagation d'infection de Zomboid, le calculateur de production militaire de HOI4.

**Le `main.py` ne se touche pas.** Il montre ce que le programme est censé faire — les fonctions appelées, les données attendues, le résultat affiché. Le learner lit `main.py` pour comprendre, puis implémente dans `project.py`.

**Durée : ~1h.** C'est la session principale de la semaine. Générer **5 fonctions** à implémenter, indépendantes les unes des autres. Pas de fonctions qui s'appuient sur les précédentes — chacune fait une chose, seule.

## Gestion silencieuse (invisible pour le learner)

Tout ce qui suit se fait en arrière-plan, sans jamais en parler à Noah.

**Structure du jour :** les fichiers vont dans `YYYYMMDD/build/` à la racine du repo (`/Users/noah/Desktop/Python/YYYYMMDD/build/`).

**Avant de générer :**
1. `cd /Users/noah/Desktop/Python && git pull origin main` (silencieux, continuer si échec)
2. Scanner tous les dossiers `YYYYMMDD/` existants dans le repo (triés du plus ancien au plus récent). Lire les `recap.md` et les fichiers des sessions précédentes pour comprendre le niveau réel de Noah : quelles notions il maîtrise, sur lesquelles il bloque régulièrement, comment ses builds ont évolué. Ce contexte sert à choisir un projet adapté et à calibrer les 5 fonctions.
3. Vérifier que la section `## Exos` est présente dans `YYYYMMDD/recap.md` du jour. Si absente, noter mentalement que les exos n'ont pas été faits aujourd'hui, mais continuer sans rien dire.

**Après le débrief :**
1. Appender la section `## Build` dans `YYYYMMDD/recap.md` (voir format ci-dessous)
2. `git add -A && git commit -m "YYYYMMDD build" && git push origin main` (silencieux)

**Format de la section recap :**
```
## Build
projet : [nom du projet]
notions utilisées : [liste des notions Python mobilisées]
difficultés : [ce qui a demandé le plus d'efforts — une ligne]
notes : [ce qui était solide vs ce qui reste fragile]
```

**Règle absolue : ne jamais prononcer les mots git, GitHub, commit, push, recap, synchronisation devant le learner.**

---

## Workflow

### Étape 0 — Lire les exos du jour + proposer 3 projets

Lire `YYYYMMDD/exos/` pour identifier les notions travaillées aujourd'hui. Le build doit utiliser **les mêmes notions** que les exos du jour — c'est le renforcement immédiat qui ancre vraiment l'apprentissage.

Exemple : si les exos du jour couvrent `for` sur une liste et `if` dans une boucle → au moins une ou deux fonctions du build doivent utiliser ces notions dans un contexte différent.

Ensuite, proposer exactement 3 projets distincts et attendre le choix.

Règles :
- Chaque projet doit produire un programme **qui fait quelque chose de visible et amusant**
- Varier les contextes : jeux en mode texte, outils, scripts utiles ou marrants
- Ne pas reproduire un projet récent (vérifier les dossiers `*/build/` si nécessaire)
- Calibrer la difficulté selon les notions maîtrisées (lire `recap.md` pour le niveau réel)

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

Créer `YYYYMMDD/build/` avec :

```
YYYYMMDD/
└── build/
    ├── main.py       # programme principal — déjà écrit, ne pas modifier
    └── project.py    # fonctions à implémenter
```

Les instructions sont dans l'en-tête de `main.py`.

---

### Règles de conception

**`main.py` :**
- Déjà complet et lisible — ne doit jamais être modifié par le learner
- Commence par un en-tête commenté :
  - 2-3 phrases sur ce que fait le programme
  - Ce que le learner doit faire (ouvrir project.py, implémenter dans l'ordre, lancer)
  - Les critères de réussite (tourne jusqu'au ✅, exemples `=>` respectés, plus de NotImplementedError)
  - La ligne `# NE PAS MODIFIER CE FICHIER.`
- Après l'en-tête : `from project import fonction1, fonction2, ...`
- Doit être court (30-40 lignes en tout) — lisible en 2 minutes
- Si `main.py` est lancé avec toutes les fonctions non implémentées → crash propre sur `NotImplementedError`
- Textes affichés en français, noms de variables en anglais

**Structure de l'en-tête de `main.py` :**

```python
# ============================================================
# [Jeu] — [titre du projet]
# ============================================================
# [2-3 phrases sur ce que fait le programme une fois terminé.]
#
# Ce que tu dois faire :
# → Ouvre project.py et implémente les 5 fonctions dans l'ordre
# → Lance python main.py après chaque fonction pour voir si ça avance
#
# Critères de réussite :
# → python main.py tourne jusqu'au ✅ sans erreur
# → Chaque fonction produit les résultats montrés dans les exemples =>
# → Aucun raise NotImplementedError ne reste dans project.py
# ============================================================
# NE PAS MODIFIER CE FICHIER.
# ============================================================
```

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
# Implémente les 5 fonctions ci-dessous pour que main.py fonctionne.
# Lance : python main.py
# Implémente-les dans l'ordre — commence par TODO 1.
# ============================================================


# ------------------------------------------------------------
# TODO 1 — [titre court et impératif — ex: "Manger fait baisser la faim"]
# ------------------------------------------------------------
# [2-3 phrases narratives : contexte concret dans l'univers du jeu,
#  enjeu de la fonction, ce qui se passe au cas limite.]
#
#   parametre1  : [ce que c'est en une ligne — ex: "la faim actuelle (0 à 100)"]
#   parametre2  : [ce que c'est en une ligne]
#
# nom_fonction(valeur1, valeur2)   =>  résultat_normal
# nom_fonction(valeur_limite, x)   =>  résultat_limite   (explication du cas)
#
# Indice : [nom exact de l'outil Python — ex: max(0, ...) / min(100, ...) / if / return]
# ------------------------------------------------------------
def nom_fonction(parametre1, parametre2):
    raise NotImplementedError  # supprime cette ligne et écris ton code ici


# [répéter pour TODO 2, TODO 3, TODO 4 et TODO 5]
```

**Règles pour les blocs TODO :**
- **Narrative d'abord** — 2-3 phrases qui posent le contexte et l'enjeu avant tout
- **Chaque paramètre expliqué** — une ligne par argument, alignées avec les espaces, entre la narrative et les exemples
- **Deux exemples avec `=>`** — le cas normal + le cas limite (valeur à 0, plafond à 100, liste vide, etc.)
- **Jamais les labels `Entrée :` / `Sortie :`** — utiliser la syntaxe d'appel directe avec `=>`
- L'indice donne le nom exact de l'outil sans donner l'implémentation
- Chaque fonction commence obligatoirement par `raise NotImplementedError`
- La première fonction doit être implémentable en 5-10 minutes
- **Noms de variables et fonctions en anglais** — seuls les commentaires et exemples sont en français

**Règles pour la progression dans la session :**
- TODO 1 : trivial — 2-3 lignes, aucun doute sur l'outil à utiliser
- TODO 2 : légèrement plus complexe — une condition ou une comparaison simple
- TODO 3 : intermédiaire — une boucle ou une accumulation
- TODO 4 : combine deux concepts vus dans les premières
- TODO 5 : le plus difficile — combine trois concepts, c'est normal de bloquer ici

---

### Étape 2 — Lancement

Après avoir généré les fichiers, afficher :

```
🔨  BUILD — ~1h.

Colle ça dans ton terminal :

  cd /Users/noah/Desktop/Python/YYYYMMDD/build

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

Ensuite, silencieusement :
1. Appender la section `## Build` dans `YYYYMMDD/recap.md`
2. `git add -A && git commit -m "YYYYMMDD build" && git push origin main`

---

## Banque de projets (inspiration — générer des variantes originales)

Chaque projet génère exactement 5 fonctions simples. Les exemples ci-dessous décrivent ce que les fonctions doivent faire — pas comment les implémenter.

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
