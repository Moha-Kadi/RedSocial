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
DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL,
    fecha_registro DATE DEFAULT CURRENT_DATE
);

DROP TABLE IF EXISTS publicaciones;
CREATE TABLE publicaciones (
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
    (1, "Mi primera publicación en la red social"),
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


### AÑADIR USUARIO ###
CREAR_USUARIO = "INSERT INTO usuarios (nombre, apellido, correo) VALUES (?, ?, ?)"

### MOSTRAR USUARIOS ###
MOSTRAR_USUARIOS = "SELECT * FROM usuarios"

### MOSTRAR USUARIO POR CORREO / NOMBRE ##
CONSULTAR_USUARIO_CORREO = "SELECT * FROM usuarios WHERE correo = ?"

### ACTUALIZAR CORREO ###
ACTUALIZAR_CORREO = "UPDATE usuarios SET correo = ? WHERE id = ?"