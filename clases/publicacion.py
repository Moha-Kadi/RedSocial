### DEFINICIÓN DE CLASES ###
class Publicacion:
    def __init__(self, id_usuario, contenido):
        self.__id_usuario = id_usuario
        self.__contenido = contenido
        
### GETTERs Y SETTERs ###
#   ID USUARIO
    def get_id_usuario(self):
        return self.__id_usuario
#   CONTENIDO
    def get_contenido(self):
        return self.__contenido
    def set_contenido(self, value):
        self.__contenido = value

    def info(self):
        return [self.get_id_usuario(), self.get_contenido()]

    def __str__(self):
        return f" - ID_Usuario: {self.get_id_usuario()}\n - Contenido: {self.get_contenido()}"

class PublicacionDB(Publicacion):
    def __init__(self, id_publicacion, id_usuario, contenido, fecha_publicacion):
        super().__init__(id_usuario, contenido)

        self.id_publicacion = id_publicacion
        self.fecha_publicacion = fecha_publicacion

### GETTERs Y SETTERs ###
#   ID PUBLICACION
    def get_id_publicacion(self):
        return self.id_publicacion
    def set_id_publicacion(self, value):
        self.id_publicacion = value
#   FECHA PUBLICACION
    def get_fecha_publicacion(self):
        return self.fecha_publicacion
    def set_fecha_publicacion(self, value):
        self.fecha_publicacion = value

    def __str__(self):
        return f" - ID: {self.get_id_publicacion()}\n{super().__str__()}\n - Fecha Publicacion: {self.get_fecha_publicacion()}"