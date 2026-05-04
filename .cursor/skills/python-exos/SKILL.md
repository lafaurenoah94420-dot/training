---
name: python-exos
description: Génère 5 petits exercices Python indépendants, un par fichier, difficulté croissante. Chaque exercice cible une seule notion. Vérification par assert. Contexte jeux vidéo (TLOU, RE, GTA, Zomboid, HOI4). Utilise quand l'utilisateur dit /python-exos.
---

# Python Exos

5 fichiers, 5 notions différentes, difficulté croissante. Chaque fichier = un seul concept, un contexte jeu vidéo, une vérification par `assert`. Le learner lance chaque fichier, corrige jusqu'à voir `✅ Correct !`, puis passe au suivant. Il s'arrête où il bloque — c'est normal.

**Durée : ~45 min.**

---

## Workflow

### Étape 0 — Choisir les 5 notions

Avant de générer quoi que ce soit, vérifier le dossier `exos/` pour voir les sessions récentes et **ne pas répéter une notion utilisée dans les 2 dernières sessions**.

Choisir 5 notions dans le pool ci-dessous, dans un ordre de difficulté croissante pour la session. Pas besoin de proposer des choix — générer directement.

**Pool de notions :**
- Variables et calcul simple
- Conditions `if / elif / else`
- Boucle `for` sur une liste
- Boucle `for` avec `range()`
- Fonction simple avec `return`
- Fonction avec paramètres multiples
- `input()` et conversion `int()` / `float()`
- String : `.upper()`, `.lower()`, `.replace()`, `len()`
- Listes : `append()`, `len()`, accès par index
- `random.randint()` ou `random.choice()`
- Condition dans une boucle (`for` + `if`)
- `while` avec condition d'arrêt
- Valeur par défaut dans une fonction
- Boucle qui accumule un résultat (compteur, somme)
- f-strings : `f"Joel a {vie} points de vie"`
- Dictionnaire simple : lire et écrire une clé (`dict["cle"]`, `dict["cle"] = valeur`)
- `in` keyword : `if element in liste`, `for x in liste`

Règle de progression dans la session :
- Fichier 01 : notion triviale (variables, calcul, string simple)
- Fichier 02 : notion légèrement plus complexe (condition, liste basique)
- Fichier 03 : notion intermédiaire (boucle, fonction simple)
- Fichier 04 : combinaison de deux notions vues précédemment
- Fichier 05 : combinaison plus exigeante — c'est normal de bloquer ici

### Étape 1 — Générer les fichiers

Créer `exos/YYYYMMDD-exos-[slug]/` avec 5 fichiers :

```
exos/YYYYMMDD-exos-[slug]/
├── 01_[notion].py
├── 02_[notion].py
├── 03_[notion].py
├── 04_[notion].py
└── 05_[notion].py
```

Pas de BRIEF.md — les instructions sont dans chaque fichier.

---

### Règles de conception de chaque fichier

**Structure type :**

```python
# ============================================================
# [Titre dans le contexte du jeu vidéo]
# ============================================================
# [2 lignes de contexte — jeu vidéo, situation concrète]
#
# Résultat attendu quand tu lances ce fichier :
#   [output exact ligne par ligne]
# ============================================================


# À toi :
[variable ou fonction à compléter] = 0  # remplace ce 0 par ton code


# --- Vérification (ne pas modifier) ---
assert [variable] == [valeur], "[message d'erreur utile en français]"
print("✅ Correct !")
```

**Règles absolues :**
- **Une seule notion par fichier** — si le fichier 03 porte sur les boucles, pas de condition dans la boucle
- **Le learner ne doit écrire que 1 à 4 lignes** — jamais plus pour résoudre l'exercice
- Le bloc `# --- Vérification ---` est déjà écrit — le learner ne le touche pas
- Les messages d'assert sont utiles : `"Résultat obtenu différent de 26 — recompte les balles"` pas `"Erreur"`
- Contexte jeu vidéo dans le titre et les variables — mais les noms de variables restent en anglais
- Textes affichés et commentaires en français

**Format selon la notion :**

*Variables et calcul :*
```python
# Joel commence avec 30 balles. Il tire 7 fois. Il ramasse 3 balles.
# Calcule les balles restantes et stocke le résultat dans balles_restantes.

# À toi :
balles_restantes = 0

assert balles_restantes == 26, "Recompte : 30 - 7 + 3 = ?"
print("✅ Correct !")
```

*Condition if/else :*
```python
# vie vaut 15. Si vie > 0, message vaut "Joel est vivant". Sinon "Joel est mort".

vie = 15

# À toi :
message = ""

assert message == "Joel est vivant", f"Obtenu : '{message}'"
print("✅ Correct !")
```

*Boucle for sur une liste :*
```python
# Additionne tous les dégâts dans la liste. Stocke le résultat dans total_degats.

degats = [5, 12, 3, 8, 20]
total_degats = 0

# À toi — utilise une boucle for :

assert total_degats == 48, f"Obtenu : {total_degats}, attendu : 48"
print("✅ Correct !")
```

*Fonction simple :*
```python
# Écris la fonction soigner() qui prend une vie actuelle et des points de soin,
# et retourne la nouvelle vie (sans dépasser 100).

# À toi :
def soigner(vie, soin):
    pass

assert soigner(60, 20) == 80, "soigner(60, 20) doit retourner 80"
assert soigner(90, 20) == 100, "soigner(90, 20) doit retourner 100, pas 110"
print("✅ Correct !")
```

*String :*
```python
# Le nom du personnage est "joel miller". Mets-le en majuscules.
# Stocke le résultat dans nom_affiche.

nom = "joel miller"

# À toi :
nom_affiche = ""

assert nom_affiche == "JOEL MILLER", f"Obtenu : '{nom_affiche}'"
print("✅ Correct !")
```

---

### Étape 2 — Lancement

Après avoir généré les fichiers, afficher :

```
📁  5 exercices générés.

Notions :
  01 — [notion]
  02 — [notion]
  03 — [notion]
  04 — [notion]
  05 — [notion]

Colle ça dans ton terminal :

  cd /Users/byronlove/Desktop/dev/python-noah/exos/YYYYMMDD-exos-[slug]

Puis pour lancer chaque exercice :

  python 01_[notion].py
  python 02_[notion].py
  (etc.)

✅  Objectif : voir "✅ Correct !" sur chaque fichier.
Commence par 01. Arrête-toi quand tu bloques — c'est normal de pas finir les 5.
Dis-moi quand tu as fini ou si tu es bloqué.
```

### Étape 3 — Débrief (quand l'utilisateur a fini)

Demander jusqu'où il est allé (quel fichier).

Feedback court (5 lignes max) :
- Jusqu'où il est allé et ce que ça dit de son niveau actuel
- La notion sur laquelle il a bloqué et pourquoi c'est normal
- Ce qu'il faut retenir avant la prochaine session
