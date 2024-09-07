from tkinter import *
from tkinter import ttk, messagebox
from controllers.Mensaje import *
from views.Gestor import *
from views.centrar_ventana import *

############################################## INVOCAR LOS MÉTODOS BD
def conexionBBDD():
    Gestor.conexionBBDD()

def eliminarBBDD():
    Gestor.eliminarBBDD()
    limpiarMostrar()

def limpiarMostrar():
    limpiarCampos()
    mostrar()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")

def mostrar():
    Gestor.mostrar(tree)

def salirAplicación():
    valor = messagebox.askquestion("Salir", Mensaje.SALIR)
    root.destroy if valor == "yes" else None

############################################## INVOCAR LOS MÉTODOS CRUD

def crear():
    Gestor.crear(miNombre.get(), miCargo.get(), miSalario.get())
    limpiarMostrar()

def actualizar():
    Gestor.actualizar(miNombre.get(), miCargo.get(), miSalario.get(), miId.get())
    limpiarMostrar()

def borrar():
    Gestor.borrar(miId.get())
    limpiarMostrar()

def buscar():
    Gestor.buscar(tree, miNombre.get())

def seleccionarHaciendoClick(event):
    item = tree.identify("item", event.x, event.y)
    miId.set(tree.item(item,"text"))
    miNombre.set(tree.item(item,"values")[0])
    miCargo.set(tree.item(item,"values")[1])
    miSalario.set(tree.item(item,"values")[2])

root = Tk()
root.title("Gestor de Empleados")
root.configure(background="lightblue")
root.geometry(centrar(600, 350, root))

#ICONOS
imagen_buscar = PhotoImage(file="img/buscar.png")
imagen_crear = PhotoImage(file="img/crear.png")
imagen_mostrar = PhotoImage(file="img/mostrar.png")
imagen_actualizar = PhotoImage(file="img/actualizar.png")
imagen_eliminar = PhotoImage(file="img/eliminar.png")

#VARIABLES PARA CAJAS DE TEXTO
miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()

################################# TABLA #######################################
headers = ["ID", "Nombre del Empleado", "Cargo", "Salario"]
tree = ttk.Treeview(height=10, columns=("#0", "#1", "#2"))
tree.place(x=0, y=130)
tree.column("#0", width=100)
tree.heading("#0", text=headers[0], anchor=CENTER)
tree.heading("#1", text=headers[1], anchor=CENTER)
tree.heading("#2", text=headers[2], anchor=CENTER)
tree.column("#3", width=100)
tree.heading("#3", text=headers[3], anchor=CENTER)
tree.bind("<Button-1>", seleccionarHaciendoClick)
mostrar()

################################# WIDGETS #######################################
########## MENÚES ###########
menubar = Menu(root)
menubasedat = Menu(menubar, tearoff=0)
menubasedat.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
menubasedat.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
menubasedat.add_command(label="Salir", command=salirAplicación)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu = Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=Gestor.mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)


################# ETIQUETAS Y CAJAS DE TEXTO #####################

entradaId = Entry(root, textvariable=miId)

labelNombre = Label(root, text="Nombre", background="lightblue")
labelNombre.place(x=50, y=10)
entryNombre = Entry(root, textvariable=miNombre, width=50)
entryNombre.place(x=100, y=10)

labelCargo = Label(root, text="Cargo", background="lightblue")
labelCargo.place(x=50, y=40)
entryCargo = Entry(root, textvariable=miCargo, width=50)
entryCargo.place(x=100, y=40)

labelSalario = Label(root, text="Salario", background="lightblue")
labelSalario.place(x=280, y=40)
entrySalario = Entry(root, textvariable=miSalario, width=10)
entrySalario.place(x=320, y=40)

labelPesos = Label(root, text="AR$", background="lightblue")
labelPesos.place(x=380, y=40)

################# BOTONES #####################

botonCrear = Button(root, text="Crear Registro",image=imagen_crear, bg="green", command=crear).place(x=50, y=85)
botonActualizar = Button(root, text="Actualizar Registro",image=imagen_actualizar, bg="orange", command=actualizar).place(x=180, y=85)
botonMostrar = Button(root, text="Mostrar Lista",image=imagen_mostrar, bg="orange",  command=mostrar).place(x=320, y=85)
botonEliminar = Button(root, text="Crear Registro",image=imagen_eliminar, bg="red", command=borrar).place(x=450, y=85)
botonBuscar = Button(root, text="Buscar Registro",image=imagen_buscar, bg="orange", command=buscar).place(x=450, y=10)

root.config(menu=menubar)
root.mainloop()
