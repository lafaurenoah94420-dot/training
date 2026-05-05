# Build — Project Zomboid : jauge de faim

## Ce que tu vas construire

Un petit simulateur texte de la faim : manger fait baisser la jauge, le temps qui passe la fait monter (avec un maximum à 100), puis un message qui résume la situation. `main.py` enchaîne des situations comme dans une journée de survie.

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

Pour borner une valeur : soit des `if` qui corrigent le résultat, soit par exemple `max(0, …)` pour ne pas descendre sous 0 et `min(100, …)` pour ne pas dépasser 100 — à toi de voir ce que ton cours a déjà vu.

</details>
