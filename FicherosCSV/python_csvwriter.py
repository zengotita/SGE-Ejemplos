#csv.writer

import csv

#Lista de listas
datos = [["Nombre", "Apellido", "Nota"],['Aitor', 'Alonso','A'],['Leire', 'Aguirre','B']]

mi_fichero = open('ficheros_csv/alumnos.csv', 'w',newline='')

with mi_fichero:
    writer = csv.writer(mi_fichero,quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(datos)

print("El fichero se ha escrito correctamente")
