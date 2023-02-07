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
DONC, une variable de notre encodage en logique propositionnelle sera représentée par
Ki = "Le sommet i est colorée en K" (K allant de 1 à N). Cela nous fait donc N*i variables au total

J'ai commencé à implémenter cette logique en code pour les sommets.
Il faut que j'améliore la numérotation de mes variables.

### 07/02 - 2H

L'objectif des 2 heures était de terminer l'étape 1. J'ai donc commencé 
à réfléchir à une méthode de numérotation de variable plus efficace que simplement
une incrémentation. J'ai donc décidé de représenter chaque Ki par un couple
(sommet, couleur), de m'en servir comme clé dans un dictionnaire en lui associant
comme valeur un entier unique. 

_ex :_
```python
id = (sommet, c)
tableCorrespondance[id]=entier_logique
```

C'est cet entier logique je met dans ma base de clause. J'ai commencé par 
représenter l'ensemble des clauses pour les sommets, vu qu'un sommet ne peut
avoir qu'une seule couleur. C'est ici que j'associe chaque id à un entier

```python
for sommet in range(self.g.getNbSommets()):
    # Init de la liste pour les clauses de l'environnement
    env = []

    # Remplissage des clauses sur les sommets
    for c in range(x):
        entier_logique += 1
        id = (sommet, c)
        # On ajoute a la table notre nouveau couple
        tableCorrespondance[id]=entier_logique
        for entier_deja_present in env:
            if [-entier_logique, -entier_deja_present] not in self.base and [-entier_deja_present,-entier_logique] not in self.base:
                self.base.append([-entier_logique, -entier_deja_present])
        env.append(entier_logique)
    self.base.append(env)
```


J'ai ensuite finis de représenter l'ensemble des clauses pour les arêtes 
vu que 2 sommets adjacents ne peuvent avoir la même couleur. Pour se faire, je 
récupère chaque entier associé aux couples précédemment créer.

```python
for sommet in range(self.g.getNbSommets()):
    for s in self.g.getAdjacents(sommet):
        for c in range(x):
            entier_1 = tableCorrespondance[sommet,c]
            entier_2 = tableCorrespondance[s,c]
            if [-entier_1, -entier_2] not in self.base and [-entier_2, -entier_1] not in self.base:
                self.base.append([-entier_1,-entier_2])
```

Notons que l'on pourrait optimiser en fusionnant les 2 boucles, mais cela
imposerait des vérifications sur la tableCorrespondance et un changement dans
la façon de gérer l'attribution de l'entier_logique. Ma solution a passé les
tests parfaitement. Je vais prendre un peu d'avance en commençant l'étape 2.