from flask import Flask
from flask import render_template
app = Flask(__name__)

#Ejercicio par y impar
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

#Practica html y css
@app.route('/edad/<nombre>/<int:edad>')
def calcularaños(nombre=None,edad=None):

    actual=2024  
    cumplir100 = actual + (100 - edad)

    return render_template('calcularedad.html', nombre=nombre,cumplir100=cumplir100)