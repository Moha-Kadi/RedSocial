### LIBRERÍAS ###
import os
from database import base_datos
from clases.publicacion import Publicacion, PublicacionDB
import settings

#   LOGIN   #
import logging
logging.basicConfig(level=logging.INFO, format="\n%(levelname)s: %(message)s")

### FUNCIONES ###
def limpiar_terminal():
    os.system("clear")

def pausar_terminal():
    input("« Pulse Enter para continuar... »")

# INSERTAMOS NUEVA PUBLICACIÓN A LA BASE DE DATOS #
def nueva_publicacion(datos): 
    base_datos.ejecutar_consulta(settings.CREAR_PUBLICACION, [*datos])

# IMPRIMIMOS INFORMACIÓN DE LAS PUBLICACIONES #
def listar_publicaciones(): 
    publicaciones = base_datos.ejecutar_consulta(settings.OBTENER_TODAS_PUBLICACIONES)
    return [PublicacionDB(*pub) for pub in publicaciones]

 # LISTAMOS PUBLICACIONES DE UN USUARIO #
def listar_publicaciones_usuario(id_usuario):
    publicacion_usuario = base_datos.ejecutar_consulta(settings.OBTENER_PUBLICACION_A_TRAVES_ID_USUARIO, [id_usuario]) 
    return [PublicacionDB(*pub) for pub in publicacion_usuario]

# EDITAMOS EL CONTENIDO DE UNA PUBLICACIÓN #
def editar_publicacion(id_publicacion,nuevo_contenido): 
    publicacion_editada = base_datos.ejecutar_consulta(settings.ACTUALIZAR_PUBLICACION, [nuevo_contenido,id_publicacion])
    return [PublicacionDB(*pub) for pub in publicacion_editada]

# ELIMINAMOS PUBLICACIÓN DE LA BASE DE DATOS #
def eliminar_publicacion(id): 
    borrar_publicacion = base_datos.ejecutar_consulta(settings.BORRAR_PUBLICACION, id) 
    return [PublicacionDB(*pub) for pub in borrar_publicacion]

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
                base_datos.commit()
                break
            
            case "1":
                print("\n*** CREAR NUEVA PUBLICACIÓN ***\n")
                id_usuario = input("Introduzca ID de usuario: ")
                contenido = input("Introduzca contenido para la publicacion: ")
                publicacion = Publicacion(id_usuario=id_usuario, contenido=contenido)
                nueva_publicacion(publicacion.info())

                logging.info("✅ Publicación agregada Correctamente.\n")

            case "2":
                print("\n*** LISTAR PUBLICACIONES ***\n")
                for publicacion in listar_publicaciones():
                    print(publicacion)
                    print()

            case "3":
                print("\n*** LISTAR PUBLICACIONES DE UN USUARIO ***\n")
                id_usuario = input("Introduzca ID de usuario: ")
                for pub_usr in listar_publicaciones_usuario(id_usuario=id_usuario):
                    print(f"\n{pub_usr}\n")

            case "4":
                print("\n*** EDITAR CONTENIDO PUBLICACIÓN ***\n")
                id_publicacion = input("Introduzca ID de la publicación: ")
                nuevo_contenido = input("Introduzca nuevo contenido: ")
                editar_publicacion(id_publicacion=id_publicacion, nuevo_contenido=nuevo_contenido)
                
                logging.info("✅ Contenido actualizado Correctamente.\n")

            case "5":
                print("\n*** ELIMINAR PUBLICACIÓN ***\n")
                id = input("Introduzca ID de publicación: ")
                eliminar_publicacion(id=id)
                
                logging.info("✅ Publicación eliminada Correctamente.\n")

            case _:
                print("\nERROR. Elija una opción válida\n")

        pausar_terminal()
