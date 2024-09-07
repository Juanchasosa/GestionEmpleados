from tkinter import messagebox
from controllers.Servicio import *
from controllers.Mensaje import *


class Gestor:
    #Gestionar servicios de conexión
    def conexionBBDD():
        try:
            Servicio.conexionBBDD()
            messagebox.showinfo("CONEXIÓN",Mensaje.EXITO_BD)
        except:
            messagebox.showinfo("CONEXIÓN",Mensaje.ERROR_BD)

    def eliminarBBDD():
        if messagebox.askyesno(message=Mensaje.CONFIRMAR_BD, title="ADVERTENCIA"):
            Servicio.eliminarBBDD()
        else:
            messagebox.showinfo("CONEXIÓN",Mensaje.ERROR_ELIMINAR_BD)

    #GESTIONAR SERVICIOS DE CRUD EMPLEADOS

    def mostrar(tree):
        registros = tree.get_children()
        [tree.delete(elemento) for elemento in registros]
        try:
            empleados = Servicio.consultar()
            [tree.insert("",0,text=empleado[0],values=(empleado[1],empleado[2],empleado[3]))for empleado in empleados]
        except:
            messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_MOSTRAR)

    def buscar(tree, criterio):
        registros = tree.get_children()
        [tree.delete(elemento) for elemento in registros]
        try:
            if len(criterio) == 0:
                messagebox.showwarning("ADVERTENCIA", Mensaje.NOMBRE_FALTANTE)
            else:
                empleados = Servicio.buscar(criterio)
                [tree.insert("",0,text=empleado[0],values=(empleado[1],empleado[2],empleado[3]))for empleado in empleados]
        except:
            messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_BUSCAR)

    def crear(nombre, cargo, salario):
        try:
            if len(nombre) == 0 and len(cargo) == 0 and len(salario) == 0 :
                messagebox.showwarning("ADVERTENCIA", Mensaje.CAMPOS_FALTANTES)
            else:
                Servicio.crear(nombre, cargo, salario)
        except:
            messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_CREAR)

    def actualizar(nombre, cargo, salario, id):
        try:
            if nombre !="" and cargo !="" and salario !="":
                Servicio.actualizar(nombre, cargo, salario,id)
            else:
                messagebox.showwarning("ADVERTENCIA", Mensaje.CAMPOS_FALTANTES)
        except:
            messagebox.showwarning("ADVERTENCIA",Mensaje.ERROR_ACTUALIZAR)

    def borrar(id):
        try:
            if messagebox.askyesno(message=Mensaje.CONFIRMAR, title="ADVERTENCIA"):
                Servicio.borrarRegistro(id)
            else:
                messagebox.showwarning("CONEXIÓN",Mensaje.MSJ_ELIMINAR)
        except:
                messagebox.showwarning("CONEXIÓN",Mensaje.ERROR_ELIMINAR)

    def mensaje():
        messagebox.showinfo(title="INFORMACIÓN",message=Mensaje.ACERCA)
