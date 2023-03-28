import pymysql
## Ejemplo de uso de **kwargs

## Funcion de crear tabla para el ejemplo
def crear_tabla_empleados():
    # Conexión a la base de datos
    db = pymysql.connect(host="localhost",user="root",password="12345Abcde",database="testsge")
    # Preparar el cursor
    cursor = db.cursor()
    # Eliminar tabla (drop) si ya existe --> ¡Cuidado! No se podrá eliminar si existen relaciones. Habría que ir en orden
    # --> Si la clave de esta tabla es una clave foránea de otra, hay que eliminar ese "constraint" o limitador con ALTER TABLE
    cursor.execute("DROP TABLE IF EXISTS CLIENTES")
    # SQL para crear tabla
    sql = """CREATE TABLE CLIENTES (
        NOMBRE  VARCHAR(30),
        APELLIDO VARCHAR(40),
        FECHA_ALTA VARCHAR(40),
        CIUDAD VARCHAR(40),
        PROVINCIA VARCHAR(40),
        TIPO VARCHAR(40),
        FECHA_NACIMIENTO VARCHAR(40))"""
    cursor.execute(sql)
    # Desconectar del servidor
    db.close()

crear_tabla_empleados()

## Función para filtrar usuarios por ciudad, provincia y fecha de alta
def filter(ciudad, provincia, fecha_alta):
    return "SELECT * FROM clientes WHERE ciudad='{}' AND provincia='{}' AND fecha_alta={};".format(ciudad, provincia, fecha_alta)

## Llamamos a la función con 3 argumentos
print(filter('Madrid', 'Madrid', '2020-01-01'))
'''Resultado: SELECT * FROM clientes WHERE ciudad='Madrid' AND provincia='Madrid' AND fecha_alta=2020-01-01;'''

## Función para filtrar usuarios con kwargs
def filter2(**kwargs):
    query = "SELECT * FROM clientes"
    i = 0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE "
        else:
            query += " AND "
        query += "{}='{}'".format(key, value)
        i += 1
    query += ";"
    return query

## Ahora podemos llamar a la función con n argumentos (clave=valor)
print(filter2(provincia='Madrid', ciudad='Madrid', fecha_alta='2020-01-01'))
'''Resultado: SELECT * FROM clientes WHERE ciudad='Madrid' AND provincia='Madrid' AND fecha_alta='2020-01-01';'''

print(filter2(ciudad='Madrid', provincia='Madrid', fecha_alta='2020-01-01', tipo='Empleado', fecha_nacimiento='1990-01-01'))
'''Resultado: SELECT * FROM clientes WHERE ciudad='Madrid' AND provincia='Madrid' AND fecha_alta='2020-01-01' AND tipo='Empleado' AND fecha_nacimiento='1990-01-01';'''