import pymysql

#Ejemplo de una consulta utilizando un solo criterio. Se podrían utilizar más con "WHERE cond1=... AND cond2=... AND ..."

def mostrar_datos_criterio(db, tabla, campo, criterio):
    # Preparar el cursor
    cursor = db.cursor()
    consulta = 'SELECT * FROM ' + tabla + ' WHERE ' + campo + '=' + criterio
    print(consulta)
    # Ejecutar SQL --> es un string
    cursor.execute(consulta)
    # Recoger más de un dato con fetchall()
    resultados = cursor.fetchall()
    if (len(resultados)>0):
        for registro in resultados:
            print('- ID de empleado: ', registro[0])
            print('- Nombre de empleado: ', registro[1])
            print('- Apellido de empleado:', registro[2])
            print('- DNI de empleado:', registro[3])
    else:
        print("No se han encontrado resultados")

####################################################################################
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
campo='ID_EMPLEADO'
criterio = input("Introduce un ID de empleado --> ") # Será por ejemplo '5' Aunque sea un campo numérico, la consulta será un string

mostrar_datos_criterio(db,tabla,campo,criterio)

# CERRAMOS CONEXIÓN
db.close()