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

v = "don't forget the tests"
s = "don't forget the unit tests"

print(type(s))
print(type(v))
print("  ")

l = s.split()
print(l)

p = v.split()
print(p)
p.reverse()
print(p)