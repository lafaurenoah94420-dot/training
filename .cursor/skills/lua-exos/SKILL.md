---
name: lua-exos
description: Génère 5 petits exercices Lua indépendants, un par fichier, difficulté croissante. Chaque exercice cible une seule notion. Vérification par assert. Contexte jeux vidéo (TLOU, RE, GTA, Zomboid, HOI4). Utilise quand l'utilisateur dit /lua-exos.
---

# Lua Exos

5 fichiers, 5 notions différentes, difficulté croissante. Chaque fichier = un seul concept, un contexte jeu vidéo, une vérification par `assert`. Le learner lance chaque fichier, corrige jusqu'à voir `✅ Correct !`, puis passe au suivant. Il s'arrête où il bloque — c'est normal.

**Durée : ~45 min.**

## Gestion silencieuse (invisible pour le learner)

Tout ce qui suit se fait en arrière-plan, sans jamais en parler à Noah.

**Structure du jour :** tous les fichiers vont dans `YYYYMMDD/exos/` à la racine du repo (`/Users/noah/Desktop/Python/YYYYMMDD/exos/`). Le dossier `YYYYMMDD/` est le dossier du jour — il contient aussi `build/`, `libre/` et `recap.md`.

**Avant de générer :**
1. `cd /Users/noah/Desktop/Python && git pull origin main` (silencieux, continuer si échec)
2. Scanner tous les dossiers `YYYYMMDD/` existants dans le repo (triés du plus ancien au plus récent). Lire les `recap.md` et les fichiers des sessions précédentes pour comprendre le niveau réel de Noah : quelles notions il maîtrise, sur lesquelles il bloque régulièrement, jusqu'où il va en général dans les exos. Ce contexte sert à calibrer les notions choisies aujourd'hui et la difficulté des exercices.

**Après le débrief :** `git add -A && git commit -m "YYYYMMDD exos" && git push origin main` (silencieux)

**Recap :**
Après le débrief, ajouter silencieusement la section suivante à `YYYYMMDD/recap.md` (créer le fichier s'il n'existe pas, sinon appender) :

```
# YYYY-MM-DD

## Exos
notions : [liste des 5 notions du jour séparées par des virgules]
score : [X]/5
bloqué : [notion du fichier où il a bloqué, ou "—" si tout fini]
notes : [une phrase sur ce qui était solide et ce qui reste fragile]
```

**Règle absolue : ne jamais prononcer les mots git, GitHub, commit, push, recap, synchronisation devant le learner.**

---

## Workflow

### Étape 0 — Choisir les 5 notions

Avant de générer quoi que ce soit, vérifier `YYYYMMDD/recap.md` si le fichier existe — pour voir les notions déjà travaillées récemment et ne pas répéter une notion utilisée dans les 2 dernières sessions.

Choisir 5 notions dans le pool ci-dessous, dans un ordre de difficulté croissante pour la session. Pas besoin de proposer des choix — générer directement.

**Pool de notions :**
- Variables et calcul simple
- Conditions `if / elseif / else / end`
- Boucle `for` sur une table avec `ipairs`
- Boucle `for` numérique (`for i = 1, n do`)
- Fonction simple avec `return`
- Fonction avec paramètres multiples
- `io.read()` et conversion `tonumber()`
- String : `string.upper()`, `string.lower()`, `string.gsub()`, opérateur `#`
- Tables (listes) : `table.insert()`, `#`, accès par index
- `math.random()` (avec `math.randomseed(os.time())` si besoin)
- Condition dans une boucle (`for` + `if`)
- `while` avec condition d'arrêt (`while ... do ... end`)
- Valeur par défaut dans une fonction (`param = param or valeur`)
- Boucle qui accumule un résultat (compteur, somme)
- Concaténation / format : `"Joel a " .. vie .. " points de vie"` ou `string.format`
- Table associative (dict) : lire et écrire une clé (`t["cle"]`, `t["cle"] = valeur`)
- Test de présence : boucle `ipairs` pour chercher un élément, ou `t[element]`

Règle de progression dans la session :
- Fichier 01 : notion triviale (variables, calcul, string simple)
- Fichier 02 : notion légèrement plus complexe (condition, table basique)
- Fichier 03 : notion intermédiaire (boucle, fonction simple)
- Fichier 04 : combinaison de deux notions vues précédemment
- Fichier 05 : combinaison plus exigeante — c'est normal de bloquer ici

### Étape 1 — Générer les fichiers

Créer `YYYYMMDD/exos/` avec 5 fichiers :

```
YYYYMMDD/
└── exos/
    ├── 01_[notion].lua
    ├── 02_[notion].lua
    ├── 03_[notion].lua
    ├── 04_[notion].lua
    └── 05_[notion].lua
```

Pas d'instructions séparées — tout est dans chaque fichier.

---

### Règles de conception de chaque fichier

**Structure type :**

```lua
-- ============================================================
-- [Jeu] — [situation courte]
-- ============================================================
-- [2-3 phrases narratives : personnage, contexte, enjeu concret.
--  Le learner doit comprendre POURQUOI ce calcul existe dans le jeu.]
--
-- Lance : lua 0X_[notion].lua
-- ============================================================

-- [données déjà définies si nécessaire]
-- [variable de départ = 0 ou ""]

-- [Ce que tu dois faire, formulé comme une action]
--
-- [déroulé pas à pas avec les valeurs réelles]
--
-- Résultat attendu : [variable] == [valeur]
--
-- Indice : [nom exact de l'outil Lua — jamais l'implémentation]

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert([variable] == [valeur], "[message d'erreur utile en français]")
print("✅ Correct !")
```

**Règles absolues :**
- **Une seule notion par fichier** — si le fichier 03 porte sur les boucles, pas de condition dans la boucle
- **Le learner ne doit écrire que 1 à 4 lignes** — jamais plus pour résoudre l'exercice
- Le bloc `-- --- Vérification ---` est déjà écrit — le learner ne le touche pas
- Les messages d'assert sont utiles : `"Recompte : 30 - 7 + 3 = ?"` pas `"Erreur"`
- Contexte jeu vidéo dans le titre et les variables — mais les noms de variables restent en anglais
- Textes affichés et commentaires en français
- L'indice donne le nom de l'outil (`for`, `if`, `+=` n'existe pas en Lua → `x = x + 1`, `string.upper`, etc.) — jamais la ligne de code

**Règle centrale pour la consigne :**
Le bloc de consigne doit montrer le déroulé pas à pas avec les valeurs réelles du fichier — pas une formule abstraite. Le learner doit pouvoir lire les commentaires et comprendre exactement ce qui doit se passer à chaque étape, sans avoir à le déduire.

- Pour un **calcul** : montrer chaque opération sur une ligne avec le résultat intermédiaire
- Pour une **condition** : montrer chaque cas (`pv = 18 → 18 > 0 ? oui → statut = "En vie"`)
- Pour une **boucle for** : dérouler chaque tour avec la valeur de la variable et l'état de l'accumulateur
- Pour un **while** : dérouler chaque tour avec l'état de toutes les variables impliquées
- Pour une **fonction** : montrer l'appel avec les vraies valeurs et le résultat avec `=>`

**Format selon la notion :**

*Variables et calcul :*
```lua
-- ============================================================
-- The Last of Us — munitions de Joel
-- ============================================================
-- Joel part avec 30 balles. Il en tire 7 sur des infectés.
-- Il fouille un cadavre et récupère 3 balles supplémentaires.
-- Combien lui en reste-t-il ?
--
-- Lance : lua 01_calcul.lua
-- ============================================================

balles_restantes = 0

-- Calcule les balles restantes avec une seule expression.
--
-- 30 - 7 = 23   (après les tirs)
-- 23 + 3 = 26   (après avoir récupéré des balles)
--
-- Résultat attendu : balles_restantes == 26
--
-- Indice : une expression avec - et +

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(balles_restantes == 26, "Recompte : 30 - 7 + 3 = ?")
print("✅ Correct !")
```

*Condition if/else :*
```lua
-- ============================================================
-- Resident Evil — statut médical
-- ============================================================
-- L'écran médical affiche "En vie" si les PV sont supérieurs à 0,
-- "Mort" sinon. Leon vient d'être touché — vérifie son statut.
--
-- Lance : lua 02_condition.lua
-- ============================================================

vie = 15
message = ""

-- Détermine le message selon la valeur de vie.
--
-- vie = 15  →  15 > 0 ? oui  →  message = "Joel est vivant"
-- vie = 0   →  0 > 0  ? non  →  message = "Joel est mort"
--
-- Résultat attendu : message == "Joel est vivant"  (car vie vaut 15 ici)
--
-- Indice : if / else / end

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(message == "Joel est vivant", "Obtenu : '" .. message .. "'")
print("✅ Correct !")
```

*Boucle for sur une table :*
```lua
-- ============================================================
-- GTA — bilan de missions
-- ============================================================
-- Franklin vient de finir sa session. À chaque mission il a infligé
-- des dégâts. Le jeu doit calculer le total pour son classement.
--
-- Lance : lua 03_for_liste.lua
-- ============================================================

degats = {5, 12, 3, 8, 20}
total_degats = 0

-- Parcours la table degats et additionne chaque valeur dans total_degats.
--
-- tour 1 : x = 5   →  total_degats = 0 + 5  = 5
-- tour 2 : x = 12  →  total_degats = 5 + 12 = 17
-- tour 3 : x = 3   →  total_degats = 17 + 3 = 20
-- tour 4 : x = 8   →  total_degats = 20 + 8 = 28
-- tour 5 : x = 20  →  total_degats = 28 + 20 = 48
--
-- Résultat attendu : total_degats == 48
--
-- Indice : for _, x in ipairs(...) do ... end  +  total_degats = total_degats + x

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(total_degats == 48, "Obtenu : " .. total_degats .. ", attendu : 48")
print("✅ Correct !")
```

*Fonction simple :*
```lua
-- ============================================================
-- The Last of Us — kit de soin
-- ============================================================
-- Joel utilise un kit de soin. La fonction calcule la nouvelle vie
-- après soin. Elle ne peut jamais dépasser 100 — c'est le maximum.
--
-- Lance : lua 03_fonction.lua
-- ============================================================

--   vie   : les points de vie actuels de Joel
--   soin  : les points récupérés grâce au kit
--
-- soigner(60, 20)  →  60 + 20 = 80   →  retourne 80
-- soigner(90, 20)  →  90 + 20 = 110  →  plafonné à 100, retourne 100
--
-- Résultat attendu : soigner(60, 20) == 80  et  soigner(90, 20) == 100
--
-- Indice : return + math.min(100, ...)

function soigner(vie, soin)
    -- remplace ce commentaire par ton code
end


-- --- Vérification (ne pas modifier) ---
assert(soigner(60, 20) == 80, "soigner(60, 20) doit retourner 80")
assert(soigner(90, 20) == 100, "soigner(90, 20) doit retourner 100, pas 110")
print("✅ Correct !")
```

*String :*
```lua
-- ============================================================
-- The Last of Us — affichage du nom
-- ============================================================
-- L'interface du jeu affiche les noms des personnages en majuscules.
-- Transforme le nom de Joel pour l'affichage.
--
-- Lance : lua 02_string.lua
-- ============================================================

nom = "joel miller"
nom_affiche = ""

-- Transforme nom en majuscules et stocke le résultat dans nom_affiche.
--
-- "joel miller"  →  chaque lettre passe en majuscule  →  "JOEL MILLER"
--
-- Résultat attendu : nom_affiche == "JOEL MILLER"
--
-- Indice : string.upper()

-- À toi :


-- --- Vérification (ne pas modifier) ---
assert(nom_affiche == "JOEL MILLER", "Obtenu : '" .. nom_affiche .. "'")
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

  cd /Users/noah/Desktop/Python/YYYYMMDD/exos

Puis pour lancer chaque exercice :

  lua 01_[notion].lua
  lua 02_[notion].lua
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

Ensuite, silencieusement :
1. Appender la section `## Exos` dans `YYYYMMDD/recap.md`
2. `git add -A && git commit -m "YYYYMMDD exos" && git push origin main`
