"""
module pour l'état de l'etape 2 ds le cas 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat
from projet.solvers.SolverAStar import SolverAStar
from projet.outils.GrapheDeLieux import GrapheDeLieux

class EtatCas1(Etat) :
    """ Classe pour definir un etat pour le cas 1 de la tache 2 (hérite de Etat)
    """ 
    
    # attributs
    # A COMPLETER
    # //////////////////////////////////////////////
    tg : GrapheDeLieux
    """ le graphe representant le monde """ 

    arrive : int

    courant : int

    # constructeurs
    # A ECRIRE/MODIFIER/COMPLETER
    # //////////////////////////////////////////////
    def __init__(self, tg : GrapheDeLieux, numSommet : int = 0, num_arv : int = -1) :
        """ constructeur d'un etat a partir du graphe representant le monde
        
        :param tg: graphe representant le monde
        
        :param numSommet: numero du sommet courant
        
        :param num_arv: numero de l'arrivee
        """
        self.courant = numSommet
        self.tg = tg
        if num_arv == -1:
            num_arv = self.tg.getNbSommets()-1
        self.arrive = num_arv

     
    
    # methodes issues de Etat
    # //////////////////////////////////////////////
    def estSolution(self) :
        """ methode detectant si l'etat est une solution
        
        :return true si l'etat courant est une solution, false sinon
        """
        return self.courant == self.arrive
    
    
    def successeurs(self) :
        """ methode permettant de recuperer la liste des etats successeurs de l'etat courant
        
        :return liste des etats successeurs de l'etat courant
        """
        liste_num = self.tg.getAdjacents(self.courant)
        liste_sommet=[]

        for n in liste_num:
            liste_sommet.append(EtatCas1(self.tg,numSommet=n,num_arv=self.arrive))
        return liste_sommet
    
    
    def h(self) :  
        """ methode permettant de recuperer l'heuristique de l'etat courant 
        
        :return heuristique de l'etat courant
        """
        return GrapheDeLieux.dist(self.courant,self.arrive,self.tg)
    
    
    def k(self, e) :
        """ methode permettant de recuperer le cout du passage de l'etat courant à l'etat e
        
        :param e: un etat
        
        :return cout du passage de l'etat courant à l'etat e
        """
        return self.tg.getCoutArete(self.courant,e.courant)
    
    
    def displayPath(self, pere) :
        """ methode pour afficher le chemin qui a mene a l'etat courant en utilisant la map des peres
        
        :param pere: map donnant pour chaque etat, son pere 
        """ 
        # A ECRIRE
        print("resultat trouve : ")
        e=self
        while pere[e] != None:
            print(e,"<-",pere[e])
            e = pere[e]
    
    
    # methodes pour pouvoir utiliser cet objet dans des listes et des map
    # //////////////////////////////////////////////
    def __hash__(self) :
        """ methode permettant de recuperer le code de hachage de l'etat courant
        pour une utilisation dans des tables de hachage
        
        :return code de hachage
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return 0 
    
    
    def __eq__(self, o) :
        """ methode de comparaison de l'etat courant avec l'objet o
        
        :param o: l'objet avec lequel on compare
        
        :return true si l'etat courant et o sont egaux, false sinon
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        if not isinstance(o,Etat):
            return False
        return self.courant == o.courant
    
    
    
    # methode pour affichage futur (heritee d'Object)
    # //////////////////////////////////////////////
    def __str__(self) : 
        """ methode mettant l'etat courant sous la forme d'une 
        chaine de caracteres en prevision d'un futur affichage
        
        :return representation de l'etat courant sour la forme d'une 
        chaine de caracteres
        """ 
        # A ECRIRE et MODIFIER le return en consequence
        return "sommet n" + str(self.courant)
    



