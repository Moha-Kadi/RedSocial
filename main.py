### LIBRERÍAS ###
import os
from database import base_datos

### MEŃUS ###
from menus import gestionar_usuarios
from menus import gestionar_publicaciones
from menus import gestionar_consultas

### FUNCIONES ###
def limpiar_terminal():
    os.system("clear")

def pausar_terminal():
    input("« Pulse Enter para continuar... »")

#   MENÚ PRINCIPAL
def menu():
    while True:
        limpiar_terminal()

        print("""
    ++++++++++++++
         MENÚ
    ++++++++++++++
            
    0 - SALIR
    1 - GESTIÓN USUARIOS
    2 - GESTIÓN PUBLICACIONES
    3 - CONSULTAS AVANZADAS BBDD
    """)

        opcion = input("Elige una de las opciones: ")

        limpiar_terminal()

        match opcion:
            case "0":
                base_datos.cerrar_conecion()
                print("\nQue tengas un buen día\n")
                break
            case "1":
                gestionar_usuarios.gestion_usuarios()
            case "2":
                gestionar_publicaciones.gestion_publicaciones()
                pass
            case "3":
                gestionar_consultas.gestion_consultas()
            case _:
                print("\nERROR. Elija una opción válida\n")

        pausar_terminal()


### COMIENZA EL PROGRAMA ###
menu()