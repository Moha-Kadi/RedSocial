### LIBRERÍAS ###
import os
from database import base_datos

### FUNCIONES ###
def limpiar_terminal():
    os.system("clear")

def pausar_terminal():
    input("« Pulse Enter para continuar... »")

def registro_ultimo_mes(): # CONSULTA DE TODOS LOS USUARIOS REGISTRADOS EL ÚLTIMO MES #
    pass 

def cantidad_total_publicaciones(): # CANTIDAD TOTAL DE PUBLICACIONES POR USUARIO #
    pass 

def num_publicaciones_usuario(): # USUARIOS CON MÁS DE 3 PUBLICACIONES #
    pass 

def publicaciones_antiguas(): # PUBLICACIONES MÁS ANTIGUAS #
    pass 

def publicaciones_palabra_clave(): # BUSCAR PUBLICACIONES POR PALABRA CLAVE #
    pass 

def gestion_consultas():
    
    while True:
        limpiar_terminal()

        print("""
    ++++++++++++++
         MENÚ
    ++++++++++++++
            
    0 - SALIR
    1 - USUARIOS REGISTRADOS EN EL ÚLTIMO MES
    2 - CANTIDAD TOTAL PUBLICACIONES POR USUARIO
    3 - USUARIOS CON +3 PUBLICACIONES
    4 - MOSTRAR PUBLICACIONES MAS ANTIGUAS
    5 - FILTRAR PUBLICACIONES POR PALABRA CLAVE
    """)

        opcion = input("Elige una de las opciones: ")

        limpiar_terminal()

        match opcion:
            case "0":
                break
            case "1":
                print("\n*** USUARIOS REGISTRADOS EN EL ÚLTIMO MES ***\n")
                registro_ultimo_mes()
            case "2":
                print("\n*** TOTAL PUBLICACIONES POR USUARIO ***\n")
                cantidad_total_publicaciones()
            case "3":
                print("\n*** USUARIOS CON +3 PUBLICACIONES ***\n")
                num_publicaciones_usuario()
            case "4":
                print("\n*** PUBLICACIONES MAS ANTIGUAS ***\n")
                publicaciones_antiguas()
            case "5":
                print("\n*** FILTRAR PUBLICACIONES POR PALABRA CLAVE ***\n")
                publicaciones_palabra_clave()
            case _:
                print("\nERROR. Elija una opción válida\n")

        pausar_terminal()
