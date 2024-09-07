import sqlite3
from models.Consulta import *
from models.Empleado import *


class Servicio:
    def conectar():
        miConexión = sqlite3.connect("Empleados.db")
        miCursor = miConexión.cursor()
        return miConexión, miCursor

    def conexionBBDD():
        miConexion, miCursor = Servicio.conectar()
        miCursor.execute(Consulta.CREATE)

    def eliminarBBDD():
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.DELETE_TABLE)

    #READ
    def consultar():
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.SELECT)
        return miCursor.fetchall()
    #CREATE
    def crear(nombre, cargo, salario):
        miConexion,miCursor = Servicio.conectar()
        empleado = Empleado(nombre, cargo, salario)
        miCursor.execute(Consulta.INSERT,(empleado.getEmpleado()))
        miConexion.commit()
    #UPDATE
    def actualizar(nombre, cargo, salario, id):
        miConexion,miCursor = Servicio.conectar()
        empleado = Empleado(nombre, cargo, salario)
        miCursor.execute(Consulta.UPDATE+id,(empleado.getEmpleado()))
        miConexion.commit()
    #DELETE
    def borrarRegistro(id):
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.DELETE+id)
        miConexion.commit()
    #BUSCAR
    def buscar(nombre):
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.BUSCAR,(nombre,))
        return miCursor.fetchall()