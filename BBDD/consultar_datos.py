import pymysql

#CONSULTA DIRECTA CONTRA UNA TABLA (EMPLEADOS)
def mostrar_datos_empleados():

    # Establecemos conexión con la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root",password="12345Abcde", db="testsge", port=3306)
    # Preparar el cursor
    cursor = db.cursor()
    #CONSULTA
    consulta = 'SELECT * FROM EMPLEADOS'
    # Ejecutar SQL --> es un string
    cursor.execute(consulta)

    # Recoger más de un dato con fetchall()
    # Resultados es una tupla de tuplas --> Guarda una tupla por cada registro de la tabla
    resultados = cursor.fetchall()
    print(resultados)
    #En este caso, sabemos qué columnas y datos tiene la tabla en concreto
    for registro in resultados:
        print('ID de empleado: ', registro[0])
        print('Nombre de empleado: ', registro[1])
        print('Apellido de empleado:', registro[2])
        print('DNI de empleado:', registro[3])
        print('----------')

    #CERRAMOS CONEXIÓN
    db.close()

mostrar_datos_empleados()