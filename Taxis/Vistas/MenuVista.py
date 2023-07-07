from Controladores.controlador import *

from tkinter import ttk, Label, Toplevel, END, CENTER, NO
from tkinter import font
from tkcalendar import DateEntry

class MenuVista:

    def __init__(self, window, data):
        self.window=window
        self.usuarioControlador=UsuarioControlador
        self.mainView(data)

    def mainView(self, data):
        if isinstance(data, tuple):
            rol=data[3]
        else:
            self.limpiar_pantalla_window()
            rol = data
        options = ["Configurar usuarios", "Configurar socios", "Configurar vehiculos",
                    "Configurar clientes", "Configurar carreras"]
        Label(self.window, text=f"Bienvenido {data}").grid(row=0, column=0, columnspan=2, padx=50, pady=(25, 25))
        
        Label(self.window, text=options[0]).grid(row=1, column=0, padx=50, pady=(0, 10))
        ttk.Button(self.window, text="Usuarios", command = lambda : self.config_usuarios_interfaz(rol)).grid(row=1, column=1, padx=50, pady=(0, 10))
        
        Label(self.window, text=options[1]).grid(row=2, column=0, padx=50, pady=(0, 10))
        ttk.Button(self.window, text="Socios", command = lambda : self.config_socios_interfaz(rol)).grid(row=2, column=1, padx=50, pady=(0, 10))
        
        Label(self.window, text=options[2]).grid(row=3, column=0, padx=50, pady=(0, 10))
        ttk.Button(self.window, text="Vehiculos", command = lambda : self.config_vehiculos_interfaz(rol)).grid(row=3, column=1, padx=50, pady=(0, 10))
        
        Label(self.window, text=options[3]).grid(row=4, column=0, padx=50, pady=(0, 10))
        ttk.Button(self.window, text="Clientes", command = lambda:  self.config_clientes_interfaz(rol)).grid(row=4, column=1, padx=50, pady=(0, 10))
        
        Label(self.window, text=options[4]).grid(row=5, column=0, padx=50, pady=(0, 10))
        ttk.Button(self.window, text="Carreras", command = lambda : self.config_carreras_interfaz(rol)).grid(row=5, column=1, padx=50, pady=(0, 10))

    def limpiar_pantalla_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def cerrar_toplevel(self, toplevel):
        toplevel.grab_release()
        # eliminar
        toplevel.destroy()
    
    def set_column_width(self, treeview, column_index, width):
        treeview.column(column_index, width=width, minwidth=width, stretch= NO, anchor="center")
    
    def llenar_fila_prueba(self, treeview, valores = (), texto = "1"):
        treeview.insert('', 'end', text=texto, values=valores)
    
    def ajustar_ancho_columnas(self, treeview):
        for column in treeview["columns"]:
            column_width = max(
                font.Font().measure(treeview.set(child, column)) for child in treeview.get_children('')
                )
            self.set_column_width(treeview, column, column_width + 20)
    
    def validar_numerico(self, text, limit):
        if text.isdigit() and len(text) <= int(limit):
            return True
        elif text == "":
            return True
        else:
            return False
    
    def validar_limite(self, text, limite):
        if len(text) < int(limite):
            return True
        else:
            return False
    
    def config_usuarios_interfaz(self, data_rol : int):
        # limpiar pantalla
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, text="Modulo de usuarios").grid(row=0, column=0, columnspan=2)
        # Tabla
        self.table_users = ttk.Treeview(self.window, height=10)
        self.table_users.grid(row=1, column=0, rowspan=3)
        self.table_users["columns"]=("c0", "c1", "c2")
        # cabeceras de las columnas
        self.table_users.heading(column="c0", text="Data 1")
        self.table_users.heading(column="c1", text="Data 2")
        self.table_users.heading(column="c2", text="ROL")
        # llenar columna !!
        self.llenar_fila_prueba(self.table_users, ("Juanito1", "12345", "1"))
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_users)
        self.table_users.column("#0", width=35, minwidth=35, stretch=NO)
        # buttons
        ttk.Button(self.window, text="Crear usuario", command = self.generar_data_usuarios, state="normal" if data_rol == 1 or data_rol == 2 else "disabled").grid(row=1, column=1) #Toplevel
        ttk.Button(self.window, text="Eliminar usuario", state="normal" if data_rol == 1 or data_rol == 2 else "disabled").grid(row=2, column=1)
        ttk.Button(self.window, text="Editar usuario", command = self.editar_data_usuarios, state="normal" if data_rol == 1 or data_rol == 2 else "disabled").grid(row=3, column=1)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView(data_rol)).grid(row=4, column=0, columnspan=2)
    
    def config_socios_interfaz(self, data_rol):
        # limpiar pantalla
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, text="Modulo de socios").grid(row=0, column=0, columnspan=3)
        # Tabla
        self.table_socios = ttk.Treeview(self.window, height=10)
        self.table_socios.grid(row=1, column=0, columnspan=3)
        self.table_socios["columns"]=("c0", "c1", "c2", "c3", "c4", "c5")
        self.table_socios.heading(column="c0", text="Data 1")
        self.table_socios.heading(column="c1", text="Data 2")
        self.table_socios.heading(column="c2", text="Data 3")
        self.table_socios.heading(column="c3", text="Data 4")
        self.table_socios.heading(column="c4", text="Data 5")
        self.table_socios.heading(column="c5", text="Data 6")
        # llenar columna !!
        self.llenar_fila_prueba(self.table_socios, ("Juanito1", "12345", "Pedrito 75", "Juarez", "Pizza", "2222"))
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_socios)
        self.table_socios.column("#0", width=35, minwidth=35, stretch=NO)
        # buttons
        ttk.Button(self.window, text="Crear socios", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.generar_data_socios).grid(row=2, column=0) #Toplevel
        ttk.Button(self.window, text="Eliminar socios", state="normal" if data_rol == 1 or data_rol == 2 else "disabled").grid(row=2, column=1)
        ttk.Button(self.window, text="Editar socios", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.editar_data_socios).grid(row=2, column=2)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView(data_rol)).grid(row=3, column=0, columnspan=3)
    
    def config_vehiculos_interfaz(self, data_rol):
        # limpiar pantalla
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, text="Modulo de vehiculos").grid(row=0, column=0, columnspan=3)
        # Tabla
        self.table_vehiculos = ttk.Treeview(self.window, height=10)
        self.table_vehiculos.grid(row=1, column=0, columnspan=3)
        self.table_vehiculos["columns"]=("c0", "c1", "c2", "c3", "c4", "c5")
        self.table_vehiculos.heading(column="c0", text="Data 1")
        self.table_vehiculos.heading(column="c1", text="Data 2")
        self.table_vehiculos.heading(column="c2", text="Data 3")
        self.table_vehiculos.heading(column="c3", text="Data 4")
        self.table_vehiculos.heading(column="c4", text="Data 5")
        self.table_vehiculos.heading(column="c5", text="Data 6")
        # llenar columna !!
        self.llenar_fila_prueba(self.table_vehiculos, ("Juanito1", "12345", "Pedrito 75", "Juarez", "Pizza", "2222"))
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_vehiculos)
        self.table_vehiculos.column("#0", width=35, minwidth=35, stretch=NO)
        # buttons
        ttk.Button(self.window, text="Crear vehiculos", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.generar_data_vehiculos).grid(row=2, column=0) #Toplevel
        ttk.Button(self.window, text="Eliminar vehiculos", state="normal" if data_rol == 1 or data_rol == 2 else "disabled").grid(row=2, column=1)
        ttk.Button(self.window, text="Editar vehiculos", state="normal" if data_rol == 1 or data_rol == 2 else "disabled", command = self.editar_data_vehiculos).grid(row=2, column=2)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView(data_rol)).grid(row=3, column=0, columnspan=3)
    
    def config_clientes_interfaz(self, data_rol):
        # limpiar pantalla
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, text="Modulo de clientes").grid(row=0, column=0, columnspan=3)
        # Tabla
        self.table_clientes = ttk.Treeview(self.window, height=10)
        self.table_clientes.grid(row=1, column=0, columnspan=3)
        self.table_clientes["columns"]=("c0", "c1", "c2", "c3", "c4", "c5", "c6")
        self.table_clientes.heading(column="c0", text="Data 1")
        self.table_clientes.heading(column="c1", text="Data 2")
        self.table_clientes.heading(column="c2", text="Data 3")
        self.table_clientes.heading(column="c3", text="Data 4")
        self.table_clientes.heading(column="c4", text="Data 5")
        self.table_clientes.heading(column="c5", text="Data 6")
        self.table_clientes.heading(column="c6", text="Data 7")
        # llenar columna !!
        self.llenar_fila_prueba(self.table_clientes, ("Juanito1", "12345", "Pedrito 75", "Juarez", "Pizza", "2222", "El xocas"))
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_clientes)
        self.table_clientes.column("#0", width=35, minwidth=35, stretch=NO)
        # buttons
        ttk.Button(self.window, text="Crear clientes", state="normal", command = self.generar_data_clientes).grid(row=2, column=0) #Toplevel
        ttk.Button(self.window, text="Eliminar clientes", state="normal").grid(row=2, column=1)
        ttk.Button(self.window, text="Editar clientes", state="normal", command = self.editar_data_clientes).grid(row=2, column=2)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView(data_rol)).grid(row=3, column=0, columnspan=3)
    
    def config_carreras_interfaz(self, data_rol):
        # limpiar pantalla
        self.limpiar_pantalla_window()
        # widgets
        Label(self.window, text="Modulo de carreras").grid(row=0, column=0, columnspan=2)
        # Tabla
        self.table_carreras = ttk.Treeview(self.window, height=10)
        self.table_carreras.grid(row=1, column=0, rowspan=3)
        self.table_carreras["columns"]=("c0", "c1", "c2", "c3", "c4")
        self.table_carreras.heading(column="#0", text="ID")
        self.table_carreras.heading(column="c0", text="Data 1")
        self.table_carreras.heading(column="c1", text="Data 2")
        self.table_carreras.heading(column="c2", text="Data 3")
        self.table_carreras.heading(column="c3", text="Data 4")
        self.table_carreras.heading(column="c4", text="Data 5")
        # llenar columna !!
        self.llenar_fila_prueba(self.table_carreras, ("Juanito1", "12345", "Pedrito 75", "Juarez", "Pizza"))
        # ajustar width de columnas
        self.ajustar_ancho_columnas(self.table_carreras)
        # ajustando columna principal
        self.table_carreras.column("#0", width=35, minwidth=35, stretch=NO, anchor="w")
        # buttons
        ttk.Button(self.window, text="Crear carreras", state="normal", command = self.generar_data_carreras).grid(row=1, column=1) #Toplevel
        ttk.Button(self.window, text="Eliminar carreras", state="normal").grid(row=2, column=1)
        ttk.Button(self.window, text="Editar carreras", state="normal", command = self.editar_data_carreras).grid(row=3, column=1)
        # volver
        ttk.Button(self.window, text="Volver", command= lambda : self.mainView(data_rol)).grid(row=4, column=0, columnspan=2)
    
    def generar_data_usuarios(self):
        # generar toplevel
        self.toplevel_usuarios_add = Toplevel(self.window)
        self.toplevel_usuarios_add.title("Agregar usuarios toplevel")
        # focus al toplevel
        self.toplevel_usuarios_add.grab_set()
        # Labels
        Label(self.toplevel_usuarios_add, text="Formulario para agregar usuarios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
        # validacion
        validacion_limite = self.toplevel_usuarios_add.register(self.validar_limite)
        Label(self.toplevel_usuarios_add, text="Usuario").grid(row=1, column=0, padx=40, pady=5)
        user = ttk.Entry(self.toplevel_usuarios_add, validate="key", validatecommand=(validacion_limite, '%P', 20))
        user.grid(row=1, column=1, padx=40, pady=5)
        
        Label(self.toplevel_usuarios_add, text="Contraseña").grid(row=2, column=0, padx=40, pady=5)
        password = ttk.Entry(self.toplevel_usuarios_add, validate="key", validatecommand=(validacion_limite, '%P', 20))
        password.grid(row=2, column=1, padx=40, pady=5)
        
        ttk.Button(self.toplevel_usuarios_add, text="Agregar").grid(row=3, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_usuarios_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_usuarios_add)).grid(row=3, column=1, padx=40, pady=(10, 25))
    
    def editar_data_usuarios(self):
        # pedir seleccion de tablas
        
        data_old = ("test1", "test2")
        # generar toplevel
        self.toplevel_usuarios_add = Toplevel(self.window)
        self.toplevel_usuarios_add.title("Editar usuarios toplevel")
        # focus al toplevel
        self.toplevel_usuarios_add.grab_set()
        # Labels
        Label(self.toplevel_usuarios_add, text="Formulario para editar usuarios").grid(row=0, column=0, columnspan=2, padx=40, pady=(25, 10))
        # validacion
        validacion_limite = self.toplevel_usuarios_add.register(self.validar_limite)
        Label(self.toplevel_usuarios_add, text="Usuario").grid(row=1, column=0, padx=40, pady=5)
        user = ttk.Entry(self.toplevel_usuarios_add, validate="key", validatecommand=(validacion_limite, '%P', 20))
        user.grid(row=1, column=1, padx=40, pady=5)
        Label(self.toplevel_usuarios_add, text=data_old[0], relief="sunken").grid(row=2, column=1, padx=40, pady=5)
        Label(self.toplevel_usuarios_add, text="Data seleccionada = ").grid(row=2, column=0, padx=40, pady=5)
        
        Label(self.toplevel_usuarios_add, text="Contraseña").grid(row=3, column=0, padx=40, pady=5)
        password = ttk.Entry(self.toplevel_usuarios_add, validate="key", validatecommand=(validacion_limite, '%P', 20))
        password.grid(row=3, column=1, padx=40, pady=5)
        Label(self.toplevel_usuarios_add, text="Data seleccionada = ").grid(row=4, column=0, padx = 40, pady = 5)
        Label(self.toplevel_usuarios_add, text=data_old[1], relief="sunken").grid(row=4, column=1, padx=40, pady=5)
        
        ttk.Button(self.toplevel_usuarios_add, text="Agregar").grid(row=5, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_usuarios_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_usuarios_add)).grid(row=5, column=1, padx=40, pady=(10, 25))
    
    def generar_data_socios(self):
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
        nombre = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        nombre.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="Apellido").grid(row=2, column=0, padx = 40, pady = 5)
        apellido = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        apellido.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="cedula").grid(row=3, column=0, padx = 40, pady = 5)
        ci = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        ci.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="telefono").grid(row=4, column=0, padx = 40, pady = 5)
        tlf = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        tlf.grid(row=4, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="Fecha ingreso").grid(row=5, column=0, padx = 40, pady = 5)
        fecha = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 10))
        fecha.grid(row=5, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="Status").grid(row=6, column=0, padx = 40, pady = 5)
        lista_status = ["1", "0"]
        status_combo = ttk.Combobox(self.toplevel_socios_add, values=lista_status)
        status_combo.set(lista_status[0])
        status_combo.grid(row=6, column=1)
        
        ttk.Button(self.toplevel_socios_add, text="Agregar").grid(row=7, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_socios_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_socios_add)).grid(row=7, column=1, padx=40, pady=(10, 25))
    
    def editar_data_socios(self):
        # pedir seleccion de tablas
        
        data_old = ("test1", "test2")
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
        nombre = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        nombre.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="Apellido").grid(row=2, column=0, padx = 40, pady = 5)
        apellido = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        apellido.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="cedula").grid(row=3, column=0, padx = 40, pady = 5)
        ci = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        ci.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="telefono").grid(row=4, column=0, padx = 40, pady = 5)
        tlf = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        tlf.grid(row=4, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="Fecha ingreso").grid(row=5, column=0, padx = 40, pady = 5)
        fecha = ttk.Entry(self.toplevel_socios_add, validate="key", validatecommand=(validacion_limite, "%P", 10))
        fecha.grid(row=5, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_socios_add, text="Status").grid(row=6, column=0, padx = 40, pady = 5)
        lista_status = ["1", "0"]
        status_combo = ttk.Combobox(self.toplevel_socios_add, values=lista_status)
        status_combo.set(lista_status[0])
        status_combo.grid(row=6, column=1)
        
        ttk.Button(self.toplevel_socios_add, text="Actualizar").grid(row=7, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_socios_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_socios_add)).grid(row=7, column=1, padx=40, pady=(10, 25))
    
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
        marca = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 20))
        marca.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Modelo").grid(row=2, column=0, padx = 40, pady = 5)
        modelo = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 20))
        modelo.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Año").grid(row=3, column=0, padx = 40, pady = 5)
        year = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_numerica, "%P", 4))
        year.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Placa").grid(row=4, column=0, padx = 40, pady = 5)
        placa = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 15))
        placa.grid(row=4, column=1, padx = 40, pady = 5)
        # llenar lista idsocio con los socios disponibles
        
        Label(self.toplevel_vehiculos_add, text="ID Socio").grid(row=6, column=0, padx = 40, pady = 5)
        idSocio_combo_status = ["Seleccionar..."]
        idSocio_combo = ttk.Combobox(self.toplevel_vehiculos_add, values=idSocio_combo_status)
        idSocio_combo.set(idSocio_combo_status[0])
        idSocio_combo.grid(row=6, column=1)
        
        Label(self.toplevel_vehiculos_add, text="Disponible").grid(row=6, column=0, padx = 40, pady = 5)
        lista_status = ["1", "0"]
        status_combo = ttk.Combobox(self.toplevel_vehiculos_add, values=lista_status)
        status_combo.set(lista_status[1])
        status_combo.grid(row=7, column=1)
        
        ttk.Button(self.toplevel_vehiculos_add, text="Agregar").grid(row=8, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_vehiculos_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_vehiculos_add)).grid(row=8, column=1, padx=40, pady=(10, 25))
    
    def editar_data_vehiculos(self):
        # pedir seleccion de tablas
        
        data_old = ("test1", "test2")
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
        marca = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 20))
        marca.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Modelo").grid(row=2, column=0, padx = 40, pady = 5)
        modelo = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 20))
        modelo.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Año").grid(row=3, column=0, padx = 40, pady = 5)
        year = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_numerica, "%P", 4))
        year.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_vehiculos_add, text="Placa").grid(row=4, column=0, padx = 40, pady = 5)
        placa = ttk.Entry(self.toplevel_vehiculos_add, validate="key", validatecommand=(validacion_limite, "%P", 15))
        placa.grid(row=4, column=1, padx = 40, pady = 5)
        # llenar lista idsocio con los socios disponibles
        
        Label(self.toplevel_vehiculos_add, text="ID Socio").grid(row=6, column=0, padx = 40, pady = 5)
        idSocio_combo_status = ["Seleccionar..."]
        idSocio_combo = ttk.Combobox(self.toplevel_vehiculos_add, values=idSocio_combo_status)
        idSocio_combo.set(idSocio_combo_status[0])
        idSocio_combo.grid(row=6, column=1)
        
        Label(self.toplevel_vehiculos_add, text="Disponible").grid(row=6, column=0, padx = 40, pady = 5)
        # llenar data de listas de id socio
        lista_status = ["1", "0"]
        status_combo = ttk.Combobox(self.toplevel_vehiculos_add, values=lista_status)
        status_combo.set(lista_status[1])
        status_combo.grid(row=7, column=1)
        
        ttk.Button(self.toplevel_vehiculos_add, text="Actualizar").grid(row=8, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_vehiculos_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_vehiculos_add)).grid(row=8, column=1, padx=40, pady=(10, 25))
    
    def generar_data_clientes(self):
        # generar toplevel
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
        nombre = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        nombre.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Apellido").grid(row=2, column=0, padx = 40, pady = 5)
        apellido= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        apellido.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Telefono 1").grid(row=3, column=0, padx = 40, pady = 5)
        telefono1 = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        telefono1.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Telefono 2").grid(row=4, column=0, padx = 40, pady = 5)
        telefono2 = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        telefono2.grid(row=4, column=1, padx = 40, pady = 5)
        # llenar lista idsocio con los socios disponibles
        
        Label(self.toplevel_clientes_add, text="Direccion").grid(row=5, column=0, padx = 40, pady = 5)
        dirc= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 50))
        dirc.grid(row=5, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Fecha ingreso").grid(row=6, column=0, padx = 40, pady = 5)
        fecha= DateEntry(self.toplevel_clientes_add)
        fecha.grid(row=6, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Estatus").grid(row=7, column=0, padx = 40, pady = 5)
        lista_status = ["1", "0"]
        status_combo = ttk.Combobox(self.toplevel_clientes_add, values=lista_status)
        status_combo.set(lista_status[1])
        status_combo.grid(row=7, column=1)
        
        ttk.Button(self.toplevel_clientes_add, text="Actualizar").grid(row=8, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_clientes_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_clientes_add)).grid(row=8, column=1, padx=40, pady=(10, 25))
    
    def editar_data_clientes(self):
        # pedir seleccion de tablas
        
        data_old = ("test1", "test2")
        # generar toplevel
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
        nombre = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        nombre.grid(row=1, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Apellido").grid(row=2, column=0, padx = 40, pady = 5)
        apellido= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 40))
        apellido.grid(row=2, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Telefono 1").grid(row=3, column=0, padx = 40, pady = 5)
        telefono1 = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        telefono1.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Telefono 2").grid(row=4, column=0, padx = 40, pady = 5)
        telefono2 = ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_numerica, "%P", 12))
        telefono2.grid(row=4, column=1, padx = 40, pady = 5)
        # llenar lista idsocio con los socios disponibles
        
        Label(self.toplevel_clientes_add, text="Direccion").grid(row=5, column=0, padx = 40, pady = 5)
        dirc= ttk.Entry(self.toplevel_clientes_add, validate="key", validatecommand=(validacion_limite, "%P", 50))
        dirc.grid(row=5, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Fecha ingreso").grid(row=6, column=0, padx = 40, pady = 5)
        fecha= DateEntry(self.toplevel_clientes_add)
        fecha.grid(row=6, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_clientes_add, text="Estatus").grid(row=7, column=0, padx = 40, pady = 5)
        lista_status = ["1", "0"]
        status_combo = ttk.Combobox(self.toplevel_clientes_add, values=lista_status)
        status_combo.set(lista_status[1])
        status_combo.grid(row=7, column=1)
        
        ttk.Button(self.toplevel_clientes_add, text="Actualizar").grid(row=8, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_clientes_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_clientes_add)).grid(row=8, column=1, padx=40, pady=(10, 25))
    
    def generar_data_carreras(self):
        # generar toplevel
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
        lista_idCarro = ["Seleccionar..."]
        # agregar id's al lista ids
        carro_combo = ttk.Combobox(self.toplevel_carreras_add, values=lista_idCarro)
        carro_combo.set(lista_idCarro[0])
        carro_combo.grid(row=1, column=1)
        
        Label(self.toplevel_carreras_add, text="ID de cliente").grid(row=2, column=0, padx = 40, pady = 5)
        lista_idCliente = ["Seleccionar..."]
        # agregar id's al lista ids
        cliente_combo = ttk.Combobox(self.toplevel_carreras_add, values=lista_idCliente)
        cliente_combo.set(lista_idCliente[0])
        cliente_combo.grid(row=2, column=1)
        
        Label(self.toplevel_carreras_add, text="Fecha de la carrera").grid(row=3, column=0, padx = 40, pady = 5)
        fecha = DateEntry(self.toplevel_carreras_add)
        fecha.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_carreras_add, text="Costo de la carrera").grid(row=4, column=0, padx = 40, pady = 5)
        cost_c = ttk.Entry(self.toplevel_carreras_add, validate="key", validatecommand=(validacion_numerica, '%P', 9))
        cost_c.grid(row=4, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_carreras_add, text="Destino de la carrera").grid(row=5, column=0, padx = 40, pady = 5)
        dir_c = ttk.Entry(self.toplevel_carreras_add, validate="key", validatecommand=(validacion_limite, '%P', 50))
        dir_c.grid(row=5, column=1, padx = 40, pady = 5)
        
        ttk.Button(self.toplevel_carreras_add, text="Agregar").grid(row=6, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_carreras_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_carreras_add)).grid(row=6, column=1, padx=40, pady=(10, 25))
    
    def editar_data_carreras(self):
        # pedir seleccion de tablas
        
        data_old = ("test1", "test2")
        # generar toplevel
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
        lista_idCarro = ["Seleccionar..."]
        # agregar id's al lista ids
        carro_combo = ttk.Combobox(self.toplevel_carreras_add, values=lista_idCarro)
        carro_combo.set(lista_idCarro[0])
        carro_combo.grid(row=1, column=1)
        
        Label(self.toplevel_carreras_add, text="ID de cliente").grid(row=2, column=0, padx = 40, pady = 5)
        lista_idCliente = ["Seleccionar..."]
        # agregar id's al lista ids
        cliente_combo = ttk.Combobox(self.toplevel_carreras_add, values=lista_idCliente)
        cliente_combo.set(lista_idCliente[0])
        cliente_combo.grid(row=2, column=1)
        
        Label(self.toplevel_carreras_add, text="Fecha de la carrera").grid(row=3, column=0, padx = 40, pady = 5)
        fecha = DateEntry(self.toplevel_carreras_add)
        fecha.grid(row=3, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_carreras_add, text="Costo de la carrera").grid(row=4, column=0, padx = 40, pady = 5)
        cost_c = ttk.Entry(self.toplevel_carreras_add, validate="key", validatecommand=(validacion_numerica, '%P', 9))
        cost_c.grid(row=4, column=1, padx = 40, pady = 5)
        
        Label(self.toplevel_carreras_add, text="Destino de la carrera").grid(row=5, column=0, padx = 40, pady = 5)
        dir_c = ttk.Entry(self.toplevel_carreras_add, validate="key", validatecommand=(validacion_limite, '%P', 50))
        dir_c.grid(row=5, column=1, padx = 40, pady = 5)
        
        ttk.Button(self.toplevel_carreras_add, text="Actualizar").grid(row=6, column=0, padx=40, pady=(10, 25))
        ttk.Button(self.toplevel_carreras_add, text="Volver", command= lambda : self.cerrar_toplevel(self.toplevel_carreras_add)).grid(row=6, column=1, padx=40, pady=(10, 25))