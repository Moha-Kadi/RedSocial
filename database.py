### LIBRERÍAS ###
import sqlite3  # IMPORTAMOS PARA HACER LA CONEXIÓN CON LA BASE DE DATOS #
from settings import DB

class BaseDatos:
    def __init__(self):
        self.__conexion = sqlite3.connect(DB)
        self.__cursor = self.__conexion.cursor()

### MÉTODOS DE LA CLASE BASEDATOS ###

#   EJECUTAR CONSULTA
    def ejecutar_consulta(self, consulta, variables=[]):
        try:
            self.__cursor.execute("PRAGMA foreign_keys = ON;")
            consulta = self.__cursor.execute(consulta,variables)
            return consulta.fetchall()
        except Exception as ex:
            print(f"Se ha producido un ERROR de tipo: {type(ex)}")

#   COMMIT PARA GUARDAR CAMBIOS        
    def commit(self):
        try:
            self.__conexion.commit()
        except Exception as ex:
            print(f"Se ha producido un ERROR: {ex}")

#   CERRAR CONEXIÓN CON LA BASE DE DATOS
    def cerrar_conecion(self):
        self.__conexion.close()


### INSTANCIA DE CLASE ###
base_datos = BaseDatos()
