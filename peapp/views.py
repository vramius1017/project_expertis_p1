# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template , url_for , request

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


@


'''
if n == 0:
        print("Attention !!!, Seul le support du Sapin sera cree")
    if int(n) % 2 == 0:
         tp = int(n)/2
    else:
         tp = (int(n)-1)/2
    return tp
    for i in range(a):
        print(' '*(a-1-i)+'*'*(1+2*i))
    for i in range(int(tp)):
        print(' '*(a-1)+'#')
    print(' '*(a-2)+3*"_")  '''
# <script src="{{ url_for('static', filename='result_pine.js') }}"></script>

#@app.route("/pine/")
@app.route("/resultpine/",methods=['POST'])
def resultpine():
    nb = request.form['nombre']
    render_template('resultpine.html',nb = nb)
     
