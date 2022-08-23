class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Hola {self.nombre} {self.apellido} tienes el numero de cuenta {self.numero_cuenta} con un balance de {self.balance}"

    def retirar(self,retiro):
        if  retiro <= self.balance :
            self.balance = self.balance - retiro
            print(f"Has retirado {retiro} y tienes unn saldo actual de {self.balance}")
        else:
            print("Fondos insuficentes")

    def depositar(self,deposito):
        self.balance = self.balance + deposito
        print(f"Has depositado {deposito} a tu cuenta, tienes un saldo actual de {self.balance}")




def CrearCliente():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido ")
    numero_cuenta = int(input("Ingresa tu numero de cuenta: "))
    balance = int(input("Ingresa tu ultimo saldo para partir de ahi: "))
    cliente = Cliente(nombre,apellido,numero_cuenta,balance)
    return cliente

def inicio(cliente):
    eleccion = 100000000000000000
    while eleccion != 0:
        print(f"Hola {cliente.nombre} {cliente.apellido} que deseas hacer (0) Salir\n(1) Depositar\n (2) Retirar ")
        eleccion= int(input())
        if eleccion == 0:
            print("Saliste del programa")
            break
        elif eleccion == 1:
            print("Has seleccionado la opcion deposito, porfavor ingresa la cantidad a depositar ")
            deposito = int(input())
            cliente.depositar(deposito)
            print(cliente)
        elif eleccion == 2:
            print("Has seleccionado la opcion de retirar, por favor seleccione la cantidad a retirar: ")
            retiro = int(input())
            cliente.retirar(retiro)
            print(cliente)



cliente = CrearCliente()
inicio(cliente)