from donnees import import_donnees_from_json
from itertools import chain, combinations


def brut_force(D):


    C = sum(D.capacites)

    # Lots possibles
    lots = list(chain(*map(lambda x: combinations(D.Articles, x),
                range(D.e_min, D.e_max + 1))))
    
    # Lots avec un indice commercial suffisant
    lots = list(filter(lambda x: sum(
        [article.indice for article in x]) >= D.r_min, lots))

    lots = [list(lot) for lot in lots]

    lots_utilisés = []



    combinaisons_lots = list(chain(*map(lambda x: combinations(lots, x),
                range(round(D.L_max/2), D.L_max + 1))))

    print("Combinaisons de lots à utilisés : " + str(len(combinaisons_lots)))

    # generation de toutes les combi possibles par combinaisons d'articles
    nbre_max_lot = 3/4 * max([article.nombre for article in D.Articles])

    # IMPOSSIBLE  :  combinatoire trop forte.

    # on retire les solutions non possibles

    # on trie par score


