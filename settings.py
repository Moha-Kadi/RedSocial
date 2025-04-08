### LIBRERÍAS ###
import os
from dotenv import load_dotenv
import sqlite3 as sq

### CARGAMOSS LAS VARIABLE DE ENTORNO DEL ARCHIVO .ENV ###
load_dotenv()

DB_PATH = os.path.dirname(os.path.abspath(__file__)) + os.sep
DB_FILE = os.getenv("DB")
DB = DB_PATH + DB_FILE


### DDBB - CREACIÓN DE TABLA (CLIENTES) ###
CREATE_TABLES_SQL = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    fecha_registro DATE DEFAULT CURRENT_DATE
);


CREATE TABLE IF NOT EXISTS publicaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);
"""

INSERT_USUARIOS_SQL = "INSERT INTO usuarios (nombre, apellido, correo) VALUES (?, ?, ?)"

INSERT_PUBLICACIONES_SQL = "INSERT INTO publicaciones (id_usuario, contenido) VALUES (?, ?)"

### DDBB - INSERTAR DATOS INICIALES ##
Insert_DatosIniciales_Usuarios = [
    ("Leonardo", "Caballero", "leonardo@mail.com"),
    ("Ana", "Poleo", "ana@mail.com"),
    ("Manuel", "Matos", "manuel@mail.com"),
]

Insert_DatosIniciales_Publicaciones = [
    (2, "¡Hola a todos!"),
    (3, "Estoy aprendiendo Python y SQLite"),
]



### INSERTAMOS DATOS INICIALES A LA BASE DE DATOS ###
# if __name__ == "__main__":
#     with base_datos.connect(DB) as conexion:
#         cursor = conexion.cursor()
#         try:
#             cursor.executescript(CREATE_TABLES_SQL)
          
#             cursor.executemany(INSERT_USUARIOS_SQL, Insert_DatosIniciales_Usuarios)
#             cursor.executemany(INSERT_PUBLICACIONES_SQL, Insert_DatosIniciales_Publicaciones)
            
#         finally:
#             cursor.close()

### USUARIOS ###
# AÑADIR USUARIO 
CREAR_USUARIO = "INSERT INTO usuarios (nombre, apellido, correo) VALUES (?, ?, ?)"
# MOSTRAR USUARIOS 
MOSTRAR_USUARIOS = "SELECT * FROM usuarios"
# MOSTRAR USUARIO POR CORREO / NOMBRE 
CONSULTAR_USUARIO_CORREO = "SELECT * FROM usuarios WHERE correo = ?"
# ACTUALIZAR CORREO
ACTUALIZAR_CORREO = "UPDATE usuarios SET correo = ? WHERE id = ?"
# ELIMINAR USUARIO 
ELIMINAR_USUARIO = "DELETE FROM usuarios WHERE id = ?"


    ### PUBLICACIONES ###
#   CREAR PUBLICACION
CREAR_PUBLICACION = "INSERT INTO publicaciones (id_usuario, contenido) VALUES (?,?)"
#   OBTENER TODAS LAS PUBLICACIONES
OBTENER_TODAS_PUBLICACIONES = "SELECT * FROM publicaciones"
#   PUBLICIONES DE UN USUARIO
OBTENER_PUBLICACION_A_TRAVES_ID_USUARIO = "SELECT * FROM publicaciones WHERE id_usuario = ?"
#   ACTUALIZAR PUBLICACION
ACTUALIZAR_PUBLICACION = "UPDATE publicaciones SET contenido = ? WHERE id = ?"
#   BORRAR PUBLICACION
BORRAR_PUBLICACION = "DELETE FROM publicaciones WHERE id = ?"


    ### CONSULTAS ###
#   USUARIOS REGISTROS DE HACE UN MES
CONSULTA_REGISTRO_UTL_MES = """
    SELECT * FROM usuarios
    WHERE fecha_registro BETWEEN ? AND ?;
"""
#   TOTAL PUBLICACIONES POR USUARIO
NUMERO_DE_PUBLICACIONES_POR_USUARIO = """
    SELECT u.nombre, COUNT(p.id) AS num_publicaciones
    FROM usuarios u
    LEFT JOIN publicaciones p ON u.id = p.id_usuario
    GROUP BY u.id
    ORDER BY num_publicaciones DESC
""" 
#   USUARIOS CON MÁS DE 3 PUBLICACIONES

#   PUBLICACIONES MÁS ANTIGUAS
CONSULTA_PUBLICACIONES_MAS_ANTIGUAS = """
    SELECT * FROM publicaciones
    ORDER BY fecha_publicacion ASC LIMIT 5;
    """

#   CONSULTA FILTRADA POR PALABRA CLAVE
CONSULTA_PALABRA_CLAVE = """
    SELECT * FROM publicaciones
        WHERE contenido LIKE ?;
    """