import random
from objectif import *

def gloutonne2(D):
    print("Borne trivial de l'instance : " + str(D.borne_trivial()))
    print("Capacités initial : " + str(D.capacites))
    print("Somme des capacités : " + str(sum(D.capacites)))

    # Trie des articles par Wi = di * vi * 0.1 * ri
    for article in D.Articles:
        article.set_poids(article.nombre * article.prix * 0.1 * article.indice)
    D.Articles = sorted(D.Articles, key=lambda x: x.poids, reverse=True)

    lot_utilise = []
    for i in range(D.L_max):
        # init du lot
        rk, ek = 0, 0
        lot = []
        for article in D.Articles:
            lot.append(article)
            rk += article.indice
            ek += 1
            if rk >= D.r_min and ek >= D.e_min:
                break
            if ek == D.e_max:
                lot.remove(article)
                rk -= article.indice
                ek -= 1
                pass
        if ek > D.e_max:
            break

        # conditionnement des lots
        N = min([article.nombre for article in lot]) * len(lot)
        condix_max = sum(D.capacites)
        if N > condix_max:
            N = condix_max

        lot_utilise.append([lot, N / len(lot), N / len(lot)])
        for article in lot:
            article.nombre -= N / len(lot)
        for capacite in D.capacites:
            if capacite > 0:
                N_par_condi = min(N, capacite)
                D.capacites[D.capacites.index(capacite)] -= N_par_condi
                N -= N_par_condi
                break

        # on remet tt à jour
        for article in D.Articles:
            article.set_poids(
                article.nombre * article.prix * 0.1 * article.indice)
        D.Articles = sorted(D.Articles, key=lambda x: x.poids, reverse=True)

    print("Nombre de lots utilisés : " + str(len(lot_utilise)))
    print("Capacités finales : " + str(D.capacites))
    print("Capacités restantes : " + str(sum(D.capacites)))
    return D, lot_utilise


def local_search(D, solution, nbr_iter):
    print("Capacités initial : " + str(D.capacites))
    print("Somme des capacités : " + str(sum(D.capacites)))

    for _ in range(nbr_iter):
        # select un lot random from solution 
        lot = random.choice(solution)
        articles_dispo = [article for article in D.Articles if article not in lot[0]]

        nombre_article_to_add = lot[2] 

        # si le lot est pas à sa capacité max, on essaye de rajouter un article de la liste des articles dispo
        if len(lot[0]) + 1 <= D.e_max:
            article_to_add = random.choice(articles_dispo)
            # def condition d'arret si possible
            if (article_to_add.nombre > nombre_article_to_add and sum(D.capacites) >= nombre_article_to_add):                 
                # on regarde si la quantité est suffisante   
                lot[0].append(article_to_add)
                D.Articles[D.Articles.index(article_to_add)].nombre -= nombre_article_to_add

                # on met à jours les capacités 
                for capacite in D.capacites:
                    if capacite > 0:
                        N_par_condi = min(nombre_article_to_add, capacite)
                        D.capacites[D.capacites.index(capacite)] -= N_par_condi
                        nombre_article_to_add -= N_par_condi
                        break
        # sinon on essaye de swap un article du lot avec un article de la liste des articles dispo
        else : 
            score_actuel = objectif(D, solution)

            article_to_swap = random.choice(lot[0])
            article_to_add = random.choice(articles_dispo)

            if(article_to_add.nombre > nombre_article_to_add):
                lot[0].remove(article_to_swap)
                lot[0].append(article_to_add)
                if (random.random() < 0.1 and sum([article.indice for article in lot[0]]) >= D.r_min):
                    D.Articles[D.Articles.index(article_to_add)].nombre -= nombre_article_to_add
                    D.Articles[D.Articles.index(article_to_swap)].nombre += nombre_article_to_add
                elif (objectif(D, solution) > score_actuel and sum([article.indice for article in lot[0]]) >= D.r_min):
                    D.Articles[D.Articles.index(article_to_add)].nombre -= nombre_article_to_add
                    D.Articles[D.Articles.index(article_to_swap)].nombre += nombre_article_to_add
                else:
                    lot[0].remove(article_to_add)
                    lot[0].append(article_to_swap)

            
    print("Nombre de lots utilisés : " + str(len(solution)))
    print("Capacités finales : " + str(D.capacites))
    print("Capacités restantes : " + str(sum(D.capacites)))
    return D, solution

