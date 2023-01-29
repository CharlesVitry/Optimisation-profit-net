import numpy as np
import cvxpy as cp
from donnees import *


def SP1(D, pi):
    y = cp.Constant(np.zeros((len(D.Articles), D.L_max)))
    
    nested_sum = [cp.sum(- pi[i][j] * D.Articles[i].nombre * y[i][j]).value for j in range(D.L_max) for i in range(len(D.Articles))]
    
    obj = cp.Maximize(cp.sum(nested_sum))

    constraints1 = [np.sum(y[i][j] for i in range(len(D.Articles))) <= D.e_max for j in range(D.L_max)]
    constraints2 = [np.sum(y[i][j] for i in range(len(D.Articles))) >= D.e_min for j in range(D.L_max)]
    constraints3 = [np.sum(D.Articles[i].indice * y[i][j] for i in range(len(D.Articles))) >= D.r_min for j in range(D.L_max)]
    
    prob = cp.Problem(obj, constraints1 + constraints2 + constraints3)
    prob.solve()
    return y.value
    

def SP2(D, pi):
    x = cp.Constant(np.zeros((len(D.Articles), D.L_max)))

    nested_sum = [cp.sum((D.Articles[i].prix + pi[i][j]) * x[i][j]).value for j in range(D.L_max) for i in range(len(D.Articles))]
    obj = cp.Maximize(cp.sum(nested_sum))

    constraints1 = [np.sum(x[i][j] for j in range(D.L_max)) <= D.Articles[i].nombre for i in range(len(D.Articles))]

    prob = cp.Problem(obj, constraints1)
    prob.solve()
    
    return x.value

def sous_grad(D):
    iter = 0
    alpha, rho = 0.9, 2
    pi = np.zeros((len(D.Articles), D.L_max))
    UB = 0

    while iter < 1:
        y = SP1(D, pi)
        x = SP2(D, pi)
        
        ub_courant = 0
        # calcul de la borne sup
        for i in range(len(D.Articles)):
            for j in range(D.L_max):
                ub_courant += - pi[i][j] * D.Articles[i].nombre * y[i][j] + (D.Articles[i].prix + pi[i][j])* x[i][j]
        if ub_courant > UB:
            UB = ub_courant

        # calcul du sous gradient
        grad = np.zeros((len(D.Articles), D.L_max))
        for i in range(len(D.Articles)):
            for j in range(D.L_max):
                grad[i][j] = y[i][j] + x[i][j]

        # mise à jour de pi
        sum_grad = np.sum(grad)
        for i in range(len(D.Articles)):
            for j in range(D.L_max):
                pi[i][j] += rho * ((UB - ub_courant) / sum_grad) *  grad[i][j]

        iter += 1
        rho = alpha * rho
    
    return UB

def main():
    instance = "instances_test/test1.json"
    D = import_donnees_from_json(instance)
    UB = sous_grad(D)
    print(UB)
main()