
def borne_lagrangienne(D):
    i = 0
    itermax = 5

    # coefs relaxation
    alpha = 0.9
    ro = 2

    # multiplicateur de lagrange
    l, u = 0

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
        ro = alpha * ro


instance = "instances_test/test1.json"
D = import_donnees_from_json(instance)
borne_lagrangienne(D)
