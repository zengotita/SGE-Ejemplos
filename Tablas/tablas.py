from prettytable import PrettyTable
from termcolor import colored as clrd
import hashlib

# Doc prettytable: https://pypi.org/project/prettytable/
# Doc termcolor: https://pypi.org/project/termcolor/

# CREAMOS EL OBJETO TABLA
tabla = PrettyTable()

# CABECERA DE LA TABLA
# PODRÍAMOS COLOREAR PARTES DE LA TABLA, PERO OJO, LUEGO PODRÍAMOS TENER PROBLEMAS A LA HORA DE FILTRAR SI NO PONEMOS LO MISMO
tabla.field_names = [clrd("NOMBRE",'blue'), clrd("APELLIDO",'blue'), clrd("DEPARTAMENTO",'blue'),clrd("EMAIL",'blue'),clrd("CONTRASEÑA",'red')]

#tabla.field_names = ["NOMBRE","APELLIDO", "DEPARTAMENTO","EMAIL","CONTRASEÑA"]

# FILAS DE LA TABLA
tabla.add_row(["Nombre 1", "Apellido 1", "Compras", "usuario1@egibide.org",hashlib.md5("querty123".encode('utf8')).hexdigest()])
tabla.add_row(["Nombre 2", "Apellido 2", "Ventas", "usuario2@egibide.org", hashlib.md5("12345Abcde".encode('utf8')).hexdigest()])
tabla.add_row(["Nombre 3", "Apellido 3", "Marketing", "usuario3@egibide.org", hashlib.md5("password".encode('utf8')).hexdigest()])
tabla.add_row(["Nombre 4", "Apellido 4", "Producción", "usuario4@egibide.org", hashlib.md5("Contraseña".encode('utf8')).hexdigest()])
tabla.add_row(["Nombre 5", "Apellido 5", "Compras", "usuario5@egibide.org", hashlib.md5("Abcde12345".encode('utf8')).hexdigest()])

print(tabla)

# ALINEAR LA TABLA A LA IZQUIERDA, CENTRO O DERECHA
tabla.align = "r" # ---> "l" , "c" , "r"
print(tabla)

# ORDENAR POR DEPARTAMENTOS
#tabla.sortby = "DEPARTAMENTO"
tabla.sortby = clrd("DEPARTAMENTO",'blue')
print(tabla)


# BORRAR FILA
tabla.del_row(3)
print(tabla)

# BORRAR DATOS:
tabla.clear_rows()
print(tabla)



