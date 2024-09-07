class Consulta:
        #Sentencias SQL en formato string
        #Se hacen las consultas en variables para luego invocarlas en los controllers y que la misma estructura no sea visible
        CREATE ='''
                CREATE TABLE empleados(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50) NOT NULL,
                CARGO VARCHAR(50) NOT NULL,
                SALARIO INT NOT NULL)
                '''

        DELETE_TABLE = "DROP TABLE empleados"

        INSERT = "INSERT INTO empleados VALUES(NULL,?,?,?)"

        SELECT = "SELECT * FROM empleados"

        UPDATE = "UPDATE empleados SET NOMBRE=?,CARGO=?,SALARIO=? WHERE ID="

        DELETE = "DELETE FROM empleados WHERE ID="

        BUSCAR = "SELECT * FROM empleados WHERE NOMBRE LIKE '%' || ? || '%'"

