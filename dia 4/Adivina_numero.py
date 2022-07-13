"""
Programa debe preguntar su nombre, que piense un numero entre el 1 hasta el 100 y tiene 8 intentos para adivinarlo.
En cada intento dira un numero, si el numero esta fuera de rango debera dar un aviso de numero no permitido, si es menor que diga que es
incorrecta y arroje avios de que es menor, de la misma manera si es mayor y si es igual que diga que acerto y cuantos intentos le costo.
"""
from random import randint
#Pedimos nombre al usuario
nombre = input("Escribe tu nombre: ")
#Le pedimos que ingrese un numero dentro del rango 1 a 100
numero = int(input(f"Hola ^{nombre}  piensa un numero del 1 al 100: "))
#Con la funcion randint elegimos un numero dentro del rango especificado y lo guardamos en una variable
aleatorio = randint(1,100)
turnos = [8,7,6,5,4,3,2,1,0]
for turno in turnos:
    print(f"turno numero {turno}")
    if turno == 0:
        print("Game over")
        break
    elif numero > 100 or numero < 1:
        print("Fuera de rango")
        numero = int(input("Escribe otra opcion de numero: "))
        pass
    elif aleatorio > numero:
        print("El numero es mayor")
        numero = int(input("Escribe otra opcion de numero: "))
    elif aleatorio < numero:
        print("Es menor")
        numero = int(input("Escribe otra opcion de numero: "))
    elif numero == aleatorio:
        print("Acertaste felicidades")
        break
    else:
        print("Hiciste tu cagadero")



