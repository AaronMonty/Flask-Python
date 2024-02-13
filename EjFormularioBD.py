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

@app.route('/getmail',methods = ['POST', 'GET'])
def get_mail():
    if request.method == 'POST':
        name = request.form['nom']
        name = name.capitalize()

        # Buscar el correo asociado al nombre en la base de datos
        mycursor.execute("SELECT correo FROM ALUMNOS WHERE nombre = %s", (name,))
        result = mycursor.fetchone()

        if result:
            email = result[0]
            return render_template('resultgetmail.html', name=name, email=email)
        else:  
            return render_template('resultgetmail.html', name=name, email="Correo no encontrado")
    else: 
        return render_template('formgetmail.html')

@app.route('/addmail', methods=['GET', 'POST'])
def add_mail():
    if request.method == 'POST':
        modif = False
        name = request.form['nom']
        name = name.capitalize()
        email = request.form['correu']

        if 'modif' in request.form:
            modif = True

        # Verificar si el nombre ya existe en la base de datos
        mycursor.execute("SELECT * FROM ALUMNOS WHERE nombre = %s", (name,))
        existing_record = mycursor.fetchone()

        if existing_record:
           # Mostrar un mensaje si el correo ya existe
            result_msg = f"JAEXISTEIX"
        elif existing_record==False:
            # Insertar un nuevo registro si no existe
            mycursor.execute("INSERT INTO ALUMNOS (nombre, correo) VALUES (%s, %s)", (name, email))
            result_msg=""
        else:
            result_msg = "MODIFICAT"

        mydb.commit()  # Guardar los cambios en la base de datos

        return render_template('resultaddmail.html', name=name, email=email, result_msg=result_msg)
    else:
        return render_template('formaddmail.html')

if __name__ == '__main__':
    app.run(debug=True)
