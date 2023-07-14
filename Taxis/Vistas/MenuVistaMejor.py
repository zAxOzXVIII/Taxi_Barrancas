from Controladores.controlador import *
from tkinter import ttk, Label, Toplevel, END, CENTER, NO
from tkinter import font, messagebox
from tkcalendar import DateEntry

class MenuVista:

    def __init__(self, window, data):
        self.window=window
        # Configurando color de la raiz window
        self.window.configure(bg="#cdd5e7")
        # configurando el resizable
        self.window.resizable(width=True, height=False)
        self.window.geometry("800x480")
        # Data de modelo
        self.data=data
        self.usuarioControlador=UsuarioControlador()
        self.sociosControlador=SociosContolador()
        self.vehiculosControlador=VehiculosControlador()
        self.clientesControlador=ClientesControlador()
        self.carrerasControlador=CarrerasControlador()
        self.mainView()

#VISTA PRINCIPAL

    def mainView(self):
        self.limpiar_pantalla_window()
        options = ["Configurar usuarios", "Configurar socios", "Configurar vehiculos",
                    "Configurar clientes", "Configurar carreras"]
        Label(self.window, bg="#ccd4eb", text=f"Bienvenido {self.data[1]}").grid(row=0, column=0, columnspan=2, padx=160, pady=(0, 25))

        Label(self.window, bg="#ccd4eb", text=options[0]).grid(row=1, column=0, padx=(0, 0), pady=(0, 10))
        ttk.Button(self.window, text="Usuarios", command = lambda : self.config_usuarios_interfaz()).grid(row=1, column=1, padx=(0, 185), pady=(0, 10))

        Label(self.window, bg="#ccd4eb", text=options[1]).grid(row=2, column=0, padx=(0, 0), pady=(0, 10))
        ttk.Button(self.window, text="Socios", command = lambda : self.config_socios_interfaz()).grid(row=2, column=1, padx=(0, 185), pady=(0, 10))

        Label(self.window, bg="#ccd4eb", text=options[2]).grid(row=3, column=0, padx=(0, 0), pady=(0, 10))
        ttk.Button(self.window, text="Vehiculos", command = lambda : self.config_vehiculos_interfaz()).grid(row=3, column=1, padx=(0, 185), pady=(0, 10))

        Label(self.window, bg="#ccd4eb", text=options[3]).grid(row=4, column=0, padx=(0, 0), pady=(0, 10))
        ttk.Button(self.window, text="Clientes", command = lambda:  self.config_clientes_interfaz()).grid(row=4, column=1, padx=(0, 185), pady=(0, 10))

        Label(self.window, bg="#ccd4eb", text=options[4]).grid(row=5, column=0, padx=(0, 0), pady=(0, 80))
        ttk.Button(self.window, text="Carreras", command = lambda : self.config_carreras_interfaz()).grid(row=5, column=1, padx=(0, 185), pady=(0, 80))

#FUNCIONES GENERALES

    def limpiar_pantalla_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def cerrar_toplevel(self, toplevel):
        toplevel.grab_release()
        toplevel.destroy()

    def set_column_width(self, treeview, column_index, width):
        treeview.column(column_index, width=width, minwidth=width, stretch= NO, anchor="w")

    def llenar_fila_prueba(self, treeview, valores = (), texto = "1"):
        treeview.insert('', 'end', text=texto, values=valores)

    def ajustar_ancho_columnas(self, treeview):
        if len(treeview.get_children()) == 0: return
        for column in treeview["columns"]:
            column_width = max(
                font.Font().measure(treeview.set(child, column)) for child in treeview.get_children()
                )
            self.set_column_width(treeview, column, column_width + 50)

    def validar_numerico(self, text, limit):
        if text.isdigit() and len(text) <= int(limit):
            return True
        elif text == "":
            return True
        else:
            return False

    def validate_entrys(self, *args):
        for entry in args:
            status=False if (entry=="" or entry=="S") else True
            if status==False:
                return False
        return status

    def validar_limite(self, text, limite):
        if len(text) < int(limite):
            return True
        else:
            return False

#VISTA DE USUARIOS

    def config_usuarios_interfaz(self):
        data_rol=self.data[3]
        self.limpiar_pantalla_window()
        Label(self.window, bg="#ccd4eb", text="Modulo de usuarios").grid(row=0, column=0, columnspan=2)
        #TABLA
        self.table_users = ttk.Treeview(self.window, height=10)
        self.table_users.grid(row=1, column=0, rowspan=3)
        self.table_users["columns"]=("c0", "c1", "c2")
        #CABECERAS DE COLUMNA
        self.table_users.heading(column="c0", text="Usuario")
        self.table_users.heading(column="c1", text="Rol ID")
        self.table_users.heading(column="c2", text="Rol")
        #LLENAR DATOS EN LA TABLA
        self.getUsers()
        #AJUSTAR ANCHO DE LAS COLUMNAS
        self.ajustar_ancho_columnas(self.table_users)
        self.table_users.column("#0", width=35, minwidth=35, stretch=NO)
        #BOTONES
        #AGREGAR
        ttk.Button(self.window, text="Crear usuario", command = self.generar_data_usuarios, state="normal" if data_rol == 1 or data_rol == 2 else "disabled").grid(row=1, column=1)
        #ELIMINAR
        ttk.Button(self.window, text="Eliminar usuario", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.borrar_usuario).grid(row=2, column=1)
        #EDITAR
        ttk.Button(self.window, text="Editar usuario", command = self.form_editar_usuario, state="normal" if data_rol == 1 or data_rol == 2 else "disabled").grid(row=3, column=1)
        #VOLVER
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView()).grid(row=4, column=0, columnspan=2)

    def getUsers(self):
        records=self.table_users.get_children()
        for element in records:
            self.table_users.delete(element)
        data=self.usuarioControlador.seleccionarUsuariosC()
        for usuario in data:
            self.table_users.insert('', 'end', text=usuario[0], values=(usuario[1],usuario[3],usuario[4]))

    def generar_data_usuarios(self):
        self.toplevel_usuarios_add = Toplevel(self.window)
        self.toplevel_usuarios_add.title("Agregar usuarios toplevel")
        # focus al toplevel
        self.toplevel_usuarios_add.grab_set()
        # Labels
        Label(self.toplevel_usuarios_add, text="Formulario para agregar usuarios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
        # validacion
        validacion_limite = self.toplevel_usuarios_add.register(self.validar_limite)
        Label(self.toplevel_usuarios_add, text="Usuario").grid(row=1, column=0, padx=40, pady=5)
        self.user = ttk.Entry(self.toplevel_usuarios_add, validate="key", validatecommand=(validacion_limite, '%P', 20))
        self.user.grid(row=1, column=1, padx=40, pady=5)

        Label(self.toplevel_usuarios_add, text="Contraseña").grid(row=2, column=0, padx=40, pady=5)
        self.password = ttk.Entry(self.toplevel_usuarios_add, validate="key", validatecommand=(validacion_limite, '%P', 20))
        self.password.grid(row=2, column=1, padx=40, pady=5)

        Label(self.toplevel_usuarios_add, text="Rol").grid(row=3, column=0, padx = 40, pady = 5)
        lista_rol = ["Seleccionar...", "1--Administrador", "2--Socio", "3--Cajera"]
        # Debe rellenar la lista con los roles caracteristicos

        self.status_combo = ttk.Combobox(self.toplevel_usuarios_add, values=lista_rol, state="readonly")
        self.status_combo.set(lista_rol[0])
        self.status_combo.grid(row=3, column=1)

        ttk.Button(self.toplevel_usuarios_add, text="Agregar", command=self.añadir_usuario).grid(row=4, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_usuarios_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_usuarios_add)).grid(row=4, column=1, padx=40, pady=(10, 25))

    def añadir_usuario(self):
        usuario=self.user.get()
        passw=self.password.get()
        rol=self.status_combo.get()
        rol=rol[0:1]

        if self.validate_entrys(usuario,passw,rol):
            respuesta=self.usuarioControlador.crearUsuarioC(usuario,passw,rol)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_usuarios_add.destroy()
                self.config_usuarios_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def form_editar_usuario(self):
        id=self.table_users.item(self.table_users.selection())["text"]
        dataOld=self.usuarioControlador.seleccionarUsuariosC(id)
        if id!="":
            self.toplevel_usuarios_add = Toplevel(self.window)
            self.toplevel_usuarios_add.title("Editar usuarios toplevel")
            self.toplevel_usuarios_add.grab_set()
            Label(self.toplevel_usuarios_add, text="Formulario para editar usuarios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
            # validacion
            validacion_limite = self.toplevel_usuarios_add.register(self.validar_limite)
            Label(self.toplevel_usuarios_add, text="Usuario").grid(row=1, column=0, padx=40, pady=5)
            self.user = ttk.Entry(self.toplevel_usuarios_add, validate="key", validatecommand=(validacion_limite, '%P', 20))
            self.user.grid(row=1, column=1, padx=40, pady=5)
            self.user.insert(0, dataOld[0][1])

            Label(self.toplevel_usuarios_add, text="Contraseña").grid(row=3, column=0, padx=40, pady=5)
            self.password = ttk.Entry(self.toplevel_usuarios_add, validate="key", validatecommand=(validacion_limite, '%P', 20))
            self.password.grid(row=3, column=1, padx=40, pady=5)
            self.password.insert(0, dataOld[0][2])

            Label(self.toplevel_usuarios_add, text="Rol").grid(row=4, column=0, padx = 40, pady = 5)
            lista_rol = ["Seleccionar...", "1--Administrador", "2--Socio", "3--Cajera"]
            lista_rol.insert(0, str(dataOld[0][3])+'-'+dataOld[0][4])
            # Debe rellenar la lista con los roles caracteristicos

            self.status_combo = ttk.Combobox(self.toplevel_usuarios_add, values=lista_rol, state="readonly")
            self.status_combo.set(lista_rol[0])
            self.status_combo.grid(row=4, column=1)

            ttk.Button(self.toplevel_usuarios_add, text="Actualizar", command=lambda:self.editar_usuario(id)).grid(row=5, column=0, padx=40, pady=(10, 25))
            ttk.Button(self.toplevel_usuarios_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_usuarios_add)).grid(row=5, column=1, padx=40, pady=(10, 25))
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

    def editar_usuario(self, idO):
        id=idO
        usuario=self.user.get()
        passw=self.password.get()
        rol=self.status_combo.get()
        rol=rol[0:1]

        if self.validate_entrys(id,usuario,passw,rol):
            respuesta=self.usuarioControlador.editarUsuariosC(id,usuario,passw,rol)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_usuarios_add.destroy()
                self.config_usuarios_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def borrar_usuario(self):
        id=self.table_users.item(self.table_users.selection())["text"]
        if id!="":
            if messagebox.askokcancel(title="Eliminar",message="Seguro que deseas eliminar?"):
                respuesta=self.usuarioControlador.eliminarUsuarioC(id)
                if type(respuesta)==int:
                    messagebox.showinfo(title="Alerta",message="Eliminado Correctamente")
                    self.config_usuarios_interfaz()
                else:
                    messagebox.showerror(self.window,respuesta)
            else:
                return
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

#SOCIOS
    def config_socios_interfaz(self):
        data_rol=self.data[3]
        # limpiar pantalla
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, bg="#ccd4eb", text="Modulo de socios").grid(row=0, column=0, columnspan=3)
        # Tabla
        self.table_socios = ttk.Treeview(self.window, height=10)
        self.table_socios.grid(row=1, column=0, columnspan=3)
        self.table_socios["columns"]=("c0", "c1", "c2", "c3", "c4", "c5")
        self.table_socios.heading(column="c0", text="Nombre")
        self.table_socios.heading(column="c1", text="Apellido")
        self.table_socios.heading(column="c2", text="Cedula")
        self.table_socios.heading(column="c3", text="Telefono")
        self.table_socios.heading(column="c4", text="Fecha de Ingreso")
        self.table_socios.heading(column="c5", text="Estatus")
        # llenar columna !!
        self.get_socios()
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_socios)
        self.table_socios.column("#0", width=35, minwidth=35, stretch=NO)
        # buttons
        ttk.Button(self.window, text="Crear socios", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.generar_data_socios).grid(row=2, column=0) #Toplevel
        ttk.Button(self.window, text="Eliminar socios", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.borrar_socio).grid(row=2, column=1)
        ttk.Button(self.window, text="Editar socios", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.form_editar_socio).grid(row=2, column=2)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView()).grid(row=3, column=0, columnspan=3)

    def get_socios(self):
        records=self.table_socios.get_children()
        for element in records:
            self.table_socios.delete(element)
        data=self.sociosControlador.seleccionarSocioC()
        for socio in data:
            self.table_socios.insert('', 'end', text=socio[0], values=(socio[1],socio[2],socio[3],socio[4],socio[5],socio[6]))

    def generar_data_socios(self):
        self.toplevel_socios_add = Toplevel(self.window)
        self.toplevel_socios_add.title("Agregar usuarios toplevel")
        # focus al toplevel
        self.toplevel_socios_add.grab_set()
        # Labels
        Label(self.toplevel_socios_add, text="Formulario para agregar socios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
        # validaciones
        validacion_limite = self.toplevel_socios_add.register(self.validar_limite)
        validacion_numerica = self.toplevel_socios_add.register(self.validar_numerico)
        Label(self.toplevel_socios_add, text="Nombre").grid(row=1, column=0, padx = 40, pady = 5)
        self.nombre = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        self.nombre.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="Apellido").grid(row=2, column=0, padx = 40, pady = 5)
        self.apellido = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        self.apellido.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="cedula").grid(row=3, column=0, padx = 40, pady = 5)
        self.ci = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        self.ci.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="telefono").grid(row=4, column=0, padx = 40, pady = 5)
        self.tlf = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        self.tlf.grid(row=4, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="Fecha ingreso").grid(row=5, column=0, padx = 40, pady = 5)
        self.fecha = DateEntry(self.toplevel_socios_add, date_pattern="y/mm/dd")
        self.fecha.grid(row=5, column=1, padx = 40, pady = 5)
        
        ttk.Button(self.toplevel_socios_add, text="Agregar", command=self.add_socio).grid(row=6, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_socios_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_socios_add)).grid(row=6, column=1, padx=40, pady=(10, 25))

    def add_socio(self):
        nombre=self.nombre.get()
        apellido=self.apellido.get()
        cedula=self.ci.get()
        telefono=self.tlf.get()
        fecha=self.fecha.get()

        if self.validate_entrys(nombre,apellido,cedula,telefono,fecha):
            respuesta=self.sociosControlador.crearSocioC(nombre,apellido,cedula,telefono,fecha)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_socios_add.destroy()
                self.config_socios_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def form_editar_socio(self):
        id=self.table_socios.item(self.table_socios.selection())["text"]
        dataOld=self.sociosControlador.seleccionarSocioC(id)
        if id!="":
            # generar toplevel
            self.toplevel_socios_add = Toplevel(self.window)
            self.toplevel_socios_add.title("Agregar usuarios toplevel")
            # focus al toplevel
            self.toplevel_socios_add.grab_set()
            # Labels
            Label(self.toplevel_socios_add, text="Formulario para agregar socios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
            # validaciones
            validacion_limite = self.toplevel_socios_add.register(self.validar_limite)
            validacion_numerica = self.toplevel_socios_add.register(self.validar_numerico)
            Label(self.toplevel_socios_add, text="Nombre").grid(row=1, column=0, padx = 40, pady = 5)
            self.nombre = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
            self.nombre.grid(row=1, column=1, padx = 40, pady = 5)
            self.nombre.insert(0, dataOld[0][1])

            Label(self.toplevel_socios_add, text="Apellido").grid(row=2, column=0, padx = 40, pady = 5)
            self.apellido = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
            self.apellido.grid(row=2, column=1, padx = 40, pady = 5)
            self.apellido.insert(0, dataOld[0][2])

            Label(self.toplevel_socios_add, text="cedula").grid(row=3, column=0, padx = 40, pady = 5)
            self.ci = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
            self.ci.grid(row=3, column=1, padx = 40, pady = 5)
            self.ci.insert(0, dataOld[0][3])

            Label(self.toplevel_socios_add, text="telefono").grid(row=4, column=0, padx = 40, pady = 5)
            self.tlf = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
            self.tlf.grid(row=4, column=1, padx = 40, pady = 5)
            self.tlf.insert(0, dataOld[0][4])

            Label(self.toplevel_socios_add, text="Estatus").grid(row=5, column=0, padx = 40, pady = 5)
            self.status = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 11))
            self.status.grid(row=5, column=1, padx = 40, pady = 5)
            self.status.insert(0, dataOld[0][6])

            ttk.Button(self.toplevel_socios_add, text="Actualizar", command=lambda:self.editar_socio(id)).grid(row=7, column=0, padx=40, pady=(10, 25))
            ttk.Button(self.toplevel_socios_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_socios_add)).grid(row=7, column=1, padx=40, pady=(10, 25))
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

    def editar_socio(self, idO):
        id=idO
        nombre=self.nombre.get()
        apellido=self.apellido.get()
        cedula=self.ci.get()
        telefono=self.tlf.get()
        status=self.status.get()

        if self.validate_entrys(id,nombre,apellido,cedula,telefono,status):
            respuesta=self.sociosControlador.actualizarSocioC(id,nombre,apellido,cedula,telefono,status)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_socios_add.destroy()
                self.config_socios_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def borrar_socio(self):
        id=self.table_socios.item(self.table_socios.selection())["text"]
        if id!="":
            if messagebox.askokcancel(title="Eliminar",message="Seguro que deseas eliminar?"):
                respuesta=self.sociosControlador.eliminarSocioC(id)
                if type(respuesta)==int:
                    messagebox.showinfo(title="Alerta",message="Eliminado Correctamente")
                    self.config_socios_interfaz()
                else:
                    messagebox.showerror(self.window,respuesta)
            else:
                return
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

#VEHICULOS

    def config_vehiculos_interfaz(self):
        data_rol=self.data[3]
        # limpiar pantalla
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, bg="#ccd4eb", text="Modulo de vehiculos").grid(row=0, column=0, columnspan=3)
        # Tabla
        self.table_vehiculos = ttk.Treeview(self.window, height=10)
        self.table_vehiculos.grid(row=1, column=0, columnspan=3)
        self.table_vehiculos["columns"]=("c0", "c1", "c2", "c3", "c4", "c5")
        self.table_vehiculos.heading(column="c0", text="Marca")
        self.table_vehiculos.heading(column="c1", text="Modelo")
        self.table_vehiculos.heading(column="c2", text="Año")
        self.table_vehiculos.heading(column="c3", text="Placa")
        self.table_vehiculos.heading(column="c4", text="ID Socio")
        self.table_vehiculos.heading(column="c5", text="Disponible")
        # llenar columna !!
        self.get_vehiculos()
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_vehiculos)
        self.table_vehiculos.column("#0", width=35, minwidth=35, stretch=NO)
        # buttons
        ttk.Button(self.window, text="Crear vehiculos", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.generar_data_vehiculos).grid(row=2, column=0) #Toplevel
        ttk.Button(self.window, text="Eliminar vehiculos", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.borrar_vehiculo).grid(row=2, column=1)
        ttk.Button(self.window, text="Editar vehiculos", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.form_editar_vehiculos).grid(row=2, column=2)
        ttk.Button(self.window, text="Cambiar Disponibilidad", command = self.disponibilidad).grid(row=2, column=3)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView()).grid(row=3, column=0, columnspan=3)

    def disponibilidad(self):
        id=self.table_vehiculos.item(self.table_vehiculos.selection())["text"]
        if id!="":
            respuesta=self.vehiculosControlador.actualizarDisponibilidad(id)
            if type(respuesta)==int:
                self.config_vehiculos_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

    def get_vehiculos(self):
        records=self.table_vehiculos.get_children()
        for element in records:
            self.table_vehiculos.delete(element)
        data=self.vehiculosControlador.seleccionarVehiculo()
        for v in data:
            self.table_vehiculos.insert('', 'end', text=v[0], values=(v[1],v[2],v[3],v[4],v[5],v[6]))

    def llenar_combobox_socio(self):
        data=self.sociosControlador.seleccionarSocioC()
        data_combo=[str(socio[0])+'-'+str(socio[3]) for socio in data]
        data_combo.insert(0, 'Seleccione...')
        return data_combo

    def generar_data_vehiculos(self):
        # generar toplevel
        self.toplevel_vehiculos_add = Toplevel(self.window)
        self.toplevel_vehiculos_add.title("Agregar usuarios toplevel")
        # focus al toplevel
        self.toplevel_vehiculos_add.grab_set()
        # Labels
        Label(self.toplevel_vehiculos_add, text="Formulario para agregar socios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
        # validaciones
        validacion_limite = self.toplevel_vehiculos_add.register(self.validar_limite)
        validacion_numerica = self.toplevel_vehiculos_add.register(self.validar_numerico)
        Label(self.toplevel_vehiculos_add, text="Marca").grid(row=1, column=0, padx = 40, pady = 5)
        self.marca = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 20))
        self.marca.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Modelo").grid(row=2, column=0, padx = 40, pady = 5)
        self.modelo = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 20))
        self.modelo.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Año").grid(row=3, column=0, padx = 40, pady = 5)
        self.year = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_numerica, "%P", 4))
        self.year.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Placa").grid(row=4, column=0, padx = 40, pady = 5)
        self.placa = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 15))
        self.placa.grid(row=4, column=1, padx = 40, pady = 5)
        # llenar lista idsocio con los socios disponibles

        Label(self.toplevel_vehiculos_add, text="ID Socio").grid(row=6, column=0, padx = 40, pady = 5)
        self.idSocio_combo = ttk.Combobox(self.toplevel_vehiculos_add, state="readonly", values=self.llenar_combobox_socio())
        self.idSocio_combo.grid(row=6, column=1)

        ttk.Button(self.toplevel_vehiculos_add, text="Agregar", command=self.add_vehiculo).grid(row=7, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_vehiculos_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_vehiculos_add)).grid(row=7, column=1, padx=40, pady=(10, 25))

    def add_vehiculo(self):
        marca=self.marca.get()
        modelo=self.modelo.get()
        anio=self.year.get()
        placa=self.placa.get()
        idSocio=self.idSocio_combo.get()
        idSocio=idSocio[0:1]

        if self.validate_entrys(marca,modelo,anio,placa,idSocio):
            respuesta=self.vehiculosControlador.crearVehiculoC(marca,modelo,anio,placa,idSocio)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_vehiculos_add.destroy()
                self.config_vehiculos_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def llenar_combobox_socio_actu(self, id):
        data=self.sociosControlador.seleccionarSocioC()
        dataid=self.sociosControlador.seleccionarSocioC(id)
        data_combo=[str(socio[0])+'-'+str(socio[3]) for socio in data]
        data_combo.insert(0, str(dataid[0][0])+'-'+str(dataid[0][3]))
        return data_combo

    def form_editar_vehiculos(self):
        id=self.table_vehiculos.item(self.table_vehiculos.selection())["text"]
        dataOld=self.vehiculosControlador.seleccionarVehiculoC(id)
        if id!="":
            # generar toplevel
            self.toplevel_vehiculos_add = Toplevel(self.window)
            self.toplevel_vehiculos_add.title("Agregar usuarios toplevel")
            # focus al toplevel
            self.toplevel_vehiculos_add.grab_set()
            # Labels
            Label(self.toplevel_vehiculos_add, text="Formulario para agregar socios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
            # validaciones
            validacion_limite = self.toplevel_vehiculos_add.register(self.validar_limite)
            validacion_numerica = self.toplevel_vehiculos_add.register(self.validar_numerico)
            Label(self.toplevel_vehiculos_add, text="Marca").grid(row=1, column=0, padx = 40, pady = 5)
            self.marca = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 20))
            self.marca.grid(row=1, column=1, padx = 40, pady = 5)
            self.marca.insert(0, dataOld[0][1])
            
            Label(self.toplevel_vehiculos_add, text="Modelo").grid(row=2, column=0, padx = 40, pady = 5)
            self.modelo = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 20))
            self.modelo.grid(row=2, column=1, padx = 40, pady = 5)
            self.modelo.insert(0, dataOld[0][2])
            
            Label(self.toplevel_vehiculos_add, text="Año").grid(row=3, column=0, padx = 40, pady = 5)
            self.year = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_numerica, "%P", 4))
            self.year.grid(row=3, column=1, padx = 40, pady = 5)
            self.year.insert(0, dataOld[0][3])
            
            Label(self.toplevel_vehiculos_add, text="Placa").grid(row=4, column=0, padx = 40, pady = 5)
            self.placa = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 15))
            self.placa.grid(row=4, column=1, padx = 40, pady = 5)
            self.placa.insert(0, dataOld[0][4])

            Label(self.toplevel_vehiculos_add, text="ID Socio").grid(row=6, column=0, padx = 40, pady = 5)
            self.idSocio_combo = ttk.Combobox(self.toplevel_vehiculos_add, state="readonly", values=self.llenar_combobox_socio_actu(dataOld[0][5]))
            self.idSocio_combo.grid(row=6, column=1)

            ttk.Button(self.toplevel_vehiculos_add, text="Actualizar", command=lambda:self.actualizar_vehiculo(id)).grid(row=7, column=0, padx=40, pady=(10, 25))
            ttk.Button(self.toplevel_vehiculos_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_vehiculos_add)).grid(row=7, column=1, padx=40, pady=(10, 25))
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

    def actualizar_vehiculo(self, idO):
        id=idO
        marca=self.marca.get()
        modelo=self.modelo.get()
        anio=self.year.get()
        placa=self.placa.get()
        idSocio=self.idSocio_combo.get()
        idSocio=idSocio[0:1]

        if self.validate_entrys(id,marca,modelo,anio,placa,idSocio):
            respuesta=self.vehiculosControlador.actualizarVehiculoC(id,marca,modelo,anio,placa,idSocio)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_vehiculos_add.destroy()
                self.config_vehiculos_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def borrar_vehiculo(self):
        id=self.table_vehiculos.item(self.table_vehiculos.selection())["text"]
        if id!="":
            if messagebox.askokcancel(title="Eliminar",message="Seguro que deseas eliminar?"):
                respuesta=self.vehiculosControlador.eliminarVehiculo(id)
                if type(respuesta)==int:
                    messagebox.showinfo(title="Alerta",message="Eliminado Correctamente")
                    self.config_vehiculos_interfaz()
                else:
                    messagebox.showerror(self.window,respuesta)
            else:
                return
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

#CLIENTES

    def config_clientes_interfaz(self):
        data_rol=self.data[3]
        # limpiar pantalla
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, bg="#ccd4eb", text="Modulo de clientes").grid(row=0, column=0, columnspan=3)
        # Tabla
        self.table_clientes = ttk.Treeview(self.window, height=10)
        self.table_clientes.grid(row=1, column=0, columnspan=3)
        self.table_clientes["columns"]=("c0", "c1", "c2", "c3", "c4", "c5", "c6")
        self.table_clientes.heading(column="c0", text="Nombre")
        self.table_clientes.heading(column="c1", text="Apellido")
        self.table_clientes.heading(column="c2", text="Telefono 1")
        self.table_clientes.heading(column="c3", text="Telefono 2")
        self.table_clientes.heading(column="c4", text="Direccion")
        self.table_clientes.heading(column="c5", text="Fecha ingreso")
        self.table_clientes.heading(column="c6", text="Estatus")
        # llenar columna !!
        self.get_clientes()
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_clientes)
        self.table_clientes.column("#0", width=35, minwidth=35, stretch=NO)
        # buttons
        ttk.Button(self.window, text="Crear clientes", state="normal", command = self.generar_data_clientes).grid(row=2, column=0) #Toplevel
        ttk.Button(self.window, text="Eliminar clientes", state="normal", command = self.borrar_cliente).grid(row=2, column=1)
        ttk.Button(self.window, text="Editar clientes", state="normal", command = self.form_editar_cliente).grid(row=2, column=2)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView()).grid(row=3, column=0, columnspan=3)

    def get_clientes(self):
        records=self.table_clientes.get_children()
        for element in records:
            self.table_clientes.delete(element)
        data=self.clientesControlador.seleccionarClienteC()
        for c in data:
            self.table_clientes.insert('', 'end', text=c[0], values=(c[1],c[2],c[3],c[4],c[5],c[6],c[7]))

    def generar_data_clientes(self):
        self.toplevel_clientes_add = Toplevel(self.window)
        self.toplevel_clientes_add.title("Agregar clientes toplevel")
        # focus al toplevel
        self.toplevel_clientes_add.grab_set()
        # Labels
        Label(self.toplevel_clientes_add, text="Formulario para agregar clientes").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
        # validaciones
        validacion_limite = self.toplevel_clientes_add.register(self.validar_limite)
        validacion_numerica = self.toplevel_clientes_add.register(self.validar_numerico)
        Label(self.toplevel_clientes_add, text="Nombre").grid(row=1, column=0, padx = 40, pady = 5)
        self.nombre = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        self.nombre.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Apellido").grid(row=2, column=0, padx = 40, pady = 5)
        self.apellido= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        self.apellido.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Telefono 1").grid(row=3, column=0, padx = 40, pady = 5)
        self.telefono1 = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        self.telefono1.grid(row=3, column=1, padx = 40, pady = 5)

        Label(self.toplevel_clientes_add, text="Telefono 2").grid(row=4, column=0, padx = 40, pady = 5)
        self.telefono2 = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        self.telefono2.grid(row=4, column=1, padx = 40, pady = 5)

        Label(self.toplevel_clientes_add, text="Direccion").grid(row=5, column=0, padx = 40, pady = 5)
        self.dirc= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 50))
        self.dirc.grid(row=5, column=1, padx = 40, pady = 5)

        Label(self.toplevel_clientes_add, text="Fecha ingreso").grid(row=6, column=0, padx = 40, pady = 5)
        self.fecha= DateEntry(self.toplevel_clientes_add)
        self.fecha.grid(row=6, column=1, padx = 40, pady = 5)

        ttk.Button(self.toplevel_clientes_add, text="Añadir", command=self.add_cliente).grid(row=8, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_clientes_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_clientes_add)).grid(row=8, column=1, padx=40, pady=(10, 25))

    def add_cliente(self):
        nombre=self.nombre.get()
        apellido=self.apellido.get()
        telefono1=self.telefono1.get()
        telefono2=self.telefono2.get()
        direccion=self.dirc.get()
        fecha=self.fecha.get_date()

        if self.validate_entrys(nombre,apellido,telefono1,direccion,fecha):
            respuesta=self.clientesControlador.crearClienteC(nombre,apellido,telefono1,direccion,fecha,telefono2)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_clientes_add.destroy()
                self.config_clientes_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def form_editar_cliente(self):
        id=self.table_clientes.item(self.table_clientes.selection())["text"]
        dataOld=self.clientesControlador.seleccionarClienteC(id)
        if id!="":
            self.toplevel_clientes_add = Toplevel(self.window)
            self.toplevel_clientes_add.title("Agregar clientes toplevel")
            # focus al toplevel
            self.toplevel_clientes_add.grab_set()
            # Labels
            Label(self.toplevel_clientes_add, text="Formulario para agregar clientes").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
            # validaciones
            validacion_limite = self.toplevel_clientes_add.register(self.validar_limite)
            validacion_numerica = self.toplevel_clientes_add.register(self.validar_numerico)
            Label(self.toplevel_clientes_add, text="Nombre").grid(row=1, column=0, padx = 40, pady = 5)
            self.nombre = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
            self.nombre.grid(row=1, column=1, padx = 40, pady = 5)
            self.nombre.insert(0, dataOld[0][1])
            
            Label(self.toplevel_clientes_add, text="Apellido").grid(row=2, column=0, padx = 40, pady = 5)
            self.apellido= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
            self.apellido.grid(row=2, column=1, padx = 40, pady = 5)
            self.apellido.insert(0, dataOld[0][2])
            
            Label(self.toplevel_clientes_add, text="Telefono 1").grid(row=3, column=0, padx = 40, pady = 5)
            self.telefono1 = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
            self.telefono1.grid(row=3, column=1, padx = 40, pady = 5)
            self.telefono1.insert(0, dataOld[0][3])

            Label(self.toplevel_clientes_add, text="Telefono 2").grid(row=4, column=0, padx = 40, pady = 5)
            self.telefono2 = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
            self.telefono2.grid(row=4, column=1, padx = 40, pady = 5)
            self.telefono2.insert(0, dataOld[0][4])

            Label(self.toplevel_clientes_add, text="Direccion").grid(row=5, column=0, padx = 40, pady = 5)
            self.dirc= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 50))
            self.dirc.grid(row=5, column=1, padx = 40, pady = 5)
            self.dirc.insert(0, dataOld[0][5])

            Label(self.toplevel_clientes_add, text="Estatus").grid(row=6, column=0, padx = 40, pady = 5)
            self.status= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 50))
            self.status.grid(row=6, column=1, padx = 40, pady = 5)
            self.status.insert(0, dataOld[0][7])

            ttk.Button(self.toplevel_clientes_add, text="Actualizar", command=lambda:self.actualizar_cliente(id)).grid(row=7, column=0, padx=40, pady=(10, 25))
            ttk.Button(self.toplevel_clientes_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_clientes_add)).grid(row=7, column=1, padx=40, pady=(10, 25))
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

    def actualizar_cliente(self, idO):
        id=idO
        nombre=self.nombre.get()
        apellido=self.apellido.get()
        telefono1=self.telefono1.get()
        telefono2=self.telefono2.get()
        direccion=self.dirc.get()
        status=self.status.get()

        if self.validate_entrys(id,nombre,apellido,telefono1,direccion,status):
            respuesta=self.clientesControlador.actualizarCliente(id,nombre,apellido,telefono1,direccion,status,telefono2)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_clientes_add.destroy()
                self.config_clientes_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def borrar_cliente(self):
        id=self.table_clientes.item(self.table_clientes.selection())["text"]
        if id!="":
            if messagebox.askokcancel(title="Eliminar",message="Seguro que deseas eliminar?"):
                respuesta=self.clientesControlador.eliminarClienteC(id)
                if type(respuesta)==int:
                    messagebox.showinfo(title="Alerta",message="Eliminado Correctamente")
                    self.config_clientes_interfaz()
                else:
                    messagebox.showerror(self.window,respuesta)
            else:
                return
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return

#CARRERAS

    def config_carreras_interfaz(self):
        data_rol=self.data[3]
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, bg="#ccd4eb", text="Modulo de carreras").grid(row=0, column=0, columnspan=2)
        # Tabla
        self.table_carreras = ttk.Treeview(self.window, height=10)
        self.table_carreras.grid(row=1, column=0, rowspan=3)
        self.table_carreras["columns"]=("c0", "c1", "c2", "c3", "c4")
        self.table_carreras.heading(column="#0", text="ID")
        self.table_carreras.heading(column="c0", text="ID Carro")
        self.table_carreras.heading(column="c1", text="ID Cliente")
        self.table_carreras.heading(column="c2", text="Fecha Carrera")
        self.table_carreras.heading(column="c3", text="Precio")
        self.table_carreras.heading(column="c4", text="Destino")
        # asignando data
        self.get_carreras()
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_carreras)
        # ajustando columna 
        self.table_carreras.column("#0", width=35, minwidth=35, stretch=NO, anchor="w")
        # buttons
        ttk.Button(self.window, text="Crear carreras", state="normal", command = self.generar_data_carreras).grid(row=1, column=1) #Toplevel
        ttk.Button(self.window, text="Eliminar carreras", state="normal", command=self.borrar_carrera).grid(row=2, column=1)
        ttk.Button(self.window, text="Editar carreras", state="normal", command = self.form_editar_carrera).grid(row=3, column=1)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView()).grid(row=4, column=0, columnspan=2)

    def get_carreras(self):
        records=self.table_carreras.get_children()
        for element in records:
            self.table_carreras.delete(element)
        data=self.carrerasControlador.seleccionarCarreraC()
        for c in data:
            self.table_carreras.insert('', 'end', text=c[0], values=(c[1],c[2],c[3],c[4],c[5]))

    def llenar_combobox_carro(self):
        data=self.vehiculosControlador.seleccionarVehiculoC()
        data_combo=[str(carro[0])+'-'+str(carro[1])+' '+str(carro[2])+' Placa:'+str(carro[4]) for carro in data]
        data_combo.insert(0, 'Seleccione...')
        return data_combo

    def llenar_combobox_cliente(self):
        data=self.clientesControlador.seleccionarClienteC()
        data_combo=[str(c[0])+'-'+str(c[3]) for c in data]
        data_combo.insert(0, 'Seleccione...')
        return data_combo

    def generar_data_carreras(self):
        self.toplevel_carreras_add = Toplevel(self.window)
        self.toplevel_carreras_add.title("Agregar usuarios toplevel")
        # focus al toplevel
        self.toplevel_carreras_add.grab_set()
        # Labels
        Label(self.toplevel_carreras_add, text="Formulario para agregar usuarios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
        # validacion
        validacion_limite = self.toplevel_carreras_add.register(self.validar_limite)
        validacion_numerica = self.toplevel_carreras_add.register(self.validar_numerico)
        Label(self.toplevel_carreras_add, text="ID de carro").grid(row=1, column=0, padx = 40, pady = 5)
        self.carro_combo = ttk.Combobox(self.toplevel_carreras_add, values=self.llenar_combobox_carro(), state="readonly")
        self.carro_combo.grid(row=1, column=1)

        Label(self.toplevel_carreras_add, text="ID de cliente").grid(row=2, column=0, padx = 40, pady = 5)
        self.cliente_combo = ttk.Combobox(self.toplevel_carreras_add, values=self.llenar_combobox_cliente(), state="readonly")
        self.cliente_combo.grid(row=2, column=1)

        Label(self.toplevel_carreras_add, text="Fecha de la carrera").grid(row=3, column=0, padx = 40, pady = 5)
        self.fecha = DateEntry(self.toplevel_carreras_add)
        self.fecha.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_carreras_add, text="Costo de la carrera").grid(row=4, column=0, padx = 40, pady = 5)
        self.cost_c = ttk.Entry(self.toplevel_carreras_add, validate="key", validatecommand=(validacion_numerica, '%P', 9))
        self.cost_c.grid(row=4, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_carreras_add, text="Destino de la carrera").grid(row=5, column=0, padx = 40, pady = 5)
        self.dir_c = ttk.Entry(self.toplevel_carreras_add, validate="key", validatecommand=(validacion_limite, '%P', 50))
        self.dir_c.grid(row=5, column=1, padx = 40, pady = 5)
        
        ttk.Button(self.toplevel_carreras_add, text="Agregar", command=self.add_carrera).grid(row=6, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_carreras_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_carreras_add)).grid(row=6, column=1, padx=40, pady=(10, 25))

    def add_carrera(self):
        carroid=self.carro_combo.get()
        clienteid=self.cliente_combo.get()
        fecha=self.fecha.get_date()
        costo=self.cost_c.get()
        dir=self.dir_c.get()
        carroid=carroid[0:1]
        clienteid=clienteid[0:1]

        if self.validate_entrys(carroid,clienteid,fecha,costo,dir):
            respuesta=self.carrerasControlador.crearCarreraC(carroid,clienteid,fecha,costo,dir)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_carreras_add.destroy()
                self.config_carreras_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def llenar_combobox_carroActu(self, id):
        dataOld=self.vehiculosControlador.seleccionarVehiculoC(id)
        data=self.vehiculosControlador.seleccionarVehiculoC()
        data_combo=[str(carro[0])+'-'+str(carro[1])+' '+str(carro[2])+' Placa:'+str(carro[4]) for carro in data]
        data_combo.insert(0, str(dataOld[0][0])+'-'+str(dataOld[0][1])+' '+str(dataOld[0][2])+' Placa:'+str(dataOld[0][4]))
        return data_combo

    def llenar_combobox_clienteActu(self, id):
        dataOld=self.clientesControlador.seleccionarClienteC(id)
        data=self.clientesControlador.seleccionarClienteC()
        data_combo=[str(c[0])+'-'+str(c[3]) for c in data]
        data_combo.insert(0, str(dataOld[0][0])+'-'+str(dataOld[0][3]))
        return data_combo

    def form_editar_carrera(self):
        id=self.table_carreras.item(self.table_carreras.selection())["text"]
        dataOld=self.carrerasControlador.seleccionarCarreraC(id)
        if id!="":
            self.toplevel_carreras_add = Toplevel(self.window)
            self.toplevel_carreras_add.title("Agregar usuarios toplevel")
            # focus al toplevel
            self.toplevel_carreras_add.grab_set()
            # Labels
            Label(self.toplevel_carreras_add, text="Formulario para agregar usuarios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
            # validacion
            validacion_limite = self.toplevel_carreras_add.register(self.validar_limite)
            validacion_numerica = self.toplevel_carreras_add.register(self.validar_numerico)
            Label(self.toplevel_carreras_add, text="ID de carro").grid(row=1, column=0, padx = 40, pady = 5)
            self.carro_combo = ttk.Combobox(self.toplevel_carreras_add, values=self.llenar_combobox_carroActu(dataOld[0][1]), state="readonly")
            self.carro_combo.grid(row=1, column=1)

            Label(self.toplevel_carreras_add, text="ID de cliente").grid(row=2, column=0, padx = 40, pady = 5)
            self.cliente_combo = ttk.Combobox(self.toplevel_carreras_add, values=self.llenar_combobox_clienteActu(dataOld[0][2]), state="readonly")
            self.cliente_combo.grid(row=2, column=1)

            Label(self.toplevel_carreras_add, text="Costo de la carrera").grid(row=4, column=0, padx = 40, pady = 5)
            self.cost_c = ttk.Entry(self.toplevel_carreras_add, validate="key", validatecommand=(validacion_numerica, '%P', 9))
            self.cost_c.grid(row=4, column=1, padx = 40, pady = 5)
            self.cost_c.insert(0, dataOld[0][4])
            
            Label(self.toplevel_carreras_add, text="Destino de la carrera").grid(row=5, column=0, padx = 40, pady = 5)
            self.dir_c = ttk.Entry(self.toplevel_carreras_add, validate="key", validatecommand=(validacion_limite, '%P', 50))
            self.dir_c.grid(row=5, column=1, padx = 40, pady = 5)
            self.dir_c.insert(0, dataOld[0][5])
            
            ttk.Button(self.toplevel_carreras_add, text="Agregar", command=lambda:self.editar_carrera(id)).grid(row=6, column=0, padx=40, pady=(10, 25))
            ttk.Button(self.toplevel_carreras_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_carreras_add)).grid(row=6, column=1, padx=40, pady=(10, 25))
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            
            return

    def editar_carrera(self, idO):
        id=idO
        carroid=self.carro_combo.get()
        clienteid=self.cliente_combo.get()
        costo=self.cost_c.get()
        dir=self.dir_c.get()
        carroid=carroid[0:1]
        clienteid=clienteid[0:1]

        if self.validate_entrys(id,carroid,clienteid,costo,dir):
            respuesta=self.carrerasControlador.actualizarCarreraC(id,carroid,clienteid,costo,dir)
            if type(respuesta)==int:
                self.limpiar_pantalla_window()
                self.toplevel_carreras_add.destroy()
                self.config_carreras_interfaz()
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showerror(self.window, "Ningún campo puede estar vacío")

    def borrar_carrera(self):
        id=self.table_carreras.item(self.table_carreras.selection())["text"]
        if id!="":
            if messagebox.askokcancel(title="Eliminar",message="Seguro que deseas eliminar?"):
                respuesta=self.carrerasControlador.eliminarCarreraC(id)
                if type(respuesta)==int:
                    messagebox.showinfo(title="Alerta",message="Eliminado Correctamente")
                    self.config_carreras_interfaz()
                else:
                    messagebox.showerror(self.window,respuesta)
            else:
                return
        else:
            messagebox.showwarning(self.window, "Elija un registro")
            return
