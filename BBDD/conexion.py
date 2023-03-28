import pymysql

def test_bd():
    # Establecemos conexión con la base de datos
    db = pymysql.connect(host="127.0.0.1", user="root",password="12345Abcde", db="testsge", port=3306)
    # Preparar el cursor: es una especie de iterador para moverse entre las filas que pueda haber en un resultado de una consulta
    cursor = db.cursor()
    # Sacamos por pantalla la versión que utilizamos
    # Con .execute ejecutamos una sentencia SQL --> es un string
    cursor.execute("SELECT VERSION()")
    # Recuperar una fila usando fetchone()
    dato = cursor.fetchone()
    print("Versión de BD : %s " % dato)

#PROBAMOS QUE FUNCIONA
test_bd()
