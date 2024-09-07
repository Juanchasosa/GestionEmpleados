class Empleado:
    #constructor
    #El doble guion bajo al principio significa que el atributo es privado
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario

    #Retornar el empleado
    def getEmpleado (self):
        return self.__nombre, self.__cargo, self.__salario



# empleado =Empleado("Juan", "jefe", 1000)
# print(empleado.getEmpleado())