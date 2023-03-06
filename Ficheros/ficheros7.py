import csv

import csv
'''
    with open('archivo_csv_alumnos.csv', 'w') as csvfichero:
    campos = ['Nombre', 'Apellido', 'Nota']
    writer = csv.DictWriter(csvfichero, fieldnames= campos)
    writer.writeheader()
    writer.writerow({'Nota': 'B', 'Nombre': 'Aitor', 'Apellido': 'Urrutia'})
'''
# CORRIGE EL SALTO DE LÍNEA ADICIONAL QUE SE HACE

############################################################
#Lectura de archivo CSV
import csv
with open('archivo_csv_alumnos.csv', 'r') as csvfichero:
    reader = csv.DictReader(csvfichero)
    for fila in reader:
        print(fila['Nombre'], fila['Apellido'], fila['Nota'])


with open('archivo_csv_alumnos.csv') as csvfichero:
    reader = csv.reader(csvfichero, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for fila in reader:
        print(fila)

resultados = []

with open('archivo_csv_alumnos.csv') as csvfichero:
    reader = csv.DictReader(csvfichero)
    for fila in reader:
        resultados.append(fila)
print (resultados)

