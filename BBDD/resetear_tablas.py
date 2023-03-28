import pymysql

def conexion():

    # Conexión a la base de datos
    db = pymysql.connect(host="127.0.0.1",user="root",password="12345Abcde",db="testsge",port=3306)
    return db

def resetear_tablas():
    db = conexion()
    cursor = db.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS EMPLEADOS")
        cursor.execute("DROP TABLE IF EXISTS DEPARTAMENTOS")

        #Departamento:
        sql = """CREATE TABLE DEPARTAMENTOS (
            ID_DEPT  INT NOT NULL,
            NOMBRE  VARCHAR(20),
            PRIMARY KEY (ID_DEPT))"""
        cursor.execute(sql)

        #Empleados:
        sql = """CREATE TABLE EMPLEADOS (
            ID_EMPLEADO  INT NOT NULL,
            NOMBRE VARCHAR(20) NOT NULL,
            APELLIDO  VARCHAR(50),
            DNI VARCHAR(10) NOT NULL,
            DEPARTAMENTO INT(11) NOT NULL,
            PRIMARY KEY (ID_EMPLEADO),
            FOREIGN KEY (DEPARTAMENTO) REFERENCES DEPARTAMENTOS(ID_DEPT))"""

        cursor.execute(sql)

        db.close()
        print('Tablas reseteadas')
    except:
        print('Error BD')

resetear_tablas()
