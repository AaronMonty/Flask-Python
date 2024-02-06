import sys

def obtener_correo(nombre, gmails):
    if nombre in gmails:
        return gmails.get(nombre)
    else:
        return "No existe"

def main():
    gmails = {
      "Mercedes": "mcast386@xtec.cat",
      "Rayane":   "rayane@rayane.sa",
      "Mohamed": "moha@gmail.com",
      "Jad":	 "jad@gmail.com",
      "Oriol":	 "joam@gmail.com",
      "Elias":	 "hola123@gmail.com",
      "Armau":	 "arnau@gmail.com",
      "Asdrúbal": "asdrubal@gmail.com",
      "Adrian":	 "pedrosanchez@asix2.com",
      "Eric": 	 "eric@gmail.com",
      "Emma":	 "pacosanz@gmail.com",
      "nishwan":	 "nishwan@gmail.com",
      "Javi":	 "javi@gmail.com",
      "Novel":	 "novelferreras49@gmail.com",
      "Bruno":	 "elcigala@gmail.com",
      "David":	 "argentino@gmail.com",
      "Judit":	 "judit@gmail.com",
      "Joao":    "joao@gmail.com",
      "Laura":	 "laura@gmail.com",
      "enrico":	 "123@gmail.com",
      "Joel":	 "joelcobre@gmail.com",
      "Aaron":	 "aaron@gmail.com",
      "Moad":	 "moad@gmail.com",
    }

    if len(sys.argv) != 2: 
        print("Por favor, proporciona un nombre como argumento.")
    else:
        nombre = sys.argv[1]
        resultado = obtener_correo(nombre, gmails)
        print(resultado)

if __name__ == "__main__":
    main()
