from contraintes import *
from donnees import *
from gloutonne1 import *
from gloutonne2 import *
from objectif import *

def solution_to_csv(solution,name):
      with open(name +".csv", "w") as f:
            f.write("id_lot,qté_production,nbre_article_lot,moyenne_dispo,mini_dispo,max_dispo,moyen_prix,min_prix,max_prix,moyen_indice,min_indice,max_indice \n")
            for i,lot in enumerate(solution) :
            
                  
                  f.write(str(i))#id lot 
                  f.write(",")
                  f.write(str(lot[2])) #qte production
                  f.write(",")
                  f.write(str(len(lot[0]))) #nbre article lot
                  f.write(",")
                  f.write(str(sum([article.nombre for article in lot[0]])/len(lot[0]))) #moyenne dispo
                  f.write(",")
                  f.write(str(min([article.nombre for article in lot[0]]))) #mini dispo
                  f.write(",")
                  f.write(str(max([article.nombre for article in lot[0]]))) #max dispo
                  f.write(",")
                  f.write(str(sum([article.prix for article in lot[0]])/len(lot[0]))) #moyen prix
                  f.write(",")
                  f.write(str(min([article.prix for article in lot[0]])) )#min prix
                  f.write(",")
                  f.write(str(max([article.prix for article in lot[0]])) )#max prix
                  f.write(",")
                  f.write(str(sum([article.indice for article in lot[0]])/len(lot[0]))) #moyen indice
                  f.write(",")
                  f.write(str(min([article.indice for article in lot[0]])) )#min indice
                  f.write(",")
                  f.write(str(max([article.indice for article in lot[0]]))) #max indice
                  f.write("\n")
                  
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

    D_after_local_search, soluce_local_search = local_search(D_after_gloutone, solution_gloutonne, 100000)
    print("Contraintes validées : " +
          str(contraintes(soluce_local_search, instance)))
    print("Score Heuristique : " + str(objectif(D_after_local_search, soluce_local_search)))

    
    solution_to_csv(solution_gloutonne, "glou1")
    solution_to_csv(soluce_local_search, "glou1_search")