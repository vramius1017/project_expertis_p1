# -*- coding: utf-8 -*-
from flask import Flask, render_template , url_for , request
import json

app = Flask(__name__)

app.config.from_object('config')

# route de la page d'acceuil projet expertis 

@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html') 

# routes des 4 fonctions 

# fonction creation sapin
@app.route("/pine/")
def pine():
    return render_template('pine.html')

# fonction polish calculator
@app.route("/polish/")
def polish():
    return render_template('polish.html')

# fonction words spliter
@app.route("/split/")
def split():
    return render_template('split.html')

# fonction word
@app.route("/words/")
def words():
    return render_template('words.html')

# routes des pages résultats des fonctions 
# fonction result de words spliter 
# input : phrase type text issue du formulaire champ phrase
# z : liste de  10 charactéres de la liste phrase
# a : int longueur de la liste de characteres phrase
# rejson : JSON  
# output : template : result_split.html , contexte : phrase=phrase,a=a,z=z,rejson=rejson

@app.route("/result_split/",methods=['POST'])
def result_split():
    z = []
    a : int
    a = 0
    phrase = request.form['phrase']
    z = phrase[0:9]
    a = len(phrase)
    rejson = json.dumps({'phrase':phrase,'a':a,'z':z})
    return render_template('result_split.html',phrase=phrase,a=a,z=z,rejson=rejson)

# fonction pour tester la parité d'un entier 
# input : n int
# test sur la valeur du reste de la division euclidienne par 2 de n
# si le reste est de 1 , n est impair sinon n est pair et tp prend une valeur entiere calculé
# output : tp int

def TestBr(n):
    t  = 0
    if int(n) % 2 == 0:
        tp = int(n)/2
    else:
        tp = (int(n)+1)/2
        return t == int(tp)

# fonction polish calculator
# input : 
# nombre1 et nombre2 type number issue du formulaire champ nombre1 et nombre2 rspectivement
# op type text issue du formulaire champ op
# nombre1 , nombre2 : int
# op : str
# er : str texte d'erreur 
# opn : str  nom de l'opération 
# 5 alternatives if : 4 pour les 4 operations correspondant aux 4 valeurs possibles de op 
# et une nulle en cas de non de non saisie d'une opération
# output : repjson : JSON
@app.route('/result_polish/', methods=['POST'])
def result_polish():
    
    er : str
    er = " "
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    op = request.form['op']
    opn = ""
    nb = 0
    respjson = json.dumps({'nombre1': nombre1, 'nombre2': nombre2,
                           'nb': nb, 'op': op, 'opn': opn, 'status': 200})
    if op == "+":
        nb = int(nombre1) + int(nombre2)
        opn = "addition"
    else:
        if op == "*":
            nb = int(nombre1) * int(nombre2)
            opn = "multiplication"
        else:
            if op == "-":
                nb = int(nombre1) - int(nombre2)
                opn = "soustraction"
            else:
                if op == "/" and int(nombre2) != 0:
                    nb = float(nombre1) / float(nombre2)
                    opn = "division par un nombre non nul"

                    if op  == " ":
                        er == " entrer une opération !!!"
                        try:
                            opn ="pas de symbole "
                            nb = 0
                            er = " entrer une opération !!!"
                        except UnboundLocalError :
                            return render_template('result_polish',nb=nb,op=op,opn=opn)
                        
    return render_template('result_polish.html', nombre1=nombre1, nombre2=nombre2, nb=nb, op=op, opn=opn, respjson=respjson, er=er)


# fonction pour nettoyer la chaine de caractére résultante de la fonction words
# input :    x : liste de plusieurs chaines de characteres
# out put    x liste de chaine de caracteres sans les charaactéres suivant[ " ] ' ,
def CleanChain(x):
    x = str(x)
    x = x.replace("[", " ")
    x = x.replace("]", " ")
    x = x.replace("'", " ")
    x = x.replace(",", " ")
    x = x.replace('"', " ")
    return x


# route du résultat de la fonction word
# input : phrase chaine de characteres type text  issue du formulaire champ phrase
# ph : liste de mot resultant de la fonction split()
# p : liste de mots resultant de la fonction reverse()
# jedi : liste  resultant de la CleanChain()


@app.route("/result_word/", methods=['POST'])
def result_word():
    
    phrase=request.form['phrase']
    ph = phrase.split()
    p = ph.reverse()
    jedi = CleanChain(ph)
    rjson = json.dumps({'phrase':phrase,'ph':ph,'p':p,'jedi':jedi})
    return render_template('result_word.html',phrase=phrase,p=p,ph=ph,jedi=jedi)
     
# route du résultat de la fonction creation sapin
# input : nombre type number issue du formulaire champ nombre
# space , star : string caracteres d'affichage déssinant le sapin
# a : int  nombre d'toile à afficher 2a-1 par branches
# branch , foot : liste d'entiers pour l'affichage des branches et du pied du sapin
# output : template result_pine.html , contexte : nombre=nombre, a=a, space=space,supt=supt,star=star,branch=branch, foot=foot, b=b

@app.route("/result_pine/",methods=['POST'])
def result_pine():
    a : int
    nombre = request.form['nombre']
    b : float
    b = 0
    space : str
    foot = []
    a = TestBr(nombre)
    star = "*"
    space = " "
    supt = "______"
    branch = list(range(int(nombre)))
    foot = [0,1,2]
    return render_template('result_pine.html', nombre=nombre, a=a, space=space,supt=supt,star=star,branch=branch, foot=foot, b=b) 
    
    



