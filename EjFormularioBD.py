from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conéctate a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

# Crea un cursor para interactuar con la base de datos
mycursor = mydb.cursor()

# Crea la tabla ALUMNOS si no existe
mycursor.execute("CREATE TABLE IF NOT EXISTS ALUMNOS (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), correo VARCHAR(255))")

# Obtiene los datos de la base de datos y los carga en el diccionario
mycursor.execute("SELECT * FROM ALUMNOS")
result = mycursor.fetchall()
mails = {row[1]: row[2] for row in result}

@app.route("/")
def inici():
    return redirect(url_for('get_mail'))

@app.route('/getmail', methods=['GET', 'POST'])
def get_mail():
    if request.method == 'POST':
        name = request.form['name']

        if name in mails:
            email = mails[name]
            return render_template('getmailresultado.html', result=f'Correo de {name}: {email}')
        else:
            return render_template('getmailresultado.html', result=f'Nombre no encontrado: {name}')

    return render_template('getmailformulario.html')

@app.route('/addmail', methods=['GET', 'POST'])
def add_mail():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Agrega el nuevo alumno a la base de datos
        mycursor.execute("INSERT INTO ALUMNOS (nombre, correo) VALUES (%s, %s)", (name, email))
        mydb.commit()

        # Actualiza el diccionario con los nuevos datos de la base de datos
        mycursor.execute("SELECT * FROM ALUMNOS")
        result = mycursor.fetchall()
        mails.update({row[1]: row[2] for row in result})

        return render_template('addmailresultado.html', result=f'Se ha añadido correctamente: {name} - {email}')

    return render_template('addmail.html')

if __name__ == '__main__':
    app.run(debug=True)
