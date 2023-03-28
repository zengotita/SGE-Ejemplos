import pymysql
import mysql.connector as mysql

def crear_tabla_empleados():
    # Conexión a la base de datos
    db = pymysql.connect(host="localhost",user="root",password="12345Abcde",database="testsge")
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe --> ¡Cuidado! No se podrá eliminar si existen relaciones. Habría que ir en orden
    # --> Si la clave de esta tabla es una clave foránea de otra, hay que eliminar ese "constraint" o limitador con ALTER TABLE
    cursor.execute("DROP TABLE IF EXISTS TRABAJADORES")
    # SQL para crear tabla
    sql = """CREATE TABLE TRABAJADORES (
        NOMBRE  VARCHAR(30),
        APELLIDO VARCHAR(40),
        DNI VARCHAR(9),
        COMPRAS  INT,
        VENTAS  INT,
        RRHH  INT,
        PRODUCCION  INT)"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

crear_tabla_empleados()