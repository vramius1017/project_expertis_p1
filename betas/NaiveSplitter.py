# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 09:46:41 2019

@author: plateformeCEPS  Sacha TORRES
"""


def CleanChain(x):
    x = str(x)
    x = x.replace("[", " ")
    x = x.replace("]", " ")
    x = x.replace("'", " ")
    x = x.replace(",", " ")
    x = x.replace('"', " ")
    return x


    
v = input (" entrer une phrase ***  ATTENTION ***  10 caractéres seulement: ")

#@print(len(v))
#print(v)
z = v[0:10]
a = len(z)
print(z)
print("affichage des {}  premiers caractéres".format(a))  
