# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 08:40:44 2019

@author: plateformeCEPS TORRES Sacha
"""

"""
Reverse words 

chaîne de charactere test  =  don't forget the tests 

chaîne de charactere test 2 =  don't forget the unit tests


"""

#v = "don't forget the tests"
s = "don't forget the unit tests"


def CleanChain(x):
    x = str(x)
    x = x.replace("["," ")
    x = x.replace("]"," ")
    x = x.replace("'"," ")
    x = x.replace(","," ")
    x = x.replace('"'," ")
    return x

# input de la chaine de caractéres v
v = input (" entrer une phrase : ")
#print(type(v))

#affichage du type des objets input
#print(type(s))
#print("  ")
#print(type(v))
#print("  ")

#affichages des objets listes 
#print("  ")
l = s.split()
#print(l)
#print(type(l))
#print("  ")
p = v.split()
#print(p)
#print(type(p))

# listes inversés
#print("  ")
p.reverse()
#print(p)
#print("  ")

z = CleanChain(p)
print(z)