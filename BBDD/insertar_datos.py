import pymysql

def insertar_datos():
    # Conexión a base de datos
    db = pymysql.connect(host="127.0.0.1",user="root",password="12345Abcde",db="testsge",port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    # Consulta SQL para insertar datos de un empleado
    sql = """INSERT INTO EMPLEADOS(ID_EMPLEADO,
            NOMBRE, APELLIDO, DNI)
            VALUES (6, 'NombreEmpleado6',NULL,'66666666P')"""
    try:
        # Ejecutar el comando SQL
        cursor.execute(sql)
        # Aceptar cambios con commit
        db.commit()
    except:
        # Rollback en caso de haber algún error
        db.rollback()
    # Desconexión
    db.close()

insertar_datos()

