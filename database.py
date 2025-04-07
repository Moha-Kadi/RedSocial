### LIBRERÍAS ###
import sqlite3  # IMPORTAMOS PARA HACER LA CONEXIÓN CON LA BASE DE DATOS #
from settings import DB

class BaseDatos:
    def __init__(self):
        self.__conexion = sqlite3.connect(DB)
        self.__cursor = self.__conexion.cursor()

    def ejecutar_consulta(self, consulta, variables=[]):

        # try:
        consulta = self.__cursor.execute(consulta,variables)
        return consulta.fetchall()
        # except Exception as ex:
        #     print(f"Se ha producido un ERROR de tipo: {type(ex)}")
        
    def commit(self):
        try:
            self.__conexion.commit()
        except Exception as ex:
            print(f"Se ha producido un ERROR: {ex}")

    def cerrar_conecion(self):
        self.__conexion.close()

    def insertar_valores():
        pass

base_datos = BaseDatos()
#base_datos.ejecutar_consulta()