jugador1 = input("Ingresa tu nombre jugador1: ")
jugador2 = input("Ingresa tu nombre jugador2: ")

ganadas1 = 0
ganadas2 = 0

end=True

while end:
    elecion1=str(input("Turno jugador 1:  Piedra | Papel | Tijera : "))
    elecion2=str(input("Turno jugador 2:  Piedra | Papel | Tijera : "))
    elecion1=elecion1.lower()
    elecion2=elecion2.lower()
    if elecion1!="tijera" and elecion1!="papel" and  elecion1!="piedra" or elecion2!="tijera" and elecion2!="papel" and elecion2!="piedra":
        print("No se pueden otras palabras ")  
    elif elecion1==elecion2:
         print("Sacasteis los dos lo mismo")
    elif elecion1=="tijera" and elecion2=="papel" or elecion1=="papel" and elecion2=="piedra" or elecion1=="piedra" and elecion2=="tijera" :
        print("Gano "+jugador1+" Jugador 1")
        ganadas1+=1
    else:
        print("Gano "+jugador2+" jugador 2")
        ganadas2+=1
    if ganadas1==3:
        print("Enhorabuena jugador "+jugador1+" ganaste la partida ")
        end=False
    elif ganadas2==3:
        print("Enhorabuena jugador "+jugador2+" ganaste ")
        end=False
    else:
        print("Aun no ha ganado nadie | Resultado de momento Jugador1: "+str(jugador1)+" Puntos: "+str(ganadas1)+ " Jugador2: "+str(jugador2)+" Puntos:"+str(ganadas2))


