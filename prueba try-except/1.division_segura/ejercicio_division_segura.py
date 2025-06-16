"""
Escribe un programa que pida dos números al usuario y muestre el resultado de dividir el primero por el segundo.
Usa try-except para manejar:
- División por cero
- Entrada que no sea numérica
"""
import os

def limpiar_pantalla():
    os.system("cls")
    
def pausar_pantalla():
    os.system('pause')
    
def pedir_numero():
    while True:
        try:
            numero = int(input(" digita un  numero: "))
            return numero
        except ValueError:
            limpiar_pantalla()
            print(f'digita un numero entero valido por favor:')
            pausar_pantalla()
            limpiar_pantalla()

def division(a,b):
    limpiar_pantalla()
    try:
        respuesta = a / b
        print(f"{a} / {b} = {respuesta}")
        return respuesta
    except ZeroDivisionError:
      print('no se puede dividir por 0')


def inicializar_ejercicio():
    limpiar_pantalla()
    numero_1 = pedir_numero()
    numero_2 = pedir_numero()
    division(numero_1,numero_2)
    
    
inicializar_ejercicio()

