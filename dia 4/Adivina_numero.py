"""
Programa debe preguntar su nombre, que piense un numero entre el 1 y el 100 y tiene 8 intentos para adivinarlo
en cada intenti
dira un numero, si el numero esta fuera de rango dar un aviso de numero no permitido, si es menor que idga que es
incorrecta ya rroje avios de que es menor, de la misma manera si es mayor y si es igual que diga que acerto y cuants
intentos le costo
"""
from random import *
nombre = input("Escribe tu nombre: ")
numero = int(input(f"Hola ^{nombre}  piensa un numero del 1 al 100: "))
aleatorio = randint(1,100)
print(aleatorio)
turnos2 = [8,7,6,5,4,3,2,1,0]
for turno in turnos2:
    print(f"turno numero {turno}")
    if turno == 0:
        print("Game over feo")
        break
    elif numero > 100 or numero < 1:
        print("Fuera de rango feo")
        numero = int(input("Escribe otra opcion de numero: "))
        break
    elif aleatorio > numero:
        print("El numero es mayor")
        numero = int(input("Escribe otra opcion de numero: "))
    elif aleatorio < numero:
        print("Es menor feo")
        numero = int(input("Escribe otra opcion de numero: "))
    elif numero == aleatorio:
        print("acertaste feo felicidades")
        break
    else:
        print("Hiciste tu cagadero")



