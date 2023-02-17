"""
module pour l'état de l'etape 2 ds le cas 3
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat


class EtatCas3(Etat):
    """ 
    Classe pour definir un etat pour le cas 3 de la tache 2
    """
    # attributs
    # A COMPLETER
    # //////////////////////////////////////////////
    tg: GrapheDeLieux
    """ le graphe representant le monde """

    liste_parents: list[int]

    courant: int

    arrive: int

    # constructeurs
    # A ECRIRE/MODIFIER/COMPLETER
    # //////////////////////////////////////////////
    def __init__(self, tg: GrapheDeLieux, dep: int = 0, arv: int = 0, l_visite=[]):
        """ constructeur d'un etat a partir du graphe representant le monde
        
        :param tg: graphe representant le monde
        
        :param param1: a definir eventuellement
        
        :param param2: a definir eventuellement
        """
        self.tg = tg
        self.courant = dep
        self.arrive = arv
        self.liste_parents = []
        if l_visite is not None:
            for n in l_visite:
                self.liste_parents.append(n)

        self.liste_parents.append(self.courant)
        # a completer pour tenir compte de la presence ou pas des deux derniers parametres

    # methodes issues de Etat
    # //////////////////////////////////////////////
    def estSolution(self):
        """ methode detectant si l'etat est une solution
        
        :return true si l'etat courant est une solution, false sinon
        """
        # A ECRIRE et MODIFIER le return en consequence
        if len(self.liste_parents) == self.tg.getNbSommets() + 1:
            return True
        return False

    def successeurs(self):
        """ methode permettant de recuperer la liste des etats successeurs de l'etat courant
        
        :return liste des etats successeurs de l'etat courant
        """
        # A ECRIRE et MODIFIER le return en consequence

        if len(self.liste_parents) == self.tg.getNbSommets():
            return [EtatCas3(self.tg, self.arrive, self.arrive, l_visite=self.liste_parents)]

        liste_sucesseur = []

        for s in range(self.tg.getNbSommets()):
            if not s in self.liste_parents:
                liste_sucesseur.append(EtatCas3(self.tg, s, self.arrive, l_visite=self.liste_parents))

        return liste_sucesseur

    def h(self):
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """
        return self.tg.getPoidsMinAir() * (self.tg.getNbSommets() - len(self.liste_parents))

    def k(self, e):
        """ methode permettant de recuperer le cout du passage de l'etat courant à l'etat e
        
        :param e: un etat
        
        :return cout du passage de l'etat courant à l'etat e
        """
        return GrapheDeLieux.dist(self.courant, e.courant, self.tg)

    def displayPath(self):
        """ methode pour afficher le chemin qui a mene a l'etat courant en utilisant la map des peres
        
        :param pere: map donnant pour chaque etat, son pere 
        """
        # A ECRIRE
        print("resultat trouve : ")
        for e in self.liste_parents:
            print(e)

    # methodes pour pouvoir utiliser cet objet dans des listes et des map
    # //////////////////////////////////////////////
    def __hash__(self):
        """ methode permettant de recuperer le code de hachage de l'etat courant
        pour une utilisation dans des tables de hachage
        
        :return code de hachage
        """
        # A ECRIRE et MODIFIER le return en consequence
        return 0

    def __eq__(self, o):
        """ methode de comparaison de l'etat courant avec l'objet o
        
        :param o: l'objet avec lequel on compare
        
        :return true si l'etat courant et o sont egaux, false sinon
        """
        # A ECRIRE et MODIFIER le return en consequence
        if not isinstance(o, Etat):
            return False
        if self.courant != o.courant:
            return False
        if len(self.liste_parents) != len(o.liste_parents):
            return False

        constante = True
        for i in range(len(self.liste_parents)):
            if self.liste_parents[i] != o.liste_parents[i]:
                constante = False

        return constante

    # methode pour affichage futur (heritee d'Object)
    # //////////////////////////////////////////////
    def __str__(self):
        """ methode mettant l'etat courant sous la forme d'une 
        chaine de caracteres en prevision d'un futur affichage
        
        :return representation de l'etat courant sour la forme d'une 
        chaine de caracteres
        """
        # A ECRIRE et MODIFIER le return en consequence
        return ""
