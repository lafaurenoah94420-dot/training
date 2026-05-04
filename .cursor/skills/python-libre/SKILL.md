---
name: python-libre
description: Créneau libre. Génère 5 idées de mini-programmes autour de Nahla (le chat), Malik et Kays (les frères). Le learner choisit, code from scratch sans scaffold. L'agent donne des indices si besoin, jamais du code. Utilise quand l'utilisateur dit /python-libre.
---

# Python Libre

Créneau libre. Pas de scaffold, pas de fonctions pré-écrites, pas de stubs. Le learner choisit une idée, part d'un fichier vide, et code ce qu'il veut.

Les idées tournent autour de ce qui l'amuse vraiment : **Nahla** (son chat, une grosse femelle qu'il adore insulter affectueusement), **Malik** (son frère, humour garanti), **Kays** (son autre frère, humour noir assumé).

**Une seule règle : le programme doit tourner à la fin.**

**Durée : ~1h.**

---

## Workflow

### Étape 0 — Proposer 3 idées

Proposer exactement 3 idées, une par personnage, dans cet ordre fixe :
1. **Nahla** — toujours autour de sa paresse, son poids, ses croquettes, son mépris total pour les humains
2. **Malik** — toujours autour de son comportement incontrôlable (court partout, se met à poil, dit des trucs de fou, complètement imprévisible)
3. **Kays** — toujours autour de son racisme extrémiste assumé, humour noir total, les trucs qu'il dit sont tellement choquants que c'en est drôle

Ne pas reproduire une idée récente (vérifier `libres/` si nécessaire).

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

Créer `libres/YYYYMMDD-libre-[slug]/main.py` avec uniquement l'en-tête :

```python
# ============================================================
# [Titre du programme]
# ============================================================
# [L'exemple d'exécution exact — ce à quoi doit ressembler le programme]
# ============================================================
```

Rien d'autre. Pas de variables, pas de fonctions, pas de commentaires supplémentaires. Le learner part de là.

### Étape 2 — Lancement

```
🆓  LIBRE — ~1h.

Colle ça dans ton terminal :

  cd /Users/byronlove/Desktop/dev/python-noah/libres/YYYYMMDD-libre-[slug]

Pour lancer ton programme :

  python main.py

Le fichier main.py t'attend. Parte de zéro.
Tu peux me demander de l'aide — je te donne des indices, pas du code.
Dis-moi quand t'as fini ou quand t'en peux plus.
```

### Pendant la session — Règle de l'agent

Si le learner demande de l'aide :
- **Donner le nom de l'outil Python** à utiliser, jamais l'implémentation
- **Poser une question** plutôt que donner une réponse : "t'as besoin de quoi pour comparer deux valeurs ?"
- Si bloqué depuis plus de 15 min sur le même point → donner un exemple minimal non lié au projet (ex: montrer comment `random.choice()` fonctionne avec une liste générique)
- **Jamais écrire du code directement dans main.py**

### Étape 3 — Débrief (quand le learner a fini ou abandonné)

Demander de coller la sortie de `python main.py`.

Feedback court (5 lignes max) :
- Ce qu'il a réussi à construire seul
- Le moment où il a bloqué et pourquoi
- 1 truc qu'il a utilisé sans s'en rendre compte (une notion des exos ou du build)

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
