import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

def agregar_usuario(mydb):
    print("Dime los datos del empleado para añadirlo a la base de datos")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")

    # Verificar si el empleado ya existe
    mycursor2 = mydb.cursor()
    mycursor2.execute("SELECT * FROM EMPLEADOS WHERE NOMBRE=%s", (nombre,))
    myresult2 = mycursor2.fetchall()

    if not myresult2:
        # Si el empleado no existe, insertar en la base de datos
        sql = "INSERT INTO EMPLEADOS (NOMBRE, APELLIDO, CORREO) VALUES (%s, %s, %s)"
        val = (nombre, apellido, correo)
        mycursor2.execute(sql, val)
        mydb.commit()
        print("Empleado agregado a la base de datos.")
    else:
        print("Error, ese empleado ya existe en la base de datos.")

def buscar_usuario(mydb):
    # Consultar y mostrar los datos del empleado por nombre
    print("Dime el nombre del empleado y te mostraré todo de él")
    nombre = input()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM EMPLEADOS WHERE NOMBRE=%s", (nombre,))
    myresult = mycursor.fetchall()

    if myresult:
        print("Datos del empleado:")
        for x in myresult:
            print(x)
    else:
        print("No se encontró ningún empleado con ese nombre.")

# Menú principal
while True:
    print("\n1. Agregar Usuario")
    print("2. Buscar Usuario")
    print("3. Salir")

    opcion = input("Selecciona una opción (1, 2, 3): ")

    if opcion == "1":
        agregar_usuario(mydb)
    elif opcion == "2":
        buscar_usuario(mydb)
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
