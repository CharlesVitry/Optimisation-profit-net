from donnees import import_donnees_from_json


def contraintes(solution, instance):
    original = import_donnees_from_json(instance)

    for lot in solution:
        nb_make = lot[2]
        for article in lot[0]:
            original.Articles[article.id-1].nombre -= nb_make

    vecteur_condition = []

    # pour chaque article, on vérifie qu'il n'est pas plus utilisé
    for article in original.Articles:
        vecteur_condition.append(article.nombre >= 0)

    # on vérifie si le lot avec le plus d'article n'est pas supérieur à la limite
    vecteur_condition.append(max([len(lot[0])
                             for lot in solution]) <= original.e_max)

    # on vérifie que le lot avec le moins d'article n'est pas inférieur à la limite
    vecteur_condition.append(min([len(lot[0])
                             for lot in solution]) >= original.e_min)

    # vérification des indices commerciales par lot
    for lot in solution:
        vecteur_condition.append(
            sum([article.indice for article in lot[0]]) >= original.r_min)

    return all(vecteur_condition)
