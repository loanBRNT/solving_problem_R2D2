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

L'étape 2 est un peu plus lourde à comprendre, j'ai complété quelques fonctions
évidentes. Je réserve la séance prochaine à l'élaboration de l'algo pour
déterminer le plus court chemin entre 2 lieux.

### 10/02 - 2H

J'ai passé la première demi-heure à analyser le code du solverAStar afin de comprendre
précisément ce qui était attendu en retour de chaque fonction. J'ai donc modifié les fonctions
que j'avais faites à la séance précédente. J'ai choisi de représenter un état de l'espace par
le graphe représentant le monde, le numero du sommet d'arrivée et le numero du sommet 
correspondant à l'état.

```python
tg : GrapheDeLieux
""" le graphe representant le monde """ 

arrive : int

courant : int
```

J'ai choisis de définir l'heuristique comme la distance de l'état courant à l'état d'arrivée
```python
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """
        return GrapheDeLieux.dist(self.courant,self.arrive,self.tg)
```

Enfin, j'estime qu'un état est solution si l'état courant = l'état d'arrivée

Cette représentation a bien fonctionné. J'ai eu un petit bug de boucle infinie due au equal que j'ai du réécrire.

Il me reste une demi-heure, je commence à réfléchir au cas 2.

### 14/02 - 2H

J'ai passé 1h15 sur le cas 2. Les paramètres que j'utilise pour ce cas 2 :
```python
    self.tg = tg #le graphe du monde
    self.courant = dep #l'etat courant
    self.arrive = ar #l'etat d'arrivee
    self.liste_parents = [] #la liste des sommets qui ont conduis au courant
    if l_visite is not None:
        for n in l_visite:
           self.liste_parents.append(n)

    self.liste_parents.append(self.courant)
```

Ensuite, il fallait redéfinir mon heuristique et ma solution.

Le nouvel heuristique d'un état est la distance qui le sépare de l'arrivée multipliée par
le nombre de sommets qu'il reste à visiter.
```python
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """
        return GrapheDeLieux.dist(self.courant,self.arrive,self.tg) * (self.tg.getNbSommets() - len(self.liste_parents))
```

Un état est solution s'il a le même état courant que l'arrivée et que la longueur de sa liste_parents
est plus grand ou égal que le nombre de sommets du graphe. (plus grand ou égal car on y ajoute 2 fois le point de départ :
au moment où il part et au moment où il y arrive)

La sélection des sucesseurs changent par rapport au cas 1. (J'ai fait le choix d'ajouter à la liste_parent le sommet courant
dans le init). Pour chaque adjacent, on initialise des nouveaux états en vérifiant s'ils n'ont pas déjà été la liste_parents 
de l'état courant. Enfin, si la liste des etats visités est pleine et que l'état arrivée est un adjacent de l'état courant, 
alors on renvoie simplement le futur état solution.

```python
    def successeurs(self) :
        """ methode permettant de recuperer la liste des etats successeurs de l'etat courant
        
        :return liste des etats successeurs de l'etat courant
        """

        liste_num = self.tg.getAdjacents(self.courant)
        liste_sommet = []

        for n in liste_num:
            if not n in self.liste_parents:
                e = EtatCas2(self.tg, n, self.arrive, l_visite=self.liste_parents)
                print(n)
                liste_sommet.append(e)
            if n == self.arrive and len(self.liste_parents) == self.tg.getNbSommets():
                return [EtatCas2(self.tg, n, self.arrive, l_visite=self.liste_parents)]

        return liste_sommet
```

Je prends un peu d'avance et je lie le cas3.

### 17/02 - 2H

Je me suis aperçu que mon heuristique n'était pas admissible. Car j'utilisais la distance entre le départ et l'arrivée
et que je la multipliais par le nombre de sommets restants. L'heuristique est censé être une estimation du coût. Dans mon
cas, l'estimation est fausse même si les résultats étaient justes. 

Ma première idée fut de moyénnée les distances entre le sommet et les autres sommets non-visités. Mais ce résultat n'est
pas admissible car on utilise une moyenne.

J'ai décidé de remplacer mon heuristique dans le cas 2 par :
```python
    def h(self) :  
        return self.tg.getPoidsMinTerre() * (self.tg.getNbSommets() - len(self.liste_parents))
```
La fonction getPoidsMinTerre nous renvoie le coût de l'arrête minimale. Même si notre estimation n'est pas forcément juste
elle reste admissible.

Ensuite je suis passé au cas 3, le cas est relativement simple car il découle du 2. La principale modification est à faire
sur le retour des sucesseurs. On ne souhaite plus avoir uniquement les adjacents, mais tous les sommets en retirant ceux
déjà visitées uniquement. 
```python
        def successeurs(self) :
        liste_num = self.tg.getAdjacents(self.courant)
        liste_sommet = []

        for n in liste_num:
            if not n in self.liste_parents:
                e = EtatCas2(self.tg, n, self.arrive, l_visite=self.liste_parents)
                liste_sommet.append(e)
            if n == self.arrive and len(self.liste_parents) == self.tg.getNbSommets():
                return [EtatCas2(self.tg, n, self.arrive, l_visite=self.liste_parents)]

        return liste_sommet
```
La fonction heuristique est adaptée aussi en utilisant getPoidsMinAir() au lieu de getPoidsMinTerre().

Cependant, l'algo mouline dès qu'on dépasse 8 villes. Le problème est très complexe, j'utilise python (qui n'est pas le 
plus opti) et on ne fait aucun thread parrallèle donc rien d'alarmant.

Fin du cas 3,et donc de l'étape 2

### 21/02 - 2H

Début de l'étape 3, j'ai passé la séance à choisir mes solvers (solverHC et solverTabou), à reprendre le cours
sur les méthodes incomplètes et à regarder le code afin de mieux saisir le sujet et réfléchir à un bon moyen de *
représenter un état solution pour mon graphe. Je vais donc définir chacun des aspects de ma méthode incomplète :

**Etat solution :** J'ai besoin de moins informations dans chaque état ici que dans un graphe d'état classique. Je n'ai 
besoin qu'uniquement de la liste des villes visitées et de mon graphe de Lieu. 

**Solution optimale :** Cela sera mon état solution avec l'_eval_ la plus faible. 

**Fonction d'eval :** Un état solution sera évaluée par rapport à la distance totale parcourue en suivant son chemin.

**Mouvement :** Je définis mon mouvement comme le changement d'ordre de deux villes consécutives. Exemple [0-1-2-3-0] 
a pour voisin [0-2-1-3-0] et [0-1-3-2-0]. On ne change pas le départ et l'arrivée.

Demain j'implemente ma solution

### 22/02 - 4H

J'ai consacré la première heure et demie à l'implémentation et aux tests. Par rapport à la séance précédente, j'ai
ajouté un attribut supplémentaire afin de pouvoir optionnellement changer de point de départ.

Voici les résultats de ma première batterie de tests :

| nb Essai | SolverTabou 10 villes | SolverHc 10 villes | SolverTabou 26 villes | SolverHc 26 villes |
|----------|-----------------------|--------------------|-----------------------|--------------------|
| 1        | 3241.51               | 3362.79            | 7164.43               | 7929.22            |
| 10       | 2633.38               | 2472.02            | 6307.56               | 7533.57            |
| 100      | 2026.27               | 2394.96            | 5972.96               | 6218.85            |
| 1000     | 2026.27               | 2228.01            | 5278.56               | 5646.05            |


| nb Essai | SolverTabou 150 villes | SolverHc 150 villes | SolverTabou 1000 villes | SolverHc 1000 villes |
|----------|------------------------|---------------------|-------------------------|----------------------|
| 1        | 41951.04               | 42602.86            | 283221.77               | 283777.36            |
| 10       | 36192.04               | 39511.43            | 284223.16               | 278286.95            |
| 100      | 32574.39               | 38945.34            | 243503.33               | 277252.16            |
| 1000     | -                      | -                   | -                       | -                    |
A première vue, Tabou semble plus performant que HC. J'avais déjà fait une première sélection entre les HC, en choisissant
de tirer une solution aléatoire après chaque essai, car cela donnait de meilleurs résultats que repartir avec un voisin
de la solution courante. Le nombre d'essai semble important, surtout dans des grands graphes et avec le sovlerTabou. 
Avec HC, l'augmentation semble "moins" impactante. Avant de conclure définitivement et parce que j'ai du temps, je vais
essayer de définir autrement mon mouvement entre les solutions et ses voisins.

La nouvelle version considère qu'une solution est voisine d'une autre si un seul sommet à changer de place dans l'ordre
de visite. Exemple [0-1-2-3-0] a pour voisin [0-2-1-3-0], [0-2-3-1-0], [0-1-3-2-0],[0-3-1-2-0] MAIS PAS [0-3-2-1-0]
Avec cette solution, j'ai espoirt d'avoir de meilleurs résultats sur les graphes plus complexes, car chaque solution
aura + de voisins, mais le temps d'exécution risque d'être vraiment plus long pour un même nombre d'essai. L'idéal serait
d'obtenir un résultat au moins aussi bon avec un nombre d'essai inférieur


| nb Essai | SolverTabou 10 villes | SolverHc 10 villes | SolverTabou 26 villes | SolverHc 26 villes |
|----------|-----------------------|--------------------|-----------------------|--------------------|
| 1        | 2932.49               | 2932.49            | 7778.03               | 8521.05            |
| 10       | 2026.27               | 2779.81            | 4258.35               | 6906.79            |
| 100      | 2026.27               | 2494.28            | 2900.02               | 6516.61            |
| 1000     | 2026.27               | 2228.01            | 3187.42               | 5893.19            |


| nb Essai | SolverTabou 150 villes | SolverHc 150 villes | SolverTabou 1000 villes | SolverHc 1000 villes |
|----------|------------------------|---------------------|-------------------------|----------------------|
| 1        | 40687.64               | 41465.74            | -                       | -                    |
| 10       | -                      | -                   | -                       | -                    |
| 100      | -                      | -                   | -                       | -                    |
| 1000     | -                      | -                   | -                       | -                    |


Pour les graphes 150/1000 villes, je pense qu'il y a trop de voisins et que l'algo prend trop de temps à tester chaque
voisins. Même les résultats pour N=1 ne sont pas obtenus via mon ordinateur.

Un peu déçu de cette nouvelle solution, je vais rester sur la première solution. Elle représente un bon compromis entre 
temps d'exécution et performance. Un nombre d'essais compris entre 100 (grand graphe) et 1000 (petits graphe)
permet d'obtenir un résultat satisfaisant avec le solverTabou de préférence qui a l'air plus "constant" dans
les résultats au fil des tests.

Il me reste un peu plus d'une heure, je vais m'attaquer à l'étape 4.