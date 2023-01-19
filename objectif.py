# calcul du score final : somme des profits nets des lots utilisés

def objectif(D, solution):
    score = sum([lot[2] * (sum([article.prix for article in lot[0]]) -
                           D.cd * len(lot[0])) for lot in solution])
    return score
