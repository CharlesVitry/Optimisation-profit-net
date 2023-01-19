from donnees import import_donnees_from_json


def contraintes(solution, instance):
    original = import_donnees_from_json(instance)

    for lot in solution:
        nb_make = lot[2]
        for article in lot[0]:
            original.Articles[article.id-1].nombre -= nb_make

    vecteur_condition = []

    # Respect du nombre d’article disponible
    for article in original.Articles:
        vecteur_condition.append(article.nombre >= 0)

    # Articles distincts dans un lot
    for lot in solution:
        vecteur_condition.append(len(lot[0]) == len(set(lot[0])))

    # on vérifie si le lot avec le plus d'article n'est pas supérieur à la limite
    vecteur_condition.append(max([len(lot[0]) for lot in solution]) <= original.e_max)

    # on vérifie que le lot avec le moins d'article n'est pas inférieur à la limite
    vecteur_condition.append(min([len(lot[0])
                             for lot in solution]) >= original.e_min)

    # vérification des indices commerciales par lot
    for lot in solution:
        vecteur_condition.append(sum([article.indice for article in lot[0]]) >= original.r_min)

    # Nombre de lots maximum
    vecteur_condition.append(len(solution) <= original.L_max)

    # respect des capacités de conditionnement
    C = sum(original.capacites)
    C_solution = sum([lot[2] * len(lot[0]) for lot in solution])
    vecteur_condition.append(C_solution <= C)

    return all(vecteur_condition)
