import json
from dataclasses import dataclass, field


@dataclass
class Article:
    id: int
    nombre: int
    prix: float
    indice: int


@dataclass
class donnees:
    e_min: int
    e_max: int
    L_max: int
    cd: float
    r_min: int
    capacites: list
    Articles: list[Article]

    def borne_trivial(self):
        C = sum(self.capacites)
        Score = D = 0

        for article in sorted(
                self.Articles, key=lambda x: x.prix, reverse=True):
            if D >= C:
                break
            n = min(article.nombre, C)
            Score += n * (article.prix - self.cd)
            D += n
        return Score


def import_donnees_from_json(chemin):
    json_data = json.load(open(chemin))
    return donnees(
        e_min=json_data["e_min"],
        e_max=json_data["e_max"],
        L_max=json_data["L_max"],
        cd=json_data["cd"],
        r_min=json_data["r_min"],
        capacites=json_data["capacites"],
        Articles=[
            Article(
                id=article["id"],
                nombre=article["nombre"],
                prix=article["prix"],
                indice=article["indice"],
            )
            for article in json_data["Articles"]
        ],
    )


def print_donnees(donnees):
    print("e_min : ", donnees.e_min)
    print("e_max : ", donnees.e_max)
    print("L_max : ", donnees.L_max)
    print("cd : ", donnees.cd)
    print("r_min : ", donnees.r_min)
    print("capacites : ", donnees.capacites)
    print("Article : ")
    print("id : ", donnees.Articles[0].id)
    print("nombre : ", donnees.Articles[0].nombre)
    print("prix : ", donnees.Articles[0].prix)
    print("indice : ", donnees.Articles[0].indice)

# test1 = import_donnees_from_json("instances_test/test1.json")
# test2 = import_donnees_from_json("instances_test/test2.json")
# test3 = import_donnees_from_json("instances_test/test3.json")

# print(test1.borne_trivial())
# print(test2.borne_trivial())
# print(test3.borne_trivial())
