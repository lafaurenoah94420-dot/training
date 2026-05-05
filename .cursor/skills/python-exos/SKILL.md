---
name: python-exos
description: Génère 5 petits exercices Python indépendants, un par fichier, difficulté croissante. Chaque exercice cible une seule notion. Vérification par assert. Contexte jeux vidéo (TLOU, RE, GTA, Zomboid, HOI4). Utilise quand l'utilisateur dit /python-exos.
---

# Python Exos

5 fichiers, 5 notions différentes, difficulté croissante. Chaque fichier = un seul concept, un contexte jeu vidéo, une vérification par `assert`. Le learner lance chaque fichier, corrige jusqu'à voir `✅ Correct !`, puis passe au suivant. Il s'arrête où il bloque — c'est normal.

**Durée : ~45 min.**

## GitHub — gestion automatique par l’agent (invisible pour le learner)

Le learner ne sait pas ce qu’est GitHub et ne doit **jamais** voir de commandes git ni entendre parler de commit, push ou synchronisation. **L’agent gère tout en arrière-plan, silencieusement, sans jamais le mentionner.**

**Repo :** `/Users/noah/Desktop/Python` — remote : `origin/main`

**Avant de générer les fichiers :** exécuter silencieusement `cd /Users/noah/Desktop/Python && git pull origin main`. Si le pull échoue, continuer quand même.

**Après le débrief :** exécuter silencieusement `cd /Users/noah/Desktop/Python && git add -A && git commit -m "[session]: YYYYMMDD" && git push origin main`. Si rien à commiter, ne rien faire.

**Règle absolue : ne jamais prononcer les mots git, GitHub, commit, push, synchronisation devant le learner. Ces mots n’existent pas dans la conversation avec lui.**

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
# [Jeu] — [situation courte]
# ============================================================
# [2-3 phrases narratives : personnage, contexte, enjeu concret.
#  Le learner doit comprendre POURQUOI ce calcul existe dans le jeu.]
#
# Lance : python 0X_[notion].py
# ============================================================

[données déjà définies si nécessaire]
[variable de départ = 0 ou ""]

# [Ce que tu dois faire, formulé comme une action]
#
# [exemple avec les valeurs réelles]  =>  [résultat attendu]
# [cas limite si pertinent]           =>  [résultat attendu]
#
# Indice : [nom exact de l'outil Python — jamais l'implémentation]

# À toi :


# --- Vérification (ne pas modifier) ---
assert [variable] == [valeur], "[message d'erreur utile en français]"
print("✅ Correct !")
```

**Règles absolues :**
- **Une seule notion par fichier** — si le fichier 03 porte sur les boucles, pas de condition dans la boucle
- **Le learner ne doit écrire que 1 à 4 lignes** — jamais plus pour résoudre l'exercice
- Le bloc `# --- Vérification ---` est déjà écrit — le learner ne le touche pas
- Les messages d'assert sont utiles : `"Recompte : 30 - 7 + 3 = ?"` pas `"Erreur"`
- Contexte jeu vidéo dans le titre et les variables — mais les noms de variables restent en anglais
- Textes affichés et commentaires en français
- L'exemple avec `=>` utilise toujours les valeurs réelles du fichier — jamais des valeurs inventées
- L'indice donne le nom de l'outil (`for`, `if`, `+=`, `.upper()`, etc.) — jamais la ligne de code

**Format selon la notion :**

*Variables et calcul :*
```python
# ============================================================
# The Last of Us — munitions de Joel
# ============================================================
# Joel part avec 30 balles. Il en tire 7 sur des infectés.
# Il fouille un cadavre et récupère 3 balles supplémentaires.
# Combien lui en reste-t-il ?
#
# Lance : python 01_calcul.py
# ============================================================

balles_restantes = 0

# Calcule les balles restantes après le combat
#
# 30 - 7 + 3  =>  balles_restantes == 26
#
# Indice : une expression avec - et +

# À toi :


# --- Vérification (ne pas modifier) ---
assert balles_restantes == 26, "Recompte : 30 - 7 + 3 = ?"
print("✅ Correct !")
```

*Condition if/else :*
```python
# ============================================================
# Resident Evil — statut médical
# ============================================================
# L'écran médical affiche "En vie" si les PV sont supérieurs à 0,
# "Mort" sinon. Leon vient d'être touché — vérifie son statut.
#
# Lance : python 02_condition.py
# ============================================================

vie = 15
message = ""

# Détermine le message selon la valeur de vie
#
# avec vie = 15  =>  message == "Joel est vivant"
# avec vie = 0   =>  message == "Joel est mort"
#
# Indice : if / else

# À toi :


# --- Vérification (ne pas modifier) ---
assert message == "Joel est vivant", f"Obtenu : '{message}'"
print("✅ Correct !")
```

*Boucle for sur une liste :*
```python
# ============================================================
# GTA — bilan de missions
# ============================================================
# Franklin vient de finir sa session. À chaque mission il a infligé
# des dégâts. Le jeu doit calculer le total pour son classement.
#
# Lance : python 03_for_liste.py
# ============================================================

degats = [5, 12, 3, 8, 20]
total_degats = 0

# Additionne tous les éléments de degats dans total_degats
#
# pour [5, 12, 3, 8, 20]  =>  total_degats == 48
#
# Indice : boucle for + +=

# À toi :


# --- Vérification (ne pas modifier) ---
assert total_degats == 48, f"Obtenu : {total_degats}, attendu : 48"
print("✅ Correct !")
```

*Fonction simple :*
```python
# ============================================================
# The Last of Us — kit de soin
# ============================================================
# Joel utilise un kit de soin. La fonction doit calculer la nouvelle vie
# après soin — sans jamais dépasser 100 (la vie maximale).
#
# Lance : python 03_fonction.py
# ============================================================

# Écris la fonction soigner(vie, soin) qui retourne la nouvelle vie
#
# soigner(60, 20)  =>  80
# soigner(90, 20)  =>  100  (pas 110 — plafonné à 100)
#
# Indice : return + max ou min selon le plafond

def soigner(vie, soin):
    pass  # remplace pass par ton code


# --- Vérification (ne pas modifier) ---
assert soigner(60, 20) == 80, "soigner(60, 20) doit retourner 80"
assert soigner(90, 20) == 100, "soigner(90, 20) doit retourner 100, pas 110"
print("✅ Correct !")
```

*String :*
```python
# ============================================================
# The Last of Us — affichage du nom
# ============================================================
# L'interface du jeu affiche les noms des personnages en majuscules.
# Transforme le nom de Joel pour l'affichage.
#
# Lance : python 02_string.py
# ============================================================

nom = "joel miller"
nom_affiche = ""

# Mets nom en majuscules et stocke le résultat dans nom_affiche
#
# "joel miller"  =>  nom_affiche == "JOEL MILLER"
#
# Indice : .upper()

# À toi :


# --- Vérification (ne pas modifier) ---
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

  cd /Users/noah/Desktop/Python/exos/YYYYMMDD-exos-[slug]

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

**Git (en arrière-plan, sans en parler) :** après le débrief, exécuter `git add -A && git commit -m "exos: session YYYYMMDD" && git push origin main` depuis `/Users/noah/Desktop/Python`. Ne rien mentionner au learner.
