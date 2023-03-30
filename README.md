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

#### Avant propos

Ce journal de bord a été écrit dans le dernier quart d'heure de chaque séance. Certaines modélisations évoluent de séance
en séance. L'archive comprend de toute façon les dernières versions de chaque modélisation.

L'ensemble du travail a été réalisé en solo. Les séances du 21/02 et 22/02 ont étaient réalisées à distance.

BONNE LECTURE

### 31/01 - 2H

L'objectif de la séance était d'installer le projet et de le prendre en main.
Il a fallu regarder l'ensemble des nombreuses documentations et corriger
quelques petites erreurs dans le code pour réussir à compiler.

Dans un second temps, il fallait regarder la documentation du solveur 
pour se familiariser avec. Puis, commencer à modéliser le problème.

Soit notre graphe de *i* sommets, on a à disposition *N* couleurs. 
DONC, une variable de notre encodage en logique propositionnelle sera représentée par
Ki = "Le sommet i est colorée en K" (K allant de 1 à N). Cela nous fait donc N*i variables au total

J'ai commencé à implémenter cette logique en code pour les sommets.
Il faut que j'améliore la numérotation de mes variables.

### 07/02 - 2H

L'objectif des 2 heures était de terminer l'étape 1. J'ai donc commencé 
à réfléchir à une méthode de numérotation de variable plus efficace que simplement
une incrémentation. J'ai décidé de représenter chaque Ki par un couple
(sommet, couleur), de m'en servir comme clé dans un dictionnaire en lui associant
comme valeur un entier unique. 

_ex :_
```python
id = (sommet, c)
tableCorrespondance[id]=entier_logique
```

C'est cet entier logique que je mets dans ma base de clause. J'ai commencé par 
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


J'ai ensuite fini de représenter l'ensemble des clauses pour les arêtes 
vu que 2 sommets adjacents ne peuvent avoir la même couleur. Pour ce faire, je 
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
le graphe représentant le monde, le numéro du sommet d'arrivée et le numéro du sommet 
correspondant à l'état.

```python
tg : GrapheDeLieux
""" le graphe representant le monde """ 

arrive : int

courant : int
```

J'ai choisi de définir l'heuristique comme la distance de l'état courant à l'état d'arrivée
```python
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """
        return GrapheDeLieux.dist(self.courant,self.arrive,self.tg)
```

Enfin, j'estime qu'un état est solution si l'état courant = l'état d'arrivée

Cette représentation a bien fonctionné. J'ai eu un petit bug de boucle infinie due à la fonction "equal" que 
j'ai du réécrire, car Astar l'utilisait.

Il me reste une demi-heure, je commence à réfléchir au cas 2.

### 14/02 - 2H

J'ai passé 1h15 sur le cas 2. Les paramètres que j'utilise pour ce cas 2 sont :
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

La nouvelle heuristique d'un état est la distance qui le sépare de l'arrivée multipliée par
le nombre de sommets qu'il reste à visiter.
```python
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """
        return GrapheDeLieux.dist(self.courant,self.arrive,self.tg) * (self.tg.getNbSommets() - len(self.liste_parents))
```

Un état est solution s'il a le même état courant que l'arrivée et que la longueur de sa liste_parents
est plus grand ou égal que le nombre de sommets du graphe. (plus grand ou égal, car on y ajoute 2 fois le point de départ :
au moment où il part et au moment où il y arrive)

La sélection des successeurs change par rapport au cas 1. (J'ai fait le choix d'ajouter à la liste_parent le sommet courant
dans le init). Pour chaque adjacent, on initialise des nouveaux états en vérifiant s'ils n'ont pas déjà été la liste_parents 
de l'état courant. Enfin, si la liste des états visités est pleine et que l'état arrivée est un adjacent de l'état courant, 
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

Je me suis aperçu que mon heuristique n'était pas admissible (grâce à l'enseignant). Car j'utilisais la distance entre 
le départ et l'arrivée et que je la multipliais par le nombre de sommets restants.
L'heuristique est censée être une estimation du coût. Dans mon
cas, l'estimation est fausse même si les résultats étaient justes. 

Ma première idée fut de moyenner les distances entre le sommet et les autres sommets non-visités. Mais ce résultat n'est
pas admissible, car on utilise une moyenne.

J'ai décidé de remplacer mon heuristique dans le cas 2 par :
```python
    def h(self) :  
        return self.tg.getPoidsMinTerre() * (self.tg.getNbSommets() - len(self.liste_parents))
```
La fonction getPoidsMinTerre nous renvoie le coût de l'arrête minimale. Même si notre estimation n'est pas forcément juste
elle reste admissible.

Ensuite, je suis passé au cas 3, le cas est relativement simple, car il découle du 2. La principale modification est à faire
sur le retour des successeurs. On ne souhaite plus avoir uniquement les adjacents, mais tous les sommets en retirant ceux
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
plus opti) et on ne fait aucun thread parallel donc rien d'alarmant.

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

Demain j'implémente ma solution

### 22/02 - 4H

J'ai consacré la première heure et demie à l'implémentation et aux tests. Par rapport à la séance précédente, j'ai
ajouté un attribut supplémentaire afin de pouvoir optionnellement changer de point de départ.

Voici les résultats de ma première batterie de tests :

| nb Essai | SolverTabou 10 villes | SolverHc 10 villes | SolverTabou 26 villes | SolverHc 26 villes |
|----------|-----------------------|--------------------|-----------------------|--------------------|
| 1        | 3241.51               | 3362.79            | 7164.43               | 7929.22            |
| 10       | 2633.38               | 2472.02            | 6307.56               | 7533.57            |
| 100      | 2026.27               | 2394.96            | 5972.96               | 5719.21            |
| 1000     | 2026.27               | 2228.01            | 5278.56               | 5646.05            |


| nb Essai | SolverTabou 150 villes | SolverHc 150 villes | SolverTabou 1000 villes | SolverHc 1000 villes |
|----------|------------------------|---------------------|-------------------------|----------------------|
| 1        | 41951.04               | 40850.86            | 283221.77               | 283777.36            |
| 10       | 36192.04               | 32376.78            | 284223.16               | 278286.95            |
| 100      | 32574.39               | 29731.48            | 267252.16               | 243503.33            |
| 1000     | -                      | -                   | -                       | -                    |


A première vue, Tabou semble plus performant que HC pour les petits graphes et HC que Tabou pour les plus grands. 
J'avais déjà fait une première sélection entre les HC, en choisissant de tirer une solution aléatoire après chaque essai, 
car cela donnait de meilleurs résultats que repartir avec un voisin de la solution courante. Le nombre d'essais semble 
important, surtout dans des grands graphes. Avant de conclure définitivement et parce que j'ai du temps, je vais
essayer de définir autrement mon mouvement entre les solutions et ses voisins.

La nouvelle version considère qu'une solution est voisine d'une autre si un seul sommet à changer de place dans l'ordre
de visite. Exemple [0-1-2-3-0] a pour voisin [0-2-1-3-0], [0-2-3-1-0], [0-1-3-2-0],[0-3-1-2-0] MAIS PAS [0-3-2-1-0]
Avec cette solution, j'ai espoir d'avoir de meilleurs résultats sur les graphes plus complexes, car chaque solution
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
voisin. Même les résultats pour N=1 ne sont pas obtenus via mon ordinateur.

Cependant, on voit qu'avec cette modélisation-là, TABOU offre des performances largement meilleures qu'avant et que HC
sur les graphes plus petits.

Un peu déçu de cette nouvelle solution, je vais rester sur la première solution. Elle représente un bon compromis entre 
temps d'exécution et performance. Un nombre d'essais compris entre 100 (grand graphe) et 1000 (petits graphes)
permet d'obtenir un résultat satisfaisant. Concernant le choix du solver, je pense qu'il faudrait opter pour le solverTabou.
Il a l'air d'être plus "constant" et peut conduire à de meilleurs résultats que le HC.

### 08/03 - 4H

Sur la première heure, je me suis occupé de l'étape 4. Il s'agit d'un problème de coloration. L'encodage du problème
peut se faire via la forme d'un graphe de contrainte. 

**L'ensemble des variables :** Les sommets du graphe.

**Le domaine des variables :** Les couleurs que peuvent prendre un sommet = Toutes les couleurs disponibles.

**L'ensemble des contraintes :** L'ensemble des sous-ensembles de doublons de valeurs autorisés pour un couple de 
sommets adjacents. = Un sous-ensemble par arrête du graphe.

J'ai choisi d'utiliser le solveurCSP pour résoudre ce problème. Les résultats sont tous obtenus et sont bons.

Sur la suite de la séance, je m'attaque à la séance 5. Je garde la partie bonus pour la dernière séance. J'ai passé 1
bonne heure sur l'installation du solver SCIP. Et le reste du temps à faire des tests avec le language ZIMPL afin d'en 
comprendre la syntaxe et le fonctionnement.

En fouillant la doc, je suis tombé sur un exemple concret du problème du voyageur que l'on essaye justement de résoudre.
L'objectif de la séance suivante va être de comprendre et d'adapter cet exemple pour notre cas.

### 15/03 - 4H

Toujours sur l'étape 5. Pour représenter notre problème sous forme de contraintes, il faut justement identifier ces "règles".

La première évidente est que l'on doit passer par une ville **UNE** fois (pas 0 ni 2, juste 1) sauf le point de départ.

La seconde est que la liste des arrêtes doit faire un chemin. Pas de sous-ensemble de sommets.

La fonction que l'on minimise est simplement la distance parcourue, que l'on pourrait représenter par une somme de chaque 
arrêtes parcourues.

Voilà ce que cela donne en language Zimpl :

```
set V := { 0..7 }; 
set E := { <i,j> in V*V with i < j };
set P [ ] := powerset(V);
set K := indexset(P);

var x[E] binary;

param px [V] := read "../../Data/pb-etape5/tsp8.txt" as "1n" comment "#";
param py [V] := read "../../Data/pb-etape5/tsp8.txt" as "2n" comment "#";

defnumb dist(a,b) := sqrt((px[a]-px[b])^2 + (py[a]-py[b])^2);

minimize cost : sum <i,j> in E : dist(i,j) * x[i,j];

subto toute_ville_visitee_une_fois :
forall <v> in V do
    (sum <v,j> in E : x [v,j] ) + ( sum<i,v> in E : x [i,v] ) == 2;

subto pas_de_sous_ensemble :
forall <k> in K with card(P[k]) > 2 and card(P[k]) < card(V) - 2 do
    sum <i,j> in E with <i> in P[k] and <j> in P[k] : x [i,j] <= card(P[k]) - 1;
```

Décomposons ensemble le code :

Déclaration des variables et des ensembles : 
- V : Ensemble des villes. Doit être modifié pour chaque problème selon le nombre de ville
- E : Construit automatique l'ensemble des arrêtes entre les sommets
- P : L'ensemble des sous-ensembles de V
- K : Liste des index de P.
- x : Variable booléenne associée à une arrête. Elle sera mise à 1 si le robot passe par elle
- Px et py : Coordonnée en x (resp. y) des villes.
```
set V := { 0..7 }; 
set E := { <i,j> in V*V with i < j };
set P [ ] := powerset(V);
set K := indexset(P);

var x[E] binary;

param px [V] := read "../../Data/pb-etape5/tsp8.txt" as "1n" comment "#";
param py [V] := read "../../Data/pb-etape5/tsp8.txt" as "2n" comment "#";
```

- Définition de notre distance
```
  defnumb dist(a,b) := sqrt((px[a]-px[b])^2 + (py[a]-py[b])^2);
```

- Définition de notre fonction à minimiser
```
  minimize cost : sum <i,j> in E : dist(i,j) * x[i,j];
```

- 1ʳᵉ contrainte : un sommet n'est lié qu'à 2 autres au maximum.
```
subto toute_ville_visitee_une_fois :
forall <v> in V do
    (sum <v,j> in E : x [v,j] ) + ( sum<i,v> in E : x [i,v] ) == 2;
```

- 2ᵉ contraintes : Un sous ensemble de n sommets ne peut être lié que par n-1 arrêtes. Cela évite les ensembles 
de sommets isolés
```
subto pas_de_sous_ensemble :
forall <k> in K with card(P[k]) > 2 and card(P[k]) < card(V) - 2 do
    sum <i,j> in E with <i> in P[k] and <j> in P[k] : x [i,j] <= card(P[k]) - 1;
```

J'ai fait quelques tests sur 6,7,8 villes qui se sont déroulés sans accros. 

Je teste par curiosité sur les 146 villes, est ce que cette nouvelle forme du problème permet-elle de
résoudre plus rapidement les problèmes que lors de notre étape 2 où on bloquait au-delà de 8 villes :

J'ai peut-être été un peu ambitieux avec 146 villes (mon PC tourne toujours). Je teste pour 26.

26 villes ne marche pas non plus, je vais donc essayer 19 :

Le problème a finalement été résolu en 283.00 secondes. 

La mise en forme sous contraintes présente quand même des avantages non négligents par rapport aux graphes.
Le programme met largement moins de temps et peut résoudre des problèmes plus complexes avec plus de villes.

Pour les 2h qu'il me reste, je vais conclure le journal et essayer de commencer à développer mon propre solver : le SolverLOLO.

# CONCLUSION DES 24 HEURES

Problème de coloration de Graphe : Etape 1 vs Etape 4

Honnêtement, je n'ai pas noté de différences flagrantes en termes de performances entre la logique propositionnelle et 
la modélisation sous forme de graphes de contraintes (CSP). Peut-être que la logique propositionnelle offre une résolution
à peine plus rapide. Mais je n'ai rien pu mesurer précisément.

Problème de parcours de graphe : Etape 2 cas 3 VS Etape 3 VS Etape 5

Ici c'est un peu plus complexe, on a vu avec l'étape 2 cas 3 que les solutions complètes n'arrivaient pas à trouver une
solution si le problème est trop complexe (temps d'exécution trop important). L'étape 3 permettait de mettre en place des solutions
incomplètes (Tabou et HC) afin de trouver une solution potentiellement un peu moins bonne, mais au moins en avoir une.

Là ou on bloquait à 8 villes avec l'étape 2, on arrivait à monter à 1000 villes avec les solutions incomplètes.

L'étape 5 apporte une alternative sur les solutions complètes de l'étape 2. En effet, grâce à la PLNE on arrive à résoudre
des problèmes allant jusqu'à une vingtaine de ville avec l'assurance d'avoir la meilleure solution. Ce qui offre, une meilleure
performance en "temps d'exécution" que pour l'étape 2, mais reste insuffisant pour des problèmes vraiment plus complexes où on préfèrera les
solutions incomplètes de l'étape 3.

# PARTIE BONUS : SOLVER LOLO

Par curiosité, j'ai réalisé mon propre solver CSP. J'avais commencé par utiliser la librairie constraint de python, 
mais je me suis aperçu qu'elle n'était pas vraiment adaptée pour résoudre des problèmes avec des contraintes de couples
interdits. De plus je n'arrivais pas à ajouter différentes contraintes sur le même problème. Il aurait fallut créer un
ensemble de problème avec une contrainte chacun puis récupérer l'intersection de tous ces problèmes. Je pense que ce
n'était pas la solution la plus optimale.

J'ai donc décidé de tout faire moi-même à l'aide d'un dictionnaire des variables et de leur domaine, et d'un second 
dictionnaire pour chaque couple interdit qui donne les valeurs respectives. Je génère alors un ensemble de solution
pour y appliquer ensuite mes contraintes et obtenir uniquement les solutions qui respectent les contraintes.

En entrée, le fichier .txt doit respecter la structure suivante :
```
Structure d'un fichier de donnees type

v var1 var1_val1 var1_val2 ... var1_valm
v var2 var2_val1 var2_val2 ... var2_valp
.
.
v varn varn_val1 varn_val2 ... varn_valj
s var1 var2 //couple de val (x,y) interdit pour var1 et var2
c x y
c x y
c x y
s ..
c x y
c x y
```