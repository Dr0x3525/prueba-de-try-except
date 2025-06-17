"""
Escribe un programa que pida dos números al usuario y muestre el resultado de dividir el primero por el segundo.
Usa try-except para manejar:
- División por cero
- Entrada que no sea numérica
"""
import os

def limpiar_pantalla():
    os.system('clear')
    
def pausar_pantalla():
    input('presiona enter para continuar...')
    
def pedir_numero(dato):
    while True:
        try:
            numero = float(input(f'por favor digita el {dato}: '))
            return numero
        except ValueError:
            limpiar_pantalla()
            print(f'Error: ingresa un numero valido por favor:')
            pausar_pantalla()
            limpiar_pantalla()

def dividir(a,b):
    limpiar_pantalla()
    try:
        respuesta = a / b
        print(f"{a} / {b} = {respuesta}")
    except ZeroDivisionError:
      print('Error: No se puede dividir entre cero.')


def inicializar_ejercicio():
    limpiar_pantalla()
    numero_1 = pedir_numero(dato='primer numero')
    numero_2 = pedir_numero(dato='segundo numero')
    dividir(numero_1,numero_2)
    

inicializar_ejercicio()
pausar_pantalla()
limpiar_pantalla()
print('Fin del ejercicio.')
pausar_pantalla()
limpiar_pantalla()