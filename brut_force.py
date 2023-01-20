from donnees import import_donnees_from_json
from itertools import chain, combinations


def brut_force(D):

    C = sum(D.capacites)

    print("Borne trivial de l'instance : " + str(D.borne_trivial()))
    print("Somme des capacités : " + str(C))
    
    # Lots possibles
    lots = list(chain(*map(lambda x: combinations(D.Articles, x),
                range(D.e_min, D.e_max + 1))))
    print("Nombre de lots possibles : " + str(len(lots)))
    
    # Lots avec un indice commercial suffisant
    lots = list(filter(lambda x: sum(
        [article.indice for article in x]) >= D.r_min, lots))
    print("Nombre de lots avec un indice commercial suffisant : " + str(len(lots)))

    # Trie par profit net décroissant/ nombre d'articles
    lots = sorted(lots, key=lambda x: len(
        x) / (sum([article.prix for article in x]) - D.cd * len(x)))
    
    lots = [list(lot) for lot in lots]

    lots_utilisés = []

    for lot in lots:
        if C == 0 or len(lots_utilisés) == D.L_max:
            break
        # lot_possible if there is nombre > 0 for each article in the lot
        lot_possible = all([article.nombre > 0 for article in lot])
        if lot_possible:
            N = min([article.nombre for article in lot] + [C])
            for article in lot:
                article.nombre -= N
            lots_utilisés.append([lot, N, 0])

    print("Nombre de lots utilisés : " + str(len(lots_utilisés)))

    for lot in lots_utilisés:
        for capacite in D.capacites:
            if capacite > 0:
                N = min(lot[1] * len(lot[0]), capacite)
                D.capacites[D.capacites.index(capacite)] -= N
                lot[2] += N / len(lot[0])
                break

    print("Capacités finales : " + str(D.capacites))
    print("Capacités restantes : " + str(sum(D.capacites)))
    return D, lots_utilisés
