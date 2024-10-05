# nome do arquivo precisar ser app
from flask import Flask

# quando executamos esse arquivo diretamente __name__ = "__main__"
app = Flask(__name__) # utilizamos a classe Flask para criar o objeto app __name__ = nome do nosso aplicativo

# Rota: comunicar com outros clientes receber e devolver info

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/about")
def about():
    return "Página sobre"

# modo debug somente se o arquivo for executado de forma manual
if __name__ == "__main__":
    app.run(debug=True)
