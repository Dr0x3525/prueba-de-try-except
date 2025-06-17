"""
Crea una lista con 5 elementos. Pide al usuario un índice e imprime el elemento en esa posición.
Maneja:
- Índice fuera de rango
- Entrada no numérica
"""
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear') 

def pausar_pantalla():
    input('Presiona enter para continuar...')    

def pedir_indice():
    while True:
        try:
            indice = int(input("que indice de la lista vas a buscar: "))
            if indice < 0:
                raise ValueError
            return indice
        except ValueError:  # Error si no se ingresa un número
            limpiar_pantalla()
            print("¡Error! Debes ingresar un número entero.")
            pausar_pantalla()
            limpiar_pantalla()
        except Exception as e:  # Cualquier otro error (genérico)
            limpiar_pantalla()
            print(f"Ocurrió un error inesperado: {e}")
            pausar_pantalla()
            limpiar_pantalla()
def buscar_indice(i,lista):
    try:
        numero = lista[i]
        print(f"numero: {numero}")
    except IndexError:  # Error si el índice no existe
        limpiar_pantalla()
        print("¡Error! El índice está fuera de rango.")
        pausar_pantalla()
        limpiar_pantalla()

def mostrar_lista(lista):
    limpiar_pantalla()
    print("lista:")
    print(lista)
    pausar_pantalla()
    limpiar_pantalla()
            
def inicializarejercicio():
    lista = [1,2,3,4,5]
    mostrar_lista(lista)
    indice = pedir_indice()
    buscar_indice(indice,lista)
    
inicializarejercicio()