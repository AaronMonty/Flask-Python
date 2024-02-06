from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/")
def hola():
    return "Hello World!"

@app.route("/my/secret/page")
def secret():
    return "Shh!"

@app.route("/user/<username>")
def user_page(username):
    return f"Welcome, {username}!"

@app.route("/blog/post/<int:post_id>")
def show_post(post_id):
    return f"This is the page for post # {post_id}"

@app.route("/calcular/par/<int:numero>")
def calcular(numero):

    if numero % 2 == 0:
        return f"El numero {numero} es par"

    else:
        return f"El numero {numero} no es par"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/edad/<nombre>/<int:edad>')
def calcularaños(nombre=None,edad=None):

    actual=2024  # Asumiendo que estamos en el año 2023
    cumplir100 = actual + (100 - edad)

    return render_template('calcularedad.html', nombre=nombre,cumplir100=cumplir100)