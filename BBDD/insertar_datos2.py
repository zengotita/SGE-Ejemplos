import pymysql

#INSERTAR DATOS

def insertar_datos_generica(db,tabla,columnas,valores):

    try:
        cursor = db.cursor()

        consulta = "INSERT INTO " + tabla + "("+ columnas +") VALUES (" + valores + ")"
        print(consulta)

        # Ejecutar SQL --> es un string
        cursor.execute(consulta)
        db.commit()
        print('Registro insertado correctamente')

    except:
        print('Error en la consulta o en la conexión')
        db.rollback() #Deshacer cambios


####################################################################################################
# PARÁMETROS DE NUESTRA BASE DE DATOS
if __name__ == "__main__":
    host = '127.0.0.1'
    usuario = 'root'
    password = '12345Abcde'
    base_datos = 'testsge'
    puerto = 3306

    # CONEXIÓN
    db = pymysql.connect(host=host, user=usuario, password=password,db=base_datos, port=puerto)

    # TABLA
    tabla = 'EMPLEADOS'

    # COLUMNAS: habría que obtenerlas de otra manera, por ejemplo, a través de una función como la que está definida en "consultar_datos2"
    # -----> String
    # VALORES: habría que obtenerlos a través de la interacción del usuario -> pidiéndole dichos valores
    # -----> String y entre comillas si el tipo de dato es VARCHAR

    columnas = "ID_EMPLEADO,NOMBRE,APELLIDO,DNI"
    valores = "1,'NombreEmpleado1','ApellidoEmpleado1','11111111T'"

    # LLAMAMOS A LA FUNCIÓN
    insertar_datos_generica(db, tabla, columnas, valores)