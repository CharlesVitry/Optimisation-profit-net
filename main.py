from contraintes import *
from donnees import *
from gloutonne1 import *
import gloutonne2
from objectif import *

if __name__ == "__main__":
    instance = "instances_test/test1.json"
    D = import_donnees_from_json(instance)

    solution_gloutonne = gloutonne1(D)
    print("Contraintes validées : " +
          str(contraintes(solution_gloutonne, instance)))
    print("Score Heuristique : " + str(objectif(D, solution_gloutonne)))
