# -*- coding: utf-8 -*-

x = input("entrer un nombre: ")
y = input("entrer un autre nombre: ")
print(" Choisir une de ces opération : + , - , * , / ")
k = input("entrer l'opération à effectuer : ")

if  k = "+" : 
    z = int(x) + int(y)
        
elif k = "-":
    z = int(x) - int(y)

elif k = "*":
    z = int(x) * int(y)
    
else:
    k == "/"
    try:
        z = int(x) / int(y)
    except ZeroDivisionError:
        print("Division par zéro impossible")
        y = input("entrer un autre nombre: ")
        

print(f'le résultat de l\'opération {z} de {x} par {y} est : {k}')
   
