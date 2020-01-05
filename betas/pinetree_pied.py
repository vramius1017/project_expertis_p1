#!/usr/bin/env python
# coding: utf-8




# nombre de branche souhaités aprés fonction test 
nbb = input("entrer le nombre de branches : ")

# calcul du nombres d'etoiles sur la base 
nbe = 2*int(nbb)-1
print("le nombre d'étoiles max sur la branche de base du sapin est : ",nbe)

# test pair- impair de nbb
if int(nbb) % 2 == 0:
    #print("le nb de branches est pair")
    tp = int(nbb)/2
else : 
    #print("le nb de branches est impair")
    tp = (int(nbb)-1)/2

print("la taille du pied du sapin est : ",int(tp))
print("\n")









# fonction affichage horizontal d'une branche
# input : long(int) output : affichage de long u caractére *
i = 0
long = 4
while i < long:        # boucle pour long itération
  i = i +1
  print("*",end='')# affichage horizontal


# In[13]:


# fonction affichage d'un element du pied 
# input : nbe output : affichage * centré selon la branche de base
i = 0
nbe = 13
st = (nbe - 1)/2
print("*")
for i in range(0,int(st)):
    print(" ",end='')
else :
    print("*",end='')


# In[8]:


# affichage du sapin pour 3 branches
#  il faut incrementer les espaces et décrémenter les * en fonction du nombre d'étoiles de la derniére branche
# le pied est centré en positionnant le caractére * à ((ne-1)/2)+1 avec ne nombre d'étoiles impaair de la derniére branche
print(2*" "+"*")
print(" " +3*"*")     
print(5*"*",)
#print(2*" "+"*")


# In[52]:


a = input("nb superieur à 3 :")

for i in range(0,int(a)):
   # for j in range(0,int(a))
    print(int(2*i+1)*"*")
       
          
    


# In[60]:


a = input("nb superieur à 3 :")
j = int((int(a) + 1)/2)
for j in range(1,b):
    print(j*" "+"*")
j=j-1


# In[101]:


nbb=int(input(" ordre du sapin: "))

if int(nbb) % 2 == 0:
    #print("le nb de branches est pair")
    tp = int(nbb)/2
else : 
    #print("le nb de branches est impair")
    tp = (int(nbb)-1)/2
for i in range(nbb):
    # on affiche un nombre impair d'etoile croinssant 2*i+1
    # et un nombre pair d'espace décroissant  soit n-1-i
    print(' '*(nbb-1-i)+'*'*(1+2*i))
for k in range(int(tp)):
    print(' '*(nbb-1)+'#')
print(' '*(nbb-2)+3*"_")         

