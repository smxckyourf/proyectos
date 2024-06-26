# pip install mysql-connector-python
import mysql.connector 

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                host = "127.0.0.1",
                user = "root",
                password = "joacod2018",
                database = "pythonDb2",
                port="3306"
            )
            print("Conexion exitosa")

            return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error))
            
            return conexion
        
    ConexionBaseDeDatos()