### LIBRERÍAS ###
import os
import settings
from clases.usuario import Usuario, UsuarioDB

#   INFO    #
import logging
logging.basicConfig(level=logging.INFO, format="\n%(levelname)s: %(message)s")

#from clases import usuario
from database import base_datos

### FUNCIONES ###
def limpiar_terminal():
    os.system("clear")

def pausar_terminal():
    input("« Pulse Enter para continuar... »")

# NUEVO INSERT A LA BASE DE DATOS #
def nuevo_usuario(datos): 
    base_datos.ejecutar_consulta(settings.CREAR_USUARIO,[*datos])         

# PRINT DE TODOS LOS USUARIOS DE LA BASE DE DATOS #
def listar_usuarios(): 
    usuarios = base_datos.ejecutar_consulta(settings.MOSTRAR_USUARIOS)
    return [UsuarioDB(*usr) for usr in usuarios]

# BUSCAMOS USUARIO A TRAVÉS DEL NOMBRE O CORRE #
def buscar_usuario(correo): 
    correo_usuario = base_datos.ejecutar_consulta(settings.CONSULTAR_USUARIO_CORREO, [correo])
    return [UsuarioDB(*usr) for usr in correo_usuario]
    
# ACTUALIZAMOS CORREO DE USUARIO #
def actualizar_correo(id,correo): 
    correo_actualizado = base_datos.ejecutar_consulta(settings.ACTUALIZAR_CORREO, [correo, id])
    return [UsuarioDB(*usr) for usr in correo_actualizado]

# ELIMINAMOS USUARIO DE LA BASE DE DATOS #
def eliminar_usuario(id): 
    borrar_usuario = base_datos.ejecutar_consulta(settings.ELIMINAR_USUARIO, id)
    return [UsuarioDB(*usr) for usr in borrar_usuario]

def gestion_usuarios():
    
    while True:
        limpiar_terminal()

        print("""
    ++++++++++++++
         MENÚ
    ++++++++++++++
            
    0 - SALIR
    1 - REGISTRAR NUEVO CLIENTE
    2 - LISTAR TODOS LOS USUARIOS
    3 - BUSCAR UN USUARIO POR CORREO 
    4 - ACTUALIZAR CORREO USUARIO
    5 - ELIMINAR USUARIO
    """)

        opcion = input("Elige una de las opciones: ")

        limpiar_terminal()

        match opcion:
            case "0":
                base_datos.commit()
                break

            case "1":
                print("\n*** REGISTRAR NUEVO CLIENTE ***\n")
                
                nombre = input("Introduzca nombre: ")
                apellido = input("Introduzca apellido: ")
                correo = input("Introduzca correo: ")

                usuario_nuevo = Usuario(nombre=nombre, apellido=apellido, correo=correo)

                nuevo_usuario(usuario_nuevo.info())

                logging.info("✅ Cliente agregado Correctamente.\n")

            case "2":
                print("\n*** LISTAR USUARIOS ***\n")
                for usuario in listar_usuarios():
                    print(f"{usuario}\n")
                    # print(f" - ID: {usuario[0]}\n - Nombre: {usuario[1]}\n - Apellido: {usuario[2]}\n - Correo: {usuario[3]}\n - Fecha Registro {usuario[4]}")
                
            case "3":
                print("\n*** BUSCAR USUARIO ***\n")
                correo = input("Introduzca un correo: ")
                for usuario in buscar_usuario(correo):
                    print(f"\n{usuario}\n")

            case "4":
                print("\n*** ACTUALIZAR CORREO ***\n")
                id = input("Introduzca ID del usuario: ")
                nuevo_correo = input("Introduzca nuevo correo: ")
                actualizar_correo(id,nuevo_correo)
                
                logging.info("✅ Correo actualizado Correctamente.\n")

            case "5":
                print("\n*** ELIMINAR USUARIO ***\n")
                id = input("Introduzca ID del usuario: ")
                eliminar_usuario(id)
                
                logging.info("✅ Cliente eliminado Correctamente.\n")

            case _:
                print("\nERROR. Elija una opción válida\n")

        pausar_terminal()
