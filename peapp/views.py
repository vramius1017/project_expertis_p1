# -*- coding: utf-8 -*-
from flask import Flask, render_template , url_for , request
import json

app = Flask(__name__)

app.config.from_object('config')

@app.route("/")
def index():
    return render_template('index.html') 



@app.route("/pine/")
def pine():
    return render_template('pine.html')


@app.route("/polish/")
def polish():
    return render_template('polish.html')


@app.route("/split/")
def split():
    return render_template('split.html')


@app.route("/words/")
def words():
    return render_template('words.html')

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

def TestBr(n):
    t  = 0
    if int(n) % 2 == 0:
        tp = int(n)/2
    else:
        tp = (int(n)+1)/2
        t = int(tp)
        return t 


@app.route('/result_polish/', methods=['POST'])
def result_polish():

    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    op = request.form['op']
    opn = ""
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
    
    respjson = json.dumps({'nombre1': nombre1, 'nombre2': nombre2,
                           'nb': nb, 'op': op, 'opn': opn, 'status': 200})
    
    return render_template('result_polish.html', nombre1=nombre1, nombre2=nombre2, nb=nb, op=op, opn=opn, respjson=respjson)


def CleanChain(x):
    x = str(x)
    x = x.replace("[", " ")
    x = x.replace("]", " ")
    x = x.replace("'", " ")
    x = x.replace(",", " ")
    x = x.replace('"', " ")
    return x

@app.route("/result_word/", methods=['POST'])
def result_word():
    
    phrase=request.form['phrase']
    ph = phrase.split()
    p = ph.reverse()
    jedi = CleanChain(ph)
    rjson = json.dumps({'phrase':phrase,'ph':ph,'p':p,'jedi':jedi})
    return render_template('result_word.html',phrase=phrase,p=p,ph=ph,jedi=jedi)
     

@app.route("/result_pine/",methods=['POST'])
def result_pine():
    
    nombre = request.form['nombre']
    # a = TestBr(nombre)
    # star = "*"
    # space = " "
    # supt = "______"
    # branch = [3,4,5,6,7,8,9,10,11,12,13]
    # foot = list(range(1,a)
    return render_template('result_pine.html', nombre=nombre)#, a=a, branch=branch, star=star, space=space, foot=foot, supt=supt)
    



