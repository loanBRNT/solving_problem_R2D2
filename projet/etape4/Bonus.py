

from projet.solvers.SolverLOLO import SolverLOLO

S = SolverLOLO("../../Data/pb-solver/test.txt")
print("RESOLUTION DU PB 1")
print(S.getSolution())

print("=======================================")

S = SolverLOLO("../../Data/pb-solver/test2.txt")
print("RESOLUTION DU PB 2")
print(S.getSolution())

