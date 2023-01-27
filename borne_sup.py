from donnees import import_donnees_from_json
import numpy as np

def borne_lagrangienne(D):
    i = 0
    itermax = 5

    # coefs relaxation
    α = 0.9
    ρ = 2

    len(D.Articles) * len(lots)
    # vecteurs multiplicateur de lagrange
    λ, μ = np.zeros()

    while i < itermax:
        # Résolution du sous-problème Lagrangien 𝐒𝐏𝐋𝟏(λ, 𝜇) → 𝑥𝑖𝑘(̅̅̅̅̅ λ, 𝜇)
        # xik = nombre d’articles de type i impliqué dans les lots de type k
        # couts régus       


        # Résolution du sous-problème Lagrangien 𝐒𝐏𝐋𝟐(λ) → 𝑦𝑖𝑘(̅̅̅̅̅ λ)
        # yik = 1 si l’article i est constitutif d’un lot de type k, 0 sinon
        # couts régus

        # Résolution du sous-problème Lagrangien 𝐒𝐏𝐋𝟑( 𝜇) → 𝑢𝑘 (̅̅̅̅̅ 𝜇)
        # uk = nombre de lots de type k conditionnés
        # couts régus

        # Calcul de la fonction duale

        # Sauvegarde de l’optimum dual courant

        # Calcul des composantes du sous-gradient de L au point (𝛌, 𝝁)

        # Mise à jour des multiplicateurs de Lagrange

        i += 1

        # révision coef de relaxation
        ρ = α * ρ


def lots_possibles(D):
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
    return lots

instance = "instances_test/test1.json"
D = import_donnees_from_json(instance)
borne_lagrangienne(D)
