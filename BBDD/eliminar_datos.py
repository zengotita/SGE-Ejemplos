import pymysql

#ELIMINAR REGISTRO
#Nota: es un ejemplo y no tiene controlada la condición de que no exista el registro a eliminar
def eliminar_datos_tabla(db,tabla,campo,criterio):
    try:
        cursor = db.cursor()
        consulta = 'DELETE FROM ' + tabla + ' WHERE ' + campo + '=' + criterio
        # Ejecutar SQL --> es un string
        cursor.execute(consulta)
        db.commit()
        print('Registro eliminado correctamente')
    except:
        print('Error en la consulta o en la conexión')
        db.rollback() #Deshacer cambios


####################################################################################################
if __name__ == "__main__":

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

    #DATOS
    campo='ID_EMPLEADO'
    criterio='7' #Aunque sea numérico, tiene que ser string ya que después la consulta generada es String

    eliminar_datos_tabla(db,tabla,campo,criterio)