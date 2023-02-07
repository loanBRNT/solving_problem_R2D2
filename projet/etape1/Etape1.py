"""
Module pour l'etape 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.solvers.SolverSAT import SolverSAT

class Etape1 :
    """
    Classe pour realiser l'etape 1 du projet (tache 1)
    """
    # attributs
    # //////////////////////////////////////////////
    g : GrapheDeLieux 
    """
    le graphe representant le monde 
    """
    base : list
    """
    la base de clauses representant le probleme. 
    C'est une liste de listes d'entiers, un entier par variable, 
    (positif si literal positif, negatif sinon). 
    Attention le 0 n'est pas autorise pour represente une variable
    maj par majBase
    """
    nbVariables : int 
    """
    le nb de variables utilisees pour representer le probleme 
    maj par majBase
    """
    
    # constructeur
    # //////////////////////////////////////////////
    def __init__ (self, fn : str, form : bool) :
        """
        constructeur
        
        :param fn: le nom du fichier dans lequel sont donnes les sommets et les aretes
        
        :param form: permet de distinguer entre les differents types de fichier 
         (pour ceux contenant des poids et des coordonnees, form est True ;
          pour les autres, form est False)   
        """
        self.g = GrapheDeLieux.loadGraph(fn,form)
        self.base = [] 
        self.nbVariables = 0        
    
    # methodes
    # //////////////////////////////////////////////
    def majBase(self, x : int) :
        """
        methode de maj de la base de clauses et du nb de variables en fonction du pb traite 
        
        :param x: parametre servant pour definir la base qui representera le probleme 
        """
        #INIT
        self.base=[]
        self.nbVariables = self.g.getNbSommets() * x
        tableCorrespondance = {}
        entier_logique=0

        #BOUCLES
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

        # Remplissage des clauses sur les aretes
        for sommet in range(self.g.getNbSommets()):
            for s in self.g.getAdjacents(sommet):
                for c in range(x):
                    entier_1 = tableCorrespondance[sommet,c]
                    entier_2 = tableCorrespondance[s,c]
                    if [-entier_1, -entier_2] not in self.base and [-entier_2, -entier_1] not in self.base:
                        self.base.append([-entier_1,-entier_2])
    
    def execSolver(self) : 
        """
        methode d'appel du solver sur la base de clauses representant le pb traite
        
        :return True si la base de clauses representant le probleme est satisfiable, 
                False sinon
        """
        return SolverSAT.solve(self.base)     
    
    def affBase(self) :
        """
        affichage de la base de clauses representant le probleme 
        """
        print('Base de clause utilise ',self.nbVariables,' variables et contient les clauses suivantes : ') 
        for cl in self.base :
            print(cl) 
    

class __testEtape1__ : 
    """  
    methode principale de test
    """
    # TESTS
    # //////////////////////////////////////////////
    if __name__ == '__main__':
        
        # TEST 1 : town10.txt avec 3 couleurs
        print("Test sur fichier town10.txt avec 3 couleurs")
        e = Etape1("../../Data/town10.txt",True)
        e.majBase(3)
        #e.affBase()
        print("Resultat obtenu (on attend True) :",e.execSolver())
        

        # TEST 2 : town10.txt avec 2 couleurs
        print("Test sur fichier town10.txt avec 2 couleurs")
        e.majBase(2)
        #e.affBase()
        print("Resultat obtenu (on attend False) :",e.execSolver())
        
        
        # TEST 3 : town10.txt avec 4 couleurs
        print("Test sur fichier town10.txt avec 4 couleurs")
        e.majBase(4)
        #e.affBase()
        print("Resultat obtenu (on attend True) :",e.execSolver())
        
        
        # TEST 4 : flat20_3_0.col avec 4 couleurs
        print("Test sur fichier flat20_3_0.col avec 4 couleurs")
        e = Etape1("../../Data/pb-etape1/flat20_3_0.col",False)
        e.majBase(4)
        # e.affBase()
        print("Resultat obtenu (on attend True) :",e.execSolver())
        
        # TEST 5 : flat20_3_0.col avec 3 couleurs
        print("Test sur fichier flat20_3_0.col avec 3 couleurs")
        e.majBase(3)
        # e.affBase() ;
        print("Resultat obtenu (on attend True) :",e.execSolver())
        
        # TEST 6 : flat20_3_0.col avec 2 couleurs
        print("Test sur fichier flat20_3_0.col avec 2 couleurs")
        e.majBase(2)
        # e.affBase() ;
        print("Resultat obtenu (on attend False) :",e.execSolver())
        
            
        
        # TEST 7 : jean.col avec 10 couleurs
        print("Test sur fichier jean.col avec 10 couleurs")
        e = Etape1("../../Data/pb-etape1/jean.col",False)
        e.majBase(10)
        # e.affBase() ;
        print("Resultat obtenu (on attend True) :",e.execSolver())
        
        # TEST 9 : jean.col avec 9 couleurs
        print("Test sur fichier jean.col avec 9 couleurs")
        e.majBase(9)
        # e.affBase() ;
        print("Resultat obtenu (on attend False) :",e.execSolver())
        
        # TEST 8 : jean.col avec 3 couleurs
        print("Test sur fichier jean.col avec 3 couleurs")
        e.majBase(3)
        # e.affBase() ;
        print("Resultat obtenu (on attend False) :",e.execSolver())


