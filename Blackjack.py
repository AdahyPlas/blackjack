#-*- Coding: UTF-8 -*-
from cartes import *
from random import *
from time import *

def main():
    prenom = input("Entre ton nom : ") #par défaut le nom sera player

    if len(prenom) > 0:
        print("Bonjour {}".format(prenom))
    else:
        prenom = "player"
        print("Ton nom sera Player")
    
    print("Mélange des cartes")
    sleep(5) #ne fait rien pendant 5 sec

    ap = randint(1, 52) #tirage de la première carte pour le player
    bp = randint(1,52) #tirage de la deuxième carte pour le player

    ac = randint(1,52) #tirage de la première carte pour l'ordinateur
    bc = randint(1,52) #tirage de la deuxième carte pour l'ordinateur
    cc = randint(1,52) #tirage de la troisième carte pour l'ordinateur

    
    print("tirage de ta première carte ")
    print(carte.Name[ap] + " de " + carte.Class[ap]) #affiche la première carte du joueur

    if carte.Name[ap] == "As": #vérifie que la carte a n'est pas un As
        ValA1p = input("Tu as eu un as, choisi sa valeur 1 ou 11 -> ")

        if carte.Class[ap] == "Pique":
            Asc.valeur = int(ValA1p)
            carte.Value[ap] = int(ValA1p)
            print("Enregistré !")

        if carte.Class[ap] == "Trèfle":
            Ast.valeur = int(ValA1p)
            carte.Value[ap] = int(ValA1p)
            print("Enregistré !")
        
        if carte.Class[ap] == "Carreau":
            AsC.valeur = int(ValA1p)
            carte.Value[ap] = int(ValA1p)
            print("Enregistré !")
        
        if carte.Class[ap] == "Cœur":
            Asc.valeur = int(ValA1p)
            carte.Value[ap] = int(ValA1p)
            print("Enregistré !")

    
    
    ValP = carte.Value[ap]

    while ap == ac:
        ac = randint(1, 52)
    
    
    
    print("Tirage de la première carte du croupier")
    print(carte.Name[ac] + " de " + carte.Class[ac] + " est la carte du coupier")

    if carte.Name[ac] == "As":
        ValA1C = choice([1, 11])

        if carte.Class[ac] == "Pique":
            Asp.valeur = int(ValA1C)
            carte.Value[ac] = int(ValA1C)

        if carte.Class[ac] == "Trèfle":
            Ast.valeur = int(ValA1C)
            carte.Value[ac] = int(ValA1C)

        if carte.Class[ac] == "Carreau":
            AsC.valeur = int(ValA1C)
            carte.Value[ac] = int(ValA1C)
        
        if carte.Class[ac] == "Cœur":
            Asc.valeur = int(ValA1C)
            carte.Value[ac] = int(ValA1C)
    
    ValC = carte.Value[ac]
        
    while bc == ap:
        bc = randint(1 ,52)
    
    while bc == bp:
        bc = randint(1, 52)
    
    while bc == ac:
        bc = randint(1, 52)
    
    print("Tirage de ta deuxième carte")

    while ap == bp:
        bp = randint(1, 52)
    
    while bp == ac:
        bp == randint(1, 52)
    
    print(carte.Name[bp] + " de " + carte.Class[bp])

    if carte.Name[bp] == "As":
        ValA2p = input("Tu as eu un as, choisi sa valeur 1 ou 11, le total de tes cartes est {} -> ".format(ValP))

        if carte.Class[bp] == "Pique":
            Asp.valeur == int(ValA2p)
            carte.Value[bp] = int(ValA2p)
            print("Enregistré")   

        if carte.Class[bp] == "Trèfle":
            Ast.valeur = int(ValA2p)
            carte.Value[bp] = int(ValA2p)
            print("Enregistré")  

        if carte.Class[bp] == "Carreau":
            AsC.valeur = int(ValA2p)
            carte.Value[bp] = int(ValA2p)
            print("Enregistré")

        if carte.Class[bp] == "Cœur":
            Asc.valeur = int(ValA2p)
            carte.Value[bp] = int(ValA2p)
            print("Enregistré")
    
    ValP = ValP + carte.Value[bp]
    
    if ValP == 21:
        print("Tu as gagné")
    
    else:
    
        print("Tirage de la deuxième carte du croupier")

        if carte.Name[bc] == "As":
            if ValA1C == 1:
                ValA2C = 11
                if carte.Class[bc] == "Pique":
                    Asp.valeur = int(ValA2C)
                    carte.Value[bc] = int(ValA2C)
            
                if carte.Class[bc] == "Cœur":
                    Asc.valeur = int(ValA2C)
                    carte.Value[bc] = int(ValA2C)
            
                if carte.Class[bc] == "Carreau":
                    AsC.valeur = int(ValA2C)
                    carte.Value[bc] = int(ValA2C)
            
                if carte.Class[bc] == "Trèfle":
                    Ast.valeur = int(ValA2C)
                    carte.Value[bc] = int(ValA2C)
    
        ValC = ValC + carte.Value[bc]

        if ValC == 21:
            print("Le Croupier a gagné !")
    
        if ValC > 21:
            print("Le croupier a perdu ! La somme de ses cartes est {}".format(ValC))
            print("Sa deuximème était {}".format(carte.Name[bp] +  " de " + carte.Class[bp]))
        
        else:
            
            askrc = True

            while askrc != False:
                askd = input("Veux-tu retirer encore une carte ? la somme de tes cartes est {}  o/n -> ".format(ValP))
                if askd == "o":
                    cp = randint(1, 52)

                    while cp == ap:
                        cp = randint(1, 52)
            
                    while cp == bp:
                        cp = randint(1, 52)
            
                    while cp == ac:
                        cp = randint(1, 52)
            
                    while cp == bc:
                        cp = randint(1, 52)
                    
                    while cp == cc:
                        cp = randint(1, 52)
            
                    print(carte.Name[cp] + " de " + carte.Class[cp])


                    if carte.Name[cp] == "As":
                        ValA3p = input("Tu as eu un as, choisi sa valeur 1 ou 11, le total de tes cartes est {} -> ".format(ValP))
                        if carte.Class[cp] == "Pique":
                            Asp.valeur = int(ValA3p)
                            carte.Value[cp] = int(ValA3p)
                            print("Enregistré")

                        if carte.Class[cp] == "Trèfle":
                            Ast.valeur = int(ValA3p)
                            carte.Value[cp] = int(ValA3p)
                            print("Enregistré")

                        if carte.Class[cp] == "Cœur":
                            Asc.valeur = int(ValA3p)
                            carte.Value[cp] = int(ValA3p)
                            print("Enregistré")

                        if carte.Class[cp] == "Carreau":
                            AsC.valeur = int(ValA3p)
                            carte.Value[cp] = int(ValA3p)
                            print("Enregistré")

                    ValP = ValP + carte.Value[cp]
                    

                    if ValP == 21:
                        print("Tu as gagné ! La somme de tes cartes fait 21")
                        askrc = False
            
                    if ValP > 21:
                        print("Tu as perdu, La somme de tes cartes fais {}".format(ValP))
                        print("La deuxième carte du croupier était '{}'".format(carte.Name[bc] + " de " + carte.Class[bc]))
                        askrc = False
                    
                    
                elif askd == "n":
                    askrc = False
                    print("La somme de tes cartes est {}".format(ValP))

                    print("Tirage de la dernière carte du croupier")
                    sleep(5.5)


                    while cc == ap:
                        cc = randint(1, 52)
                        
                    while cc == bp:
                        cc = randint(1, 52)
                        
                    while cc == ac:
                        cc = randint(1, 52)
                        
                    while cc == bc:
                        cc = randint(1, 52)

                    if carte.Name[cc] == "As":
                        ValA3C = choice([1, 11])
                        if carte.Class[cc] == "Pique":
                            Asp.valeur = int(ValA3C)
                            carte.Value[cc] = int(ValA3C)
                        
                        if carte.Class[cc] == "Trèfle":
                            Ast.valeur = int(ValA3C)
                            carte.Value[cc] = int(ValA3C)
                        
                        if carte.Class[cc] == "Cœur":
                            Asc.valeur = int(ValA3C)
                            carte.Value[cc] = int(ValA3C)
                        
                        if carte.Class[cc] == "Carreau":
                            AsC.valeur = int(ValA3C)
                            carte.Value[cc] = int(ValA3C)

                        ValC= ValC + carte.Value[cc]

                    print("L'ordinateur va retourner le cartes dans")
                    print("3 sec")
                    sleep(1)
                    print("2 sec")
                    sleep(1)
                    print("1 sec")
                    sleep(1)

                    print("La deuxième carte du croupier est le/la {}".format(carte.Name[bc] + " de " + carte.Class[bc]))
                    print("la troisième carte du croupier est le/la {}".format(carte.Name[cc] + " de " + carte.Class[cc]))
                    
                    def affichepoint():
                        print("La somme de tes cartes est {}".format(ValP))
                        print("La somme des cartes du courpier est {}".format(ValC))

                    if ValP > ValC:
                        print("Tu as gagné !")
                        affichepoint()

                    if ValP == ValC:
                        print("Égalité")
                        affichepoint()

                    if ValP < ValC:
                        print("tu as perdu")
                        affichepoint()

                
                else:
                    print("Tirage de la dernière carte du croupier")
                    sleep(5.5)



                    while cc == ap:
                        cc = randint(1, 52)
                        
                    while cc == bp:
                        cc = randint(1, 52)
                        
                    while cc == ac:
                        cc = randint(1, 52)
                        
                    while cc == bc:
                        cc = randint(1, 52)
                    
                    if carte.Name[cc] == "As":
                        ValA3C = choice([1, 11])
                        if carte.Class[cc] == "Pique":
                            Asp.valeur = ValA3C
                            carte.Value[cc] = ValA3C
                        
                        if carte.Class[cc] == "Trèfle":
                            Ast.valeur = ValA3C
                            carte.Value[cc] = ValA3C
                        
                        if carte.Class[cc] == "Cœur":
                            Asc.valeur = ValA3C
                            carte.Value[cc] = ValA3C
                        
                        if carte.Class[cc] == "Carreau":
                            AsC.valeur = ValA3C
                            carte.Value[cc] = ValA3C

                        ValC = ValC + carte.Value[cc]

                    print("L'ordinateur va retourner les cartes dans")
                    print("3 sec")
                    sleep(1)
                    print("2 sec")
                    sleep(1)
                    print("1 sec")
                    sleep(1)

                    print("La deuxième carte du croupier est le/la {}".format(carte.Name[bc] + " de " + carte.Class[bc]))
                    print("la troisième carte du croupier est le/la {}".format(carte.Name[cc] + " de " + carte.Class[cc]))
                    
                    def affichepoint():
                        print("La somme de tes cartes est {}".format(ValP))
                        print("La somme des cartes du courpier est {}".format(ValC))

                    if ValP > ValC:
                        print("Tu as gagné !")
                        affichepoint()

                    if ValP == ValC:
                        print("Égalité")
                        affichepoint()

                    if ValP < ValC:
                        print("tu as perdu")
                        affichepoint()

 
a = True
p = 1
while a != False:
    print("partie {}".format(p))
    main()
    ask = input("Veux tu commencer  une nouvelle partie o/n -> ")

    if ask == "n":
        a = False
    
    p += 1
    









    
