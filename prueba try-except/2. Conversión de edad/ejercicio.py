"""
Pide al usuario su edad y conviértela a entero.
Maneja posibles errores si el usuario no ingresa un número válido.
Si la edad es negativa, lanza manualmente una excepción con 'raise ValueError'.
"""

import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') 

def pausar_pantalla():
    input('Presiona enter para continuar...')

def pedir_edad():
    while True:
        try:
            edad = int(input("cual es tu edad:"))
            if edad < 0:
                raise ValueError
            return edad
        except ValueError:
            limpiar_pantalla()
            print("digita un numero correcto")
            pausar_pantalla()
            limpiar_pantalla()
            
      
def inicializa_ejercicio():
    limpiar_pantalla()
    pedir_edad()
    limpiar_pantalla()
    print("fin del ejercicio")
    pausar_pantalla()
    limpiar_pantalla()
    
inicializa_ejercicio()