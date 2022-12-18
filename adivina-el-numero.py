# Adivina el numero! 
from random import randrange

jmf = "fernandez"
jmf1="juanm"
jmf2= "@gmail.com"
print("*" * 20)
print("*" * 10)
print("*")
print("* Adivina el número!")
print("*")
print("* Fernandez Juan Manuel")
print("*", jmf+jmf1+jmf2)
print("*")
print("* Debes elegir un número del 0 al 10, si adivinas el juego te informara.\n* Para salir ingresa un número mayor a 10")
print("*" * 20)

terminar = True
ganaste = 0
veces = 0

def jugamos(intento):
    global ganaste, veces, terminar
    if intento <= 10:
        if intento < 0:
            print("El número debe ser mayor o igual a 0")
        else:
            print("El número ingresado es ", intento)
            # almaceno un número random en $numalea
            numalea=randrange(10)
            # Suma 1 cada vez que se juega
            veces += 1
            # Si numalea es igual a intento, el jugador gano
            if numalea == intento:
                print("//////////////      GANASTE     \\\\\\\\\\\\\\\\\\\\\\\\\n")
                # suma 1 si el jugador gano
                ganaste += 1
            else:
                print("//////////////      No ganaste! >( ")

                print("El número que salio es el ", numalea, "\n")
    else:
        terminar = False
        # Estadísticas del juego
        print(" |||==========================================||| ")
        print(" |||======== EL JUEGO TERMINO  ")
        print(" |||==========================================||| ")
        print(" |||======== JUGASTE", veces," VECES ")
        print(" |||==========================================||| ")
        print(" |||======== GANASTE", ganaste, "VECES ")
        print(" |||==========================================||| ")
        return terminar


while terminar == True:
    # si no se ingresa un número entero se vuelve a preguntar.
    while True:
        try:
            intento = int(input("Ingresar un número: "))
            break
        except ValueError:
            print("Debes ingresar un número entero")
    jugamos(intento)
