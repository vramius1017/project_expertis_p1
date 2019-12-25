from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    
    return "hello world !!!  page d'acceuil  3 liens pour les trois applications exercies faire un template poules pages header content footer avec bootstrap 4"

if __name__ == "__main__":
    app.run()    