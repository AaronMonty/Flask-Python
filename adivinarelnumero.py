import random

numero1=int(input("Dime el primer numero desde cual quieres que piense"))
numero2=int(input("Dime el segundo numero desde cual quieres que piense"))

numero_secreto = random.randint(numero1, numero2)
    
intentos = 0
end = True
print("Bienvenido al juego de adivinar el número")
print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    
while end:
    intento = int(input("Tu intento: "))
        
    intentos += 1
        
    if intento == numero_secreto:
         print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
         end = False
    elif intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo. | Llevas "+str(intentos)+" intentos")
            
    else:
        print("El número es menor. Intenta de nuevo. | Llevas "+str(intentos)+" intentos")
