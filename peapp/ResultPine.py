# -*- coding: utf-8 -*-
# test de la parité du nombre de branches
# calcul de tp: position du milieu de la branche pour le positionement du tronc
def TestNbb(n:int):
    if n == 0 :
        print("Attention !!!, Seul le support du Sapin sera cree")
    if int(n) % 2 == 0:
         tp = int(n)/2
    else:                  
         tp = (int(n)-1)/2
    return tp     
# on affiche un nombre impair d'etoile croinssant 2*i+1
# et un nombre pair d'espace décroissant  soit n-1-i
# affichage du support du pied du sapin
# même centrage que le pied décalé de un pour afficher trois underscore centrés
def CreatePine(a:int):
    tp = TestNbb(a)
    for i in range(a):
        print(' '*(a-1-i)+'*'*(1+2*i))
    for i in range(int(tp)):
        print(' '*(a-1)+'#')
    print(' '*(a-2)+3*"_")

# test : CreatePine(6) --> OK
#        CreatePine(0) --> KO  
CreatePine(10)
