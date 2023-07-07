from Modelos.ModelosT import *

class UsuarioControlador(Usuarios):

    def crearUsuarioC(self, usuario:str, contrasenia:str, role:int):
        respuesta=super().crearUsuario(usuario,contrasenia,role)
        return respuesta

    def seleccionarUsuariosC(self, usuarioId:int=0):
        respuesta=super().seleccionarUsuarios(usuarioId)
        return respuesta

    def editarUsuariosC(self, usuarioId: int, usuario: str, contrasenia: str, role: int):
        respuesta=super().editarUsuarios(usuarioId, usuario, contrasenia, role)
        return respuesta

    def eliminarUsuarioC(self, usuarioId: int):
        respuesta=super().eliminarUsuario(usuarioId)
        return respuesta

    def validarUsuarioC(self, ususario: str, contrasenia: str):
        respuesta=super().validarUsuario(ususario, contrasenia)
        return respuesta

class SociosContolador(Socios):

    def crearSocioC(self, nombre:str, apellido:str, cedula:str, telefono:str, ingreso:str):
        respuesta=super().crearSocio(nombre,apellido,cedula,telefono,ingreso)
        return respuesta

    def seleccionarSocioC(self, socioId:int=0):
        respuesta=super().seleccionarSocio(socioId)
        return respuesta

    def actualizarSocioC(self, socioId:int, nombre:str, apellido:str, cedula:str, telefono:str, ingreso:str):
        respuesta=super().actualizarSocio(socioId,nombre,apellido,cedula,telefono,ingreso)
        return respuesta

    def eliminarSocioC(self, socioId:int):
        respuesta=super().eliminarSocio(socioId)
        return respuesta

    def buscarSocioPorCedula(self, cedula:str):
        respuesta=super().verificarSocioNoExista(cedula)
        return respuesta

    def consultarVehiculosPorSocioC(self, socioId:int):
        respuesta=super().consultarVehiculosPorSocio(socioId)
        return respuesta

class VehiculosControlador(Vehiculos):

    def crearVehiculoC(self, marca:str, modelo:str, anio:str, placa:str, socioId:int):
        respuesta=super().crearVehiculo(marca, modelo, anio, placa, socioId)
        return respuesta

    def seleccionarVehiculoC(self, vehiculoId:int=0):
        respuesta=super().seleccionarVehiculo(vehiculoId)
        return respuesta

    def actualizarVehiculoC(self, vehiculoId:int, marca:str, modelo:str, anio:str, placa:str, socioId:int):
        respuesta=super().actualizarVehiculo(vehiculoId, marca, modelo, anio, placa, socioId)
        return respuesta

    def actualizarDisponibilidad(self, vehiculoId:int):
        respuesta=super().actualizarDisponibilidad(vehiculoId)
        return respuesta

    def eliminarVehiculo(self, vehiculoId:int):
        respuesta=super().eliminarVehiculo(vehiculoId)
        return respuesta

    def buscarVehiculoPorPlaca(self, placa:str):
        respuesta=super().verificarPlacaNoExista(placa)
        return respuesta

class ClientesControlador(Clientes):

    def crearClienteC(self, nombre:str, apellido:str, telefonoUno:str, direccion:str, ingreso:str, telefonoDos:str=""):
        respuesta=super().crearCliente(nombre, apellido, telefonoUno, direccion, ingreso, telefonoDos)
        return respuesta

    def seleccionarClienteC(self, clienteId:int=0):
        respuesta=super().seleccionarCliente(clienteId)
        return respuesta

    def actualizarCliente(self, clienteId:int, nombre:str, apellido:str, telefonoUno:str, direccion:str, status:int, telefonoDos:str=""):
        respuesta=super().actualizarCliente(clienteId, nombre, apellido, telefonoUno, direccion, status, telefonoDos)
        return respuesta

    def eliminarClienteC(self, clienteId:int):
        respuesta=super().eliminarCliente(clienteId)
        return respuesta

    def buscarClientePorTelefono(self, telefono:str):
        respuesta=super().verificarTelefonoNoExista(telefono)
        return respuesta

class CarrerasControlador(Carreras):

    def crearCarreraC(self, carroId:int, clienteId:int, fechaCarrera:str, precio:float, destino:str):
        respuesta=super().crearCarrera(carroId, clienteId, fechaCarrera, precio, destino)
        return respuesta

    def seleccionarCarreraC(self, carreraId:int=0):
        respuesta=super().seleccionarCarreras(carreraId)
        return respuesta

    def actualizarCarreraC(self, carreraId:int, carroId:int, clienteId:int, fechaCarrera:str, precio:float, destino:str):
        respuesta=super().actualizarCarreras(carreraId, carroId, clienteId, fechaCarrera, precio, destino)
        return respuesta

    def eliminarCarreraC(self, carreraId:int):
        respuesta=super().eliminarCarrera(carreraId)
        return respuesta

    def buscarCarrerasPorFechaC(self, fecha: str):
        respuesta=super().buscarCarrerasPorFecha(fecha)
        return respuesta
