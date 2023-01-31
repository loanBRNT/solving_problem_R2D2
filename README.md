# Solving problem R2D2
 
R2D2 est un robot placé dans un monde 2D représenté par un graphe non orienté : les arêtes
représentent les routes que R2D2 peut suivre, alors que les sommets représentent les lieux où
R2D2 a des choses à faire. Les arêtes seront pondérées pour représenter la longueur du chemin
que doit parcourir R2D2 pour aller du sommet origine de l’arête au sommet arrivée de l’arête. Et
chaque sommet est pondéré par sa position dans le plan 2D du monde (coordonnées euclidiennes).
On prendra comme hypothèse que R2D2 connaît le monde dans lequel il est placé.
Le travail que doit faire R2D2 : déposer 1 cube de couleur à chaque lieu de manière à ce qu’il y
ait dans deux lieux voisins (c-à-d liés par une arête) des cubes de couleur différente.
On considérera que R2D2 dispose de suffisamment de cubes.
Le travail de R2D2 va se décomposer en plusieurs tâches :

— tâche 1 : Au début, R2D2 décide de n’utiliser que 3 couleurs. Il va donc devoir “raisonner”
pour savoir si ces 3 couleurs lui suffisent ou pas pour réaliser son travail.

— tâche 2 : Ensuite, R2D2 cherche à savoir comment il va aller déposer les cubes le plus
rapidement possible. Pour cela, il cherche des chemins les plus courts en termes de distance
parcourue.

— tâche 3 : Finalement, R2D2 cherche à savoir combien il lui faut de couleurs a minima pour
réaliser son travail.

---

## Journal de Bord

### 31/01 - 2H

L'objectif de la séance était d'installer le projet et de le prendre en main.
Il a fallut regarder l'ensemble des nombreuses documentations et corriger
quelques petites erreurs dans le code pour réussir à compiler.

Dans un second temps, il fallait regarder la documentation du solveur 
pour se familiariser avec. Puis, on commence à modéliser le problème.

Soit notre graphe de *i* sommets, on a à disposition *N* couleurs. 
DONC, une variable de notre encodage en logique propositionelle sera représentée par
Ki = "Le sommet i est colorée en K" (K allant de 1 à N). Cela nous fait donc N*i variables au total

J'ai commencé à implémenter cette logique en code pour les sommets.
Il faut que j'améliore la numérotation de mes variables.