### LIBRERÍAS ###
import os
from database import base_datos
import settings
import datetime
from clases.usuario import UsuarioDB
from clases.publicacion import PublicacionDB

### FUNCIONES ###
def limpiar_terminal():
    os.system("clear")

def pausar_terminal():
    input("« Pulse Enter para continuar... »")

def registro_ultimo_mes(): # CONSULTA DE TODOS LOS USUARIOS REGISTRADOS EL ÚLTIMO MES #
    fecha_actual = datetime.datetime.today()
    fecha_mes_atras = fecha_actual-datetime.timedelta(days=30)
    consulta_mes = base_datos.ejecutar_consulta(settings.CONSULTA_REGISTRO_UTL_MES, [fecha_mes_atras, fecha_actual])
    return [UsuarioDB(*con) for con in consulta_mes]

def cantidad_total_publicaciones(): # CANTIDAD TOTAL DE PUBLICACIONES POR USUARIO #
    publi_usuarios = base_datos.ejecutar_consulta(settings.NUMERO_DE_PUBLICACIONES_POR_USUARIO)
    return publi_usuarios

def num_publicaciones_usuario(): # USUARIOS CON MÁS DE 3 PUBLICACIONES #
    usuario3_publicaciones = base_datos.ejecutar_consulta(settings.USUARIOS_MAS_3_PUBLICACIONES)
    return usuario3_publicaciones

def publicaciones_antiguas(): # PUBLICACIONES MÁS ANTIGUAS #
    publicaciones_antiguas = base_datos.ejecutar_consulta(settings.CONSULTA_PUBLICACIONES_MAS_ANTIGUAS)
    return [PublicacionDB(*con) for con in publicaciones_antiguas] 

def publicaciones_palabra_clave(palabra): # BUSCAR PUBLICACIONES POR PALABRA CLAVE #
    palabra_clave = base_datos.ejecutar_consulta(settings.CONSULTA_PALABRA_CLAVE, ["%"+palabra+"%"])
    return [PublicacionDB(*usr) for usr in palabra_clave]

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
                for usuario in registro_ultimo_mes():
                    print(f"{usuario}\n")
            case "2":
                print("\n*** TOTAL PUBLICACIONES POR USUARIO ***\n")
                for pub_usuario in cantidad_total_publicaciones():
                    print(f" - Usuario: {pub_usuario[0]}\n - Nº Publicaciones: {pub_usuario[1]}\n")
            case "3":
                print("\n*** USUARIOS CON +3 PUBLICACIONES ***\n")
                for usuario3 in num_publicaciones_usuario():
                    print(f"\n - Usuario: {usuario3[0]}\n - Total de: {usuario3[1]} publicaciones\n")
            case "4":
                print("\n*** PUBLICACIONES MAS ANTIGUAS ***\n")
                for publi in publicaciones_antiguas():
                    print(f"{publi}\n")
            case "5":
                print("\n*** FILTRAR PUBLICACIONES POR PALABRA CLAVE ***\n")
                palabra_clave = input("Introduzca palabra clave: ")
                for palabra in publicaciones_palabra_clave(palabra=palabra_clave):
                    print(f"\n{palabra}\n")
            case _:
                print("\nERROR. Elija una opción válida\n")

        pausar_terminal()
