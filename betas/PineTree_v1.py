# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:03:46 2019

@author: Sacha TORRES
"""

# entrer le nombre de branches 

nbb=int(input(" ordre du sapin: "))

# test de la parité du nombre de branches
# calcul de tp: position du milieu de la branche pour le positionement du tronc

if int(nbb) % 2 == 0:     # test : print("le nb de branches est pair")
    tp = int(nbb)/2
else : 
                          # test : print("le nb de branches est impair")
    tp = (int(nbb)-1)/2
 # on affiche un nombre impair d'etoile croinssant 2*i+1
    # et un nombre pair d'espace décroissant  soit n-1-i

for i in range(nbb):
    print(' '*(nbb-1-i)+'*'*(1+2*i))
for k in range(int(tp)):
    print(' '*(nbb-1)+'#')

# affichage du support du pied du sapin
# même centrage que le pied décalé de un pour afficher trois underscore centrés    
print(' '*(nbb-2)+3*"_")   
