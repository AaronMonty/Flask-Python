#Importamos las librerias necesarias
import sys
import csv

#Esta funcion sirve para cargar los datos desde un archivo csv
#Le pasamos un argumento el cual sera ruta_archivo
def cargar_datos_desde_csv(ruta_archivo):
    gmails = {}
    with open(ruta_archivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            nombre, correo = row
            gmails[nombre] = correo
    return gmails

#Obtenemos los correos con esta funcion 
def obtener_correo(nombre, gmails):
    if nombre in gmails:
        return gmails.get(nombre)
    else:
        return "No existe"
#Funcion main el cual tiene un control de errores de si le pasa el nombre y la ruta del archivo csv
def main():
    if len(sys.argv) != 3:
        print("Por favor, proporciona un nombre como argumento y la ruta del archivo CSV.")
    else:
        nombre = sys.argv[1]
        ruta_archivo = sys.argv[2]
        gmails = cargar_datos_desde_csv(ruta_archivo)
        resultado = obtener_correo(nombre, gmails)
        print(resultado)

if __name__ == "__main__":
    main()
