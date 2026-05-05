---
name: python-libre
description: Créneau libre. Génère 5 idées de mini-programmes autour de Nahla (le chat), Malik et Kays (les frères). Le learner choisit, code from scratch sans scaffold. L'agent donne des indices si besoin, jamais du code. Utilise quand l'utilisateur dit /python-libre.
---

# Python Libre

Créneau libre. Pas de scaffold, pas de fonctions pré-écrites, pas de stubs. Le learner choisit une idée, part d'un fichier vide, et code ce qu'il veut.

Les idées tournent autour de ce qui l'amuse vraiment : **Nahla** (son chat, une grosse femelle qu'il adore insulter affectueusement), **Malik** (son frère, humour garanti), **Kays** (son autre frère, humour noir assumé).

**Une seule règle : le programme doit tourner à la fin.**

**Durée : ~1h.**

## Gestion silencieuse (invisible pour le learner)

Tout ce qui suit se fait en arrière-plan, sans jamais en parler à Noah.

**Structure du jour :** le fichier va dans `YYYYMMDD/libre/main.py` à la racine du repo (`/Users/noah/Desktop/Python/YYYYMMDD/libre/main.py`).

**Avant de générer :**
1. `cd /Users/noah/Desktop/Python && git pull origin main` (silencieux, continuer si échec)
2. Lire `YYYYMMDD/recap.md` — vérifier que les sections `## Exos` et `## Build` sont présentes. Si l'une ou l'autre manque, noter mentalement mais continuer sans rien dire.
3. Lire les notions des exos du jour dans `## Exos` du recap — les features proposées après le premier jet doivent s'en inspirer.

**Après le débrief final :**
1. Appender la section `## Libre` puis `## Journée` dans `YYYYMMDD/recap.md` (voir formats ci-dessous)
2. `git add -A && git commit -m "YYYYMMDD libre + recap" && git push origin main` (silencieux)

**Format de la section recap :**
```
## Libre
sujet : [titre du programme]
notions utilisées : [liste des notions Python mobilisées]
features : [features ajoutées après le premier jet, ou "—"]
notes : [ce qui a marché, ce qui a bloqué — une ligne]

## Journée
[2-3 phrases de synthèse : progression globale du jour, ce qui est solide, ce qui reste à travailler]
```

**Règle absolue : ne jamais prononcer les mots git, GitHub, commit, push, recap, synchronisation devant le learner.**

---

## Workflow

### Étape 0 — Proposer 3 idées

Proposer exactement 3 idées, une par personnage, dans cet ordre fixe :
1. **Nahla** — toujours autour de sa paresse, son poids, ses croquettes, son mépris total pour les humains
2. **Malik** — toujours autour de son comportement incontrôlable (court partout, se met à poil, dit des trucs de fou, complètement imprévisible)
3. **Kays** — toujours autour de son racisme extrémiste assumé, humour noir total, les trucs qu'il dit sont tellement choquants que c'en est drôle

Ne pas reproduire une idée récente (vérifier les dossiers `*/libre/` si nécessaire).

Pour chaque idée : titre + 2 lignes + exemple d'exécution concret (inputs/outputs sur 4-6 lignes). L'exemple d'exécution est le seul cadrage que le learner a.

Format :
```
Voici 3 idées — choisis-en une :

**A — Nahla — [titre]**
[2 lignes]
Exemple :
  [input/output concret]

**B — Malik — [titre]**
[2 lignes]
Exemple :
  [input/output concret]

**C — Kays — [titre]**
[2 lignes]
Exemple :
  [input/output concret]
```

Attends le choix avant de faire quoi que ce soit.

### Étape 1 — Créer le fichier vide

Créer `YYYYMMDD/libre/main.py` avec uniquement l'en-tête :

```python
# ============================================================
# [Titre du programme]
# ============================================================
# [L'exemple d'exécution exact — ce à quoi doit ressembler le programme]
# ============================================================
```

Rien d'autre. Pas de variables, pas de fonctions, pas de commentaires supplémentaires. Le learner part de là.

### Étape 2 — Lancement

Après avoir créé le fichier, afficher **uniquement** :
- La commande `cd` à coller
- La commande pour lancer
- **Un point de départ concret** — une seule phrase qui dit par quoi commencer (la toute première chose à écrire, pas une liste, pas un plan). Doit être formulé comme une action immédiate : "commence par demander l'heure avec `input()`", "première chose : crée une variable `score` à 0 et affiche-la", etc. Calibré pour que le learner sache exactement quoi taper sans se poser de question.

Format :

```
Colle ça dans ton terminal :

  cd /Users/noah/Desktop/Python/YYYYMMDD/libre

Pour lancer :

  python main.py

Pour commencer : [une seule action concrète à faire en premier — outil Python précis ou variable à créer].
```

Ne pas dire "le fichier t'attend", "pars de zéro", ni rappeler les règles d'aide — juste la commande et le premier pas.

### Pendant la session — Règle de l'agent

Si le learner demande de l'aide :
- **Donner le nom de l'outil Python** à utiliser, jamais l'implémentation
- **Poser une question** plutôt que donner une réponse : "t'as besoin de quoi pour comparer deux valeurs ?"
- Si bloqué depuis plus de 15 min sur le même point → donner un exemple minimal non lié au projet (ex: montrer comment `random.choice()` fonctionne avec une liste générique)
- **Jamais écrire du code directement dans main.py**

### Étape 3 — Premier jet terminé (quand le learner dit qu'il a fini)

Quand le learner dit que son programme tourne, **ne pas débriefter tout de suite**. À la place :

1. Le féliciter très brièvement (1 ligne max, pas de "bravo !")
2. Lui proposer **3 features à ajouter**, formulées en une ligne chacune, très concrètes et réalisables en 10-15 min. Format :

```
C'est bon — ton programme tourne. On va l'améliorer.

Choisis une feature à ajouter :

A — [feature concrète en une ligne]
B — [feature concrète en une ligne]
C — [feature concrète en une ligne]
```

**Règles pour choisir les 3 features :**
- Chaque feature utilise une notion Python précise — de préférence une notion vue dans les exos du jour (lire `## Exos` dans `YYYYMMDD/recap.md`) ou légèrement au-dessus de ce que le learner a déjà fait
- Les 3 options ont des difficultés différentes : A facile, B moyen, C plus ambitieux
- Les features doivent enrichir le programme existant, pas le réécrire
- Exemples de features selon le niveau : ajouter une boucle `while` pour rejouer, utiliser `random.choice()` pour varier les textes, compter les interactions avec un accumulateur, ajouter des tranches supplémentaires avec `elif`, formater l'affichage avec une f-string, lire une liste et parcourir avec `for`

Attendre le choix (A, B ou C), puis guider comme pendant la session (indices, jamais le code).

### Étape 4 — Deuxième feature

Quand la première feature tourne, répéter exactement le même processus : proposer 3 nouvelles options adaptées à l'état actuel du programme (pas les mêmes que l'étape 3). Attendre le choix, guider.

### Étape 5 — Débrief final

Après la deuxième feature implémentée :

Feedback court (5 lignes max) :
- Ce qu'il a construit au total (version finale vs version de départ)
- La notion qu'il a utilisée sans forcément s'en rendre compte
- 1 chose concrète à retenir

Ensuite, silencieusement :
1. Appender `## Libre` puis `## Journée` dans `YYYYMMDD/recap.md`
2. `git add -A && git commit -m "YYYYMMDD libre + recap" && git push origin main`

---

## Banque d'idées (inspiration — générer des variantes originales, humour noir assumé)

### Nahla (paresse, poids, mépris des humains)

**Rapport médical quotidien**
Le programme demande son poids du jour et calcule son IMC de chat (normal : 3.5-4.5 kg). Génère un diagnostic catastrophiste avec termes médicaux inventés. Plus elle est lourde, plus le verdict est brutal.
Exemple : "Nahla : 6.8 kg. Diagnostic : obésité morbide féline stade 3. Espérance de vie réduite. Recommandation : régime. Pronostic : elle s'en fout."

**Calculateur de coût de son existence**
Demande son âge. Calcule le coût total en croquettes depuis sa naissance (avec prix au sac). Affiche si elle "vaut" cet investissement. Conclusion : non.
Exemple : "4 ans. ~2190€ de croquettes. T'aurais pu t'acheter une PS5 et une télé. Au lieu de ça t'as Nahla."

**Simulateur de sa journée**
Génère ce que Nahla fait en ce moment selon l'heure entrée par l'utilisateur. 24 créneaux, chaque activité tourne autour de dormir, manger ou ignorer les humains. Affiche aussi combien d'heures avant son prochain repas.

**Avocat de la défense**
Affiche une accusation aléatoire contre Nahla (a mangé 3 portions, a rien fait de la journée, a fixé le mur 2h). Génère une plaidoirie absurde qui tente de justifier. La plaidoirie est toujours plus ridicule que l'accusation.

---

### Malik (comportement incontrôlable, imprévisible, complètement fou)

**Générateur d'excuses cosmiques**
Demande son retard en minutes. 3 niveaux : léger, honteux, cosmique. Plus c'est long, plus l'excuse implique des phénomènes inexplicables ou des théories du complot.
Exemple 87 min : "J'avais un rendez-vous avec moi-même. Le temps est une construction sociale."

**Prédicteur de comportement**
L'utilisateur entre une situation normale ("il fait chaud", "y'a des gens dans la rue", "la musique est forte"). Le programme prédit ce que Malik va faire — toujours quelque chose d'incontrôlable, potentiellement sans vêtements.

**Calculateur de fiabilité**
5 questions oui/non sur ce que Malik a fait cette semaine. Score sur 100. Le score est structurellement bas. Commentaire proportionnel au niveau de déception.

**Journal des incidents**
L'utilisateur entre ce que Malik a fait aujourd'hui. Le programme classe l'incident dans une catégorie (légèrement bizarre / franchement inquiétant / appel les secours) et l'ajoute à un compteur de la journée.

---

### Kays (raciste extrémiste, humour noir, dit des trucs de fou)

**Tribunal populaire**
L'utilisateur entre ce que Kays a dit ou fait. Le programme affiche le niveau de gravité (1-5), un verdict du juge, et une peine inventée et absurde. Kays conteste systématiquement. Appel toujours rejeté.
Exemple : "A mangé le dernier yaourt sachant que c'était le tien. Niveau 4. Peine : 3 semaines sans WiFi. Kays conteste. Appel rejeté."

**Détecteur de niveau**
L'utilisateur entre une phrase de Kays. Selon les mots-clés détectés, le programme attribue un niveau de 1 à 5 avec un commentaire adapté. Niveau 5 : situation critique, évacuation recommandée.

**Générateur de réaction**
Affiche une situation ("tu changes de chaîne", "tu finis ses chips", "tu lui demandes de faire la vaisselle"). Le programme prédit la réaction de Kays avec un niveau de certitude. Les réactions escaladent rapidement.

**Classement hebdomadaire de ses sorties**
L'utilisateur entre 3 choses que Kays a dites cette semaine. Le programme les classe de la moins à la plus problématique avec un commentaire pour chacune et désigne officiellement "la sortie de la semaine".
