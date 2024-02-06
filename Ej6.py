texto = input("Ingresa un texto: ")

texto = texto.lower() 
texto_sin_espacios = texto.replace(" ", "")  

if texto_sin_espacios == texto_sin_espacios[::-1]:
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")