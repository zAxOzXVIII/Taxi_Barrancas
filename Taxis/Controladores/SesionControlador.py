from Modelos.ModelosT import *

class SesionControlador(Usuarios):

    def validarUsuarioC(self, ususario: str, contrasenia: str):
        respuesta=super().validarUsuario(ususario, contrasenia)
        return respuesta