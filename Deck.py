#-*- Coding: UTF-8 -*-


class carte:
    nc = 0
    n = {}
    Name = {}
    Class = {}
    Value = {}


    def __init__(self, Nom, Classe, Valeur):
        self.nom = Nom
        self.classe = Classe
        self.valeur = Valeur
        carte.nc += 1
        carte.n[carte.nc] = carte.nc
        carte.Name[carte.nc] = self.nom
        carte.Class[carte.nc] = self.classe
        carte.Value[carte.nc] = self.valeur
    
    def list(What):
        if What == "Name":
            for i in range(1, carte.nc):
                print(carte.Name[i])
        if What == "Class":
            for j in range(1, carte.nc):
                print(carte.Class[j])
        if What == "Value":
            for k in range(1, carte.nc):
                print(carte.Value[k])





