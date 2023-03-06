#csv.writer

import csv

#Lista de listas
datos = [["Nombre", "Apellido", "Nota"],['Aitor', 'Alonso','A'],['Leire', 'Aguirre','B']]

mi_fichero = open('ficheros_csv/alumnos2.csv', 'w',newline='')

for dato in datos:
    writer = csv.writer(mi_fichero,quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(dato)

mi_fichero.close()

print("El fichero se ha escrito correctamente")