### LIBRERÍAS ###
import os
from clases import publicacion
from database import base_datos

### FUNCIONES ###
def limpiar_terminal():
    os.system("clear")

def pausar_terminal():
    input("« Pulse Enter para continuar... »")

def nueva_publicacion(): # INSERTAMOS NUEVA PUBLICACIÓN A LA BASE DE DATOS #
    pass 

def listar_publicaciones(): # IMPRIMIMOS INFORMACIÓN DE LAS PUBLICACIONES #
    pass 

def listar_publicaciones_usuario(): # LISTAMOS PUBLICACIONES DE UN USUARIO #
    pass 

def editar_publicacion(): # EDITAMOS EL CONTENIDO DE UNA PUBLICACIÓN #
    pass 

def eliminar_publicacion(): # ELIMINAMOS PUBLICACIÓN DE LA BASE DE DATOS #
    pass 

def gestion_publicaciones():
    
    while True:
        limpiar_terminal()

        print("""
    ++++++++++++++
         MENÚ
    ++++++++++++++
            
    0 - SALIR
    1 - CREAR NUEVA PUBLICACIÓN
    2 - LISTAR TODAS LAS PUBLICACIONES
    3 - LISTAR PUBLICACIONES DE UN USUARIO 
    4 - EDITAR CONTENIDO PUBLICACIÓN
    5 - ELIMINAR PUBLICACIÓN
    """)

        opcion = input("Elige una de las opciones: ")

        limpiar_terminal()

        match opcion:
            case "0":
                break
            case "1":
                print("\n*** CREAR NUEVA PUBLICACIÓN ***\n")
            case "2":
                print("\n*** LISTAR PUBLICACIONES ***\n")
            case "3":
                print("\n*** LISTAR PUBLICACIONES DE UN USUARIO ***\n")
            case "4":
                print("\n*** EDITAR CONTENIDO PUBLICACIÓN ***\n")
            case "5":
                print("\n*** ELIMINAR PUBLICACIÓN ***\n")
            case _:
                print("\nERROR. Elija una opción válida\n")

        pausar_terminal()
