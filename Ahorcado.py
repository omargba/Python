#Importamos la funcion choice para elegir algo al azar dentro de una lista
from random import choice

#Definimos palabras al azar dentro de una lista
palabras = ["azul", "rojo", "amarillo", "semaforo", "avila", "omar", "amor","python","nada"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    #Esta funcion escoge una palabra al azar
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

def pedir_letra():
    #Esta funcion valida la letra ingresada
    letra_elegida = ' '
    es_valida = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"

    while not es_valida:
        letra_elegida = input("elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida

def mostar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("-")
    print(' '.join(lista_oculta))

def chequear(letra_elegida,palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias

def perder():
    print("Perdiste feo")
    print("La palabra era esta feo " + palabra)

    return True

def ganar(palabra_descubierta):
    mostar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones encontraste la palabra")

    return True

palabra,letras_unicas = elegir_palabra(palabras)
while not juego_terminado:
    print("\n" + "*" * 20 + "\n")
    mostar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas: " + " ".join(letras_incorrectas))
    print(f"vidas: {intentos}")
    print("\n" + "*" * 20 + "\n")
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear(letra,palabra,intentos,aciertos)

    juego_terminado = terminado

print("Muñaño")






