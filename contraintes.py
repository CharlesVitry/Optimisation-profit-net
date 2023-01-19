from donnees import import_donnees_from_json


def contraintes(solution, instance):
    original = import_donnees_from_json(instance)

    for lot in solution:
        nb_make = lot[2]
        for article in lot[0]:
            original.Articles[article.id-1].nombre -= nb_make

    vecteur_condition = []

    for article in original.Articles:
        vecteur_condition.append(article.nombre >= 0)

    vecteur_condition.append(max([len(lot[0])
                             for lot in solution]) <= original.e_max)

    vecteur_condition.append(min([len(lot[0])
                             for lot in solution]) >= original.e_min)

    return all(vecteur_condition)
