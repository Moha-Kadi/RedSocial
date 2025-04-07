### DEFINICIÓN DE CLASES ###
class Usuario:
    def __init__(self, nombre:str, apellido:str, correo:str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        

### GETTERs y SETTERs ###
#   NOMBRE
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, value):
        self.__nombre = value
#   APELLIDO
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, value):
        self.__apellido = value
#   CORREO
    def get_correo(self):
        return self.__correo
    def set_correo(self, value):
        self.__correo = value

    def info(self):
        return [self.get_nombre(), self.get_apellido(), self.get_correo()]

    def __str__(self):
        return f" - Nombre: {self.get_nombre()}\n - Apellido: {self.get_apellido()}\n - Email: {self.get_correo()}"
    

class UsuarioDB(Usuario):
    def __init__(self, id, nombre, apellido, correo, fecha_registro):
        super().__init__(nombre, apellido, correo)

        self.__id = id
        self.__fecha_registro = fecha_registro

### GETTERs y SETTERs ###
#   ID
    def get_id(self):
        return self.__id
    def set_id(self, value):
        self.__id = value
#   FECHA REGISTRO
    def get_fecha_registro(self):
        return self.__fecha_registro
    def set_fecha_registro(self, value):
        self.__fecha_registro = value


    def __str__(self):
        return  f" - ID: {self.get_id()}\n{super().__str__()}\n - Fecha Regristro: {self.get_fecha_registro()}"
    