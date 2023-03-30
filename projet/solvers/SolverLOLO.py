from constraint import *

from projet.outils.GrapheDeLieux import GrapheDeLieux

'''
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
'''


class SolverLOLO:

    def __init__(self, fic):
        self.dico = {}
        self.contraintes = {}
        self.domaineComplet = 1
        f = open(fic)
        if f is not None:
            ligne = f.readline()
            tmp = ligne.split("\n")[0].split(" ")

            while tmp[0] == "v":
                self.dico[tmp[1]] = []
                temp_domaine = 0
                for i in range(2, len(tmp)):
                    self.dico[tmp[1]].append(int(tmp[i]))
                    temp_domaine += 1

                self.domaineComplet = self.domaineComplet * temp_domaine

                ligne = f.readline()
                tmp = ligne.split("\n")[0].split(" ")

            while tmp[0] == "s":
                if tmp[1] in self.dico and tmp[2] in self.dico:
                    indice = (tmp[1], tmp[2])
                    self.contraintes[indice] = []
                    ligne = f.readline()
                    tmp = ligne.split("\n")[0].split(" ")
                    while tmp[0] == "c":
                        self.contraintes[indice].append((tmp[1], tmp[2]))
                        ligne = f.readline()
                        tmp = ligne.split("\n")[0].split(" ")
                else:
                    ligne = f.readline()
                    tmp = ligne.split("\n")[0].split(" ")

            f.close()

            self.nbContraintes = len(self.contraintes)
            self.ensembleCombinaison = [{} for e in range(self.domaineComplet)]
            val_domaine = self.domaineComplet
            grande_boucle = 1
            for variable in self.dico:
                indice = 0
                val_domaine = val_domaine // len(self.dico[variable])
                for repet in range(grande_boucle):
                    for val_var in self.dico[variable]:
                        for r in range(val_domaine):
                            self.ensembleCombinaison[indice][variable] = val_var
                            indice += 1
                grande_boucle = grande_boucle * len(self.dico[variable])

        else:
            print("Erreur : Le fichier " + fic + "est introuvable")

    def getEnsembleCombinaison(self):
        return self.ensembleCombinaison

    def getSolution(self):
        out = self.ensembleCombinaison
        for (var1, var2) in self.contraintes:
            temp = out.copy()
            for combinaison in out:
                for couple in self.contraintes[(var1, var2)]:
                    if (int(combinaison[var1]) == int(couple[0])) and (int(combinaison[var2]) == int(couple[1])):
                        temp.remove(combinaison)
            out = temp
        return out
