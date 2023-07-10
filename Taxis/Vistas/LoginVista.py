from tkinter import ttk, Label, Toplevel, END, CENTER, NO
from tkinter import font
from tkinter import messagebox
from Controladores.SesionControlador import SesionControlador
from Vistas.MenuVistaMejor import MenuVista

class LoginVista:
    def __init__(self, window):
        self.Sesion=SesionControlador()
        self.window = window
        self.window.title("Linea de Taxis Dos picos")
        # self.window.geometry("320x280")
        # main login
        self.login_main_vista()

    def limpiar_pantalla_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def validar_longitud(entry):
        if len(entry.get()) > 20:
            entry.delete(20, END)

    def login_main_vista(self):
        Label(self.window, text="Inicio de sesiones").grid(row=0, column=0, padx=100, pady=(50, 0))
        # entrys
        self.usuario = ttk.Entry(self.window)
        self.usuario.grid(row=1, column=0, padx=100, pady=(15,5))
        #self.usuario.bind('<KeyRelease>', lambda event: self.validar_longitud(self.usuario))
        self.usuario.focus()

        self.contrasenia = ttk.Entry(self.window, show = "*")
        self.contrasenia.grid(row=2, column=0, padx=100, pady=(5,5))
        #self.contrasenia.bind('<KeyRelease>', lambda event: self.validar_longitud(self.contrasenia))
        # button
        ttk.Button(self.window, text="Ingresar", command=self.main_menu).grid(row=3, column=0, padx=100, pady=(25,50))

    def main_menu(self):
        if self.usuario.get()!="" and self.contrasenia.get()!="":
            respuesta=self.Sesion.validarUsuarioC(self.usuario.get(),self.contrasenia.get())
            if isinstance(respuesta, tuple):
                self.limpiar_pantalla_window()
                MenuVista(self.window, respuesta)
            else:
                messagebox.showerror(self.window,respuesta)
        else:
            messagebox.showinfo(title = "Mensaje del sistema", message ="Ningun campo puede estar vacío")