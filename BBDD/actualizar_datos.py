import pymysql

#EJEMPLO DE ACTUALIZAR UN CAMPO EN BASE A UN CRITERIO
#Nota: podríamos actualizar más campos a la vez y utilizar más de un criterio en la consulta

def actualizar_campo_tabla(db,tabla,valor,campo_actualizar,campo,criterio):

    try:
        cursor = db.cursor()
        #Ojo, cuidado con el valor, tiene que corresponder al tipo de dato que se quiera actualizar
        #Ejemplo: el valor del DNI tiene que ir entre comillas.
        consulta = "UPDATE " + tabla + " SET " + campo_actualizar + " = '" + valor + "' WHERE " + campo + '=' + criterio
        print(consulta)
        # Ejecutar SQL --> es un string
        cursor.execute(consulta)
        db.commit()
        print('Registro actualizado correctamente')
    except:
        print('Error en la consulta o en la conexión')
        db.rollback() #Deshacer cambios
    finally:
        db.close()
####################################################################################################
if __name__ == "__main__":

    #PARÁMETROS DE NUESTRA BASE DE DATOS
    host='127.0.0.1'
    usuario='root'
    base_datos='testsge'
    password='12345Abcde'
    puerto=3306

    #CONEXIÓN -> Si tenemos un programa principal, sólo habría que realizar la conexión al principio y desconectar al final
                 # Salvo que queramos hacer lo contrario

    db = pymysql.connect(host=host,user=usuario,password=password,db=base_datos,port=puerto)

    #TABLA
    tabla='EMPLEADOS'

    #DATOS
    campo='ID_EMPLEADO'
    criterio='6' #Aunque sea numérico, tiene que ser string ya que después la consulta generada es String
    campo_actualizar = 'DNI'
    valor_actualizar = '00000000A' #Este valor ya de por sí es String, pero en la consulta habrá que añadirle las comillas

    # LLAMADA A LA FUNCIÓN QUE ACTUALIZA LA TABLA CON EL NUEVO DATO
    actualizar_campo_tabla(db,tabla,valor_actualizar,campo_actualizar,campo,criterio)