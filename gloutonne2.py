
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
    return lot_utilise
