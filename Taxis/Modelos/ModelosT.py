import mariadb
# import hashlib

class Conexion():

    def conn(self):
        try:
            conn=mariadb.connect(host='localhost',user='root',password='', database='base_taxi')
            return conn
        except mariadb.Error as e:
            return e

    def consulta(self, consulta, parametros:tuple, option:int):
        conexion=self.conn()
        cursor=conexion.cursor()
        if option==0: #SET QUERY
            try:
                cursor.execute(consulta,parametros)
                conexion.commit()
                rows=cursor.rowcount
                return rows
            except mariadb.Error as e:
                return e
            finally:
                conexion.close()
        else: #GET QUERY
            try:
                cursor.execute(consulta,parametros)
                conexion.commit()
                fetch=cursor.fetchall()
                return fetch
            except mariadb.Error as e:
                return e
            finally:
                conexion.close()

class Usuarios(Conexion):

    def crearUsuario(self, usuario:str, contrasenia:str, role:int):
        verificar=self.verificarUsuarioNoExista(usuario)
        if verificar==[]:
            consulta="INSERT INTO usuarios(usuario,contrasenia,id_rol) VALUES (?,?,?)"
            execute=self.consulta(consulta,(usuario,contrasenia,role),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
                return respuesta
        else:
            respuesta="El usuario ya existe"
        return respuesta

    def seleccionarUsuarios(self, usuarioId:int=0):
        if usuarioId==0:
            consulta="SELECT u.*,r.rol FROM usuarios as u INNER JOIN roles as r ON u.id_rol=r.id"
            respuesta=self.consulta(consulta,(),1)
        else:
            consulta="SELECT u.*,r.rol FROM usuarios as u INNER JOIN roles as r ON u.id_rol=r.id WHERE u.id=?"
            respuesta=self.consulta(consulta,(usuarioId,),1)
        return respuesta

    def editarUsuarios(self, usuarioId:int, usuario:str, contrasenia:str, role:int):
        verificarId=self.seleccionarUsuarios(usuarioId)
        if verificarId!=[]:
            consulta="SELECT * FROM usuarios WHERE id!=? AND usuario=?"
            verificarUsuario=self.consulta(consulta,(usuarioId,usuario),1)
            if verificarUsuario==[]:
                consulta="UPDATE usuarios SET usuario=?, contrasenia=?, id_rol=? WHERE id=?"
                execute=self.consulta(consulta,(usuario,contrasenia,role,usuarioId),0)
                if type(execute)==int:
                    if execute>0:
                        respuesta=1
                    else:
                        respuesta=0
                else:
                    respuesta=execute
            else:
                respuesta="Ya existe ese nombre de usuario"
        else:
            respuesta="Usuario no existe"
        return respuesta

    def eliminarUsuario(self, usuarioId:int):
        verificarId=self.seleccionarUsuarios(usuarioId)
        if verificarId!=[]:
            consulta="DELETE FROM usuarios WHERE id=?"
            execute=self.consulta(consulta,(usuarioId,),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
        else:
            respuesta="Usuario no existe"
        return respuesta

    def verificarUsuarioNoExista(self, usuario:str):
        consulta="SELECT * FROM usuarios WHERE usuario=?"
        return self.consulta(consulta,(usuario,),1)

    # """def encriptar(self, contrasenia:str):
    #     encriptado=hashlib.md5(contrasenia.encode()).hexdigest()
    #     return encriptado"""

    def validarUsuario(self, ususario:str, contrasenia:str):
        verificarUsuario=self.verificarUsuarioNoExista(ususario)
        if verificarUsuario!=[]:
            if verificarUsuario[0][2]==contrasenia:
                datosUsuario=verificarUsuario[0]
                respuesta=datosUsuario
            else:
                respuesta="Contraseña Invalida"
        else:
            respuesta="Usuario no existe"
        return respuesta

class Socios(Conexion):

    def crearSocio(self, nombre:str, apellido:str, cedula:str, telefono:str, ingreso:str):
        verificar=self.verificarSocioNoExista(cedula)
        if verificar==[]:
            consulta="INSERT INTO socios(nombre,apellido,cedula,telefono,fecha_ingreso,status) VALUES (?,?,?,?,?,1)"
            execute=self.consulta(consulta,(nombre,apellido,cedula,telefono,ingreso),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
        else:
            respuesta="Ya existe un socio con esa cedula"
        return respuesta

    def seleccionarSocio(self, socioId:int=0):
        if socioId==0:
            consulta="SELECT * FROM socios ORDER BY status DESC"
            respuesta=self.consulta(consulta,(),1)
        else:
            consulta="SELECT * FROM socios WHERE id=?"
            respuesta=self.consulta(consulta,(socioId,),1)
        return respuesta

    def actualizarSocio(self, socioId:int, nombre:str, apellido:str, cedula:str, telefono:str, status:int):
        verificarId=self.seleccionarSocio(socioId)
        if verificarId!=[]:
            consulta="SELECT * FROM socios WHERE id!=? AND cedula=?"
            verificarCedula=self.consulta(consulta,(socioId,cedula),1)
            if verificarCedula==[]:
                consulta="UPDATE socios SET nombre=?,apellido=?,cedula=?,telefono=?,status=? WHERE id=?"
                execute=self.consulta(consulta,(nombre,apellido,cedula,telefono,status,socioId),0)
                if type(execute)==int:
                    if execute>0:
                        respuesta=1
                    else:
                        respuesta=0
                else:
                    respuesta=execute
            else:
                respuesta="Ya existe esa cedula en otro socio"
        else:
            respuesta="Socio no existe"
        return respuesta

    def eliminarSocio(self, socioId:int):
        verificarId=self.seleccionarSocio(socioId)
        if verificarId!=[]:
            consulta="UPDATE socios SET status=0 WHERE id=?"
            execute=self.consulta(consulta,(socioId,),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
        else:
            respuesta="Socio no existe"
        return respuesta

    def verificarSocioNoExista(self, cedula:str):
        consulta="SELECT * FROM socios WHERE cedula=?"
        return self.consulta(consulta,(cedula,),1)

    def consultarVehiculosPorSocio(self, socioId:int):
        verificarId=self.seleccionarSocio(socioId)
        if verificarId!=[]:
            consulta="SELECT v.id,v.marca,v.modelo,v.anio,v.placa,v.id_socio,CONCAT(s.nombre,' ',s.apellido),s.cedula,v.disponible FROM vehiculos AS v INNER JOIN socios AS s ON v.id_socio=s.id WHERE s.id=? ORDER BY v.id ASC"
            execute=self.consulta(consulta,(socioId,),1)
        else:
            respuesta="No existe ese socio"
        return respuesta

class Vehiculos(Conexion):

    def __init__(self):
        self.socios=Socios()

    def crearVehiculo(self, marca:str, modelo:str, anio:str, placa:str, socioId:int):
        verificarPlaca=self.verificarPlacaNoExista(placa)
        if verificarPlaca==[]:
            verificarSocio=self.socios.seleccionarSocio(socioId)
            if verificarSocio!=[]:
                consulta="INSERT INTO vehiculos(marca,modelo,anio,placa,id_socio,disponible) VALUES(?,?,?,?,?,1)"
                execute=self.consulta(consulta,(marca,modelo,anio,placa,socioId),0)
                if type(execute)==int:
                    if execute>0:
                        respuesta=1
                    else:
                        respuesta=0
                else:
                    respuesta=execute
            else:
                respuesta="No existe ese id de socio"
        else:
            respuesta="Ya existe esa placa en otro vehiculo"
        return respuesta

    def seleccionarVehiculo(self, vehiculoId:int=0):
        if vehiculoId==0:
            consulta="SELECT * FROM vehiculos ORDER BY id_socio ASC"
            respuesta=self.consulta(consulta,(),1)
        else:
            consulta=f"SELECT * FROM vehiculos WHERE id='{vehiculoId}'"
            respuesta=self.consulta(consulta,(vehiculoId,),1)
        return respuesta

    def actualizarVehiculo(self, vehiculoId:int, marca:str, modelo:str, anio:str, placa:str, socioId:int):
        verificarId=self.seleccionarVehiculo(vehiculoId)
        if verificarId!=[]:
            consulta="SELECT * FROM vehiculos WHERE id!=? AND placa=?"
            verificarPlaca=self.consulta(consulta,(vehiculoId,placa),1)
            if verificarPlaca==[]:
                verificarSocio=self.socios.seleccionarSocio(socioId)
                if verificarSocio!=[]:
                    consulta="UPDATE vehiculos SET marca=?,modelo=?,anio=?,placa=?,id_socio=? WHERE id=?"
                    execute=self.consulta(consulta,(marca,modelo,anio,placa,socioId,vehiculoId),0)
                    if type(execute)==int:
                        if execute>0:
                            respuesta=1
                        else:
                            respuesta=0
                    else:
                        respuesta=execute
                else:
                    respuesta="No existe ese socio"
            else:
                respuesta="Ya existe esa placa en otro vehiculo"
        else:
            respuesta="No existe ese vehiculo"
        return respuesta

    def actualizarDisponibilidad(self, vehiculoId:int):
        verificarId=self.seleccionarVehiculo(vehiculoId)
        if verificarId!=[]:
            if verificarId[0][6]==0:
                consulta="UPDATE vehiculos SET disponible=1 WHERE id=?"
            else:
                consulta="UPDATE vehiculos SET disponible=0 WHERE id=?"
            execute=self.consulta(consulta,(vehiculoId,),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
        else:
            respuesta="No existe ese vehiculo"
        return respuesta

    def eliminarVehiculo(self, vehiculoId:int):
        verificarId=self.seleccionarVehiculo(vehiculoId)
        if verificarId!=[]:
            consulta="DELETE FROM vehiculos WHERE id=?"
            execute=self.consulta(consulta,(vehiculoId,),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
        else:
            respuesta="No existe ese vehiculo"
        return respuesta

    def verificarPlacaNoExista(self, placa:str):
        consulta="SELECT * FROM vehiculos WHERE placa=?"
        return self.consulta(consulta,(placa,),1)

    def verificarDisponibilidadVehiculo(self, vehiculoId:int):
        consulta="SELECT * FROM vehiculos WHERE id=? AND disponible=1"
        return self.consulta(consulta,(vehiculoId,),1)

class Clientes(Conexion):

    def crearCliente(self, nombre:str, apellido:str, telefonoUno:str, direccion:str, ingreso:str, telefonoDos:str=""):
        verificarTelefono=self.verificarTelefonoNoExista(telefonoUno)
        if verificarTelefono==[]:
            consulta="INSERT INTO clientes(nombre,apellido,telefono_uno,telefono_dos,direccion,fecha_ingreso,status) VALUES (?,?,?,?,?,?,1)"
            execute=self.consulta(consulta,(nombre,apellido,telefonoUno,telefonoDos,direccion,ingreso),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
        else:
            respuesta="Ya existe ese numero de telefono"
        return respuesta

    def seleccionarCliente(self, clienteId:int=0):
        if clienteId==0:
            consulta="SELECT * FROM clientes"
            respuesta=self.consulta(consulta,(),1)
        else:
            consulta="SELECT * FROM clientes WHERE id=?"
            respuesta=self.consulta(consulta,(clienteId,),1)
        return respuesta

    def actualizarCliente(self, clienteId:int, nombre:str, apellido:str, telefonoUno:str, direccion:str,status:str, telefonoDos:str=""):
        verificarId=self.seleccionarCliente(clienteId)
        if verificarId!=[]:
            consulta="SELECT * FROM clientes WHERE id!=? AND telefono_uno=?"
            verificarTelf=self.consulta(consulta,(clienteId,telefonoUno),1)
            if verificarTelf==[]:
                consulta="UPDATE clientes SET nombre=?,apellido=?,telefono_uno=?,telefono_dos=?,direccion=?,status=? WHERE id=?"
                execute=self.consulta(consulta,(nombre,apellido,telefonoUno,telefonoDos,direccion,status,clienteId),0)
                if type(execute)==int:
                    if execute>0:
                        resultado=1
                    else:
                        resultado=1
                else:
                    resultado=execute
            else:
                resultado="Ya existe ese telefono en otro cliente"
        else:
            resultado="No existe ese cliente"
        return resultado

    def eliminarCliente(self, clienteId:int):
        verificarId=self.seleccionarCliente(clienteId)
        if verificarId!=[]:
            consulta="UPDATE clientes SET status=0 WHERE id=?"
            execute=self.consulta(consulta,(clienteId,),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
        else:
            respuesta="No existe ese cliente"
        return respuesta

    def verificarTelefonoNoExista(self, telefono:str):
        consulta="SELECT * FROM clientes WHERE telefono_uno=?"
        return self.consulta(consulta,(telefono,),1)

    def verificarClienteActivo(self, clienteId:int):
        consulta="SELECT * FROM clientes WHERE id=? AND status=1"
        return self.consulta(consulta,(clienteId,),1)

class Carreras(Conexion):

    def __init__(self):
        self.vehiculo=Vehiculos()
        self.cliente=Clientes()

    def crearCarrera(self, carroId:int, clienteId:int, fechaCarrera:str, precio:float, destino:str):
        verificarVehiculo=self.vehiculo.verificarDisponibilidadVehiculo(carroId)
        if verificarVehiculo!=[]:
            verificarCliente=self.cliente.verificarClienteActivo(clienteId)
            if verificarCliente!=[]:
                consulta="INSERT INTO carreras(id_carro,id_cliente,fecha_carrera,precio,destino) VALUES (?,?,?,?,?)"
                execute=self.consulta(consulta,(carroId,clienteId,fechaCarrera,precio,destino),0)
                if type(execute)==int:
                    if execute>0:
                        respuesta=1
                        self.vehiculo.actualizarDisponibilidad(carroId)
                    else:
                        respuesta=0
                else:
                    respuesta=execute
            else:
                respuesta="Ese clienete no está activo, verifica por favor"
        else:
            respuesta="El vehiculo no existe o no está disponible, verifica por favor"
        return respuesta

    def seleccionarCarreras(self, carreraId:int=0):
        if carreraId==0:
            consulta="SELECT * FROM carreras"
            respuesta=self.consulta(consulta,(),1)
        else:
            consulta="SELECT * FROM carreras WHERE id=?"
            respuesta=self.consulta(consulta,(carreraId,),1)
        return respuesta

    def actualizarCarreras(self, carreraId:int, carroId:int, clienteId:int, precio:float, destino:str):
        verificarId=self.seleccionarCarreras(carreraId)
        if verificarId!=[]:
            verificarCliente=self.cliente.verificarClienteActivo(clienteId)
            if verificarCliente!=[]:
                consulta="UPDATE carreras SET id_carro=?,id_cliente=?,precio=?,destino=? WHERE id=?"
                execute=self.consulta(consulta,(carroId,clienteId,precio,destino,carreraId),0)
                if type(execute)==int:
                    if execute>0:
                        respuesta=1
                    else:
                        respuesta=0
                else:
                    respuesta=execute
            else:
                respuesta="Ese clienete no está activo, verifica por favor"
        else:
            respuesta="No existe ese registro de carrera"
        return respuesta

    def eliminarCarrera(self, carreraId:int):
        verificarId=self.seleccionarCarreras(carreraId)
        if verificarId!=[]:
            consulta="DELETE FROM carreras WHERE id=?"
            execute=self.consulta(consulta,(carreraId,),0)
            if type(execute)==int:
                if execute>0:
                    respuesta=1
                else:
                    respuesta=0
            else:
                respuesta=execute
        else:
            respuesta="No existe ese registro de carrera"
        return respuesta

    def buscarCarrerasPorFecha(self, fecha:str):
        consulta="SELECT * FROM carreras WHERE fecha_carrera=?"
        return self.consulta(consulta,(fecha,),1)