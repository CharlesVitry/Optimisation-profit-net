from contraintes import *
from donnees import *
from gloutonne1 import *
from gloutonne2 import *
from objectif import *

if __name__ == "__main__":
      instance = "instances_test/test1.json"
      D = import_donnees_from_json(instance)

      D_after_gloutone, solution_gloutonne = gloutonne1(D)
      
      # filtrage des lots non utilisés
      #solution_gloutonne = list(filter(lambda x: x[2] > 0, solution_gloutonne))

      print("Contraintes validées : " +
          str(contraintes(solution_gloutonne, instance)))
      print("Score Heuristique : " + str(objectif(D, solution_gloutonne)))
      
      print("\n\n\n\n")

      D_after_local_search, soluce_local_search = local_search(D_after_gloutone, solution_gloutonne)
      print("Contraintes validées : " +
          str(contraintes(soluce_local_search, instance)))
      print("Score Heuristique : " + str(objectif(D_after_local_search, soluce_local_search)))
