#CONSULTA DE DATOS - 2
# Nota: es un ejemplo concreto en el que realizamos una consulta sin ningún criterio
import pymysql

####################################################################################################
#FUNCIÓN PARA DEVOLVER EL NOMBRE DE LAS COLUMNAS DE UNA TABLA
def nombre_columnas(db,base_datos,tabla):
    # Preparar el cursor
    cursor = db.cursor()

    #CONSULTAS PARA SABER EL NOMBRE DE LAS COLUMNAS DE UNA TABLA
    # --> LAS DOS PRIMERAS DEVUELVEN MÁS DATOS
    #consulta = 'SHOW COLUMNS FROM ' + tabla
    #consulta = 'DESCRIBE ' + tabla

    consulta = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA ='" + base_datos + "' AND TABLE_NAME='" + tabla + "'"

    # Ejecutar SQL
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    print(resultados)
    #Como "resultados" guarda una tupla de tuplas, una alternativa es guardar los nombres en una lista
    #El nombre está en el primer elemento de cada tupla
    columnas=[]
    for columna in resultados:
        columnas.append(columna[0])

    #Alternativa para crear una lista utilizando un bucle en una misma línea
    columnas2=[columnas[0] for columnas in resultados]

    return columnas2

####################################################################################################

#CONSULTA GENÉRICA PARA CUALQUIER TABLA
def mostrar_datos_tabla(db, base_datos, tabla):

    try:
        #Nombre de las columnas
        columnas = nombre_columnas(db,base_datos,tabla)
        # Preparar el cursor
        cursor = db.cursor()
        consulta = 'SELECT * FROM ' + tabla

        # Ejecutar SQL --> es un string
        cursor.execute(consulta)

        # Recoger más de un dato con fetchall()
        # Resultados es una tupla de tuplas --> Guarda una tupla por cada registro de la tabla
        resultados = cursor.fetchall()

        #En este caso, sabemos que la tabla tiene
        print('RESULTADO DE LA CONSULTA\n++++++++++++++++++++++++')
        for registro in resultados:
            for i in range(0,len(columnas)):
                print(columnas[i],':', registro[i])
            print('-----------')

        db.commit()

    except:
        print('Error en la consulta')
        #db.rollback() #En principio no sería necesario, ya que no hacemos cambios en las tablas

####################################################################################################
#PARÁMETROS DE NUESTRA BASE DE DATOS

host='127.0.0.1'
usuario='root'
password='12345Abcde'
base_datos='testsge'
puerto=3306

#CONEXIÓN
db = pymysql.connect(host=host,user=usuario,password=password,db=base_datos,port=puerto)

#TABLA
tabla='EMPLEADOS'

#PROBAMOS
mostrar_datos_tabla(db,base_datos,tabla)

# CERRAMOS CONEXIÓN
db.close()