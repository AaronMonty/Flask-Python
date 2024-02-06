jugador1 = input("Ingresa tu nombre jugador1: ")
jugador2 = input("Ingresa tu nombre jugador2: ")

perdidas1 = 0
perdidas2= 0

end=True

while end:
    elecion1=int(input("Turno jugador 1:  1=Piedra | 2=Papel |3=Tijera : "))
    elecion2=int(input("Turno jugador 2:  1=Piedra | 2=Papel |3=Tijera : "))

    if elecion1<=0 or elecion2 <=0:
        print("No se puede numeros negativos intentelo de nuevo ")
    elif elecion1>=4 or elecion2 >=4:
        print("No se pueden numeros mayores a 3")
    else:
        if elecion1==elecion2:
            print("Sacasteis los dos lo mismo")
        elif elecion1>elecion2:
            print("Gano Jugador 1")
            perdidas2+=1
        else:
            print("Gano jugador 2")
            perdidas1+=1

    if perdidas2==3:
        print("Enhorabuena jugador "+jugador1+" ganaste ")
        end=False
    if perdidas1==3:
        print("Enhorabuena jugador "+jugador2+" ganaste ")
        end=False


