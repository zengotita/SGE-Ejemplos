import csv

datos = [["Nombre", "Apellido", "Nota"],['Aitor', 'Alonso', 'A'],['Leire', 'Aguirre', 'B']]

mi_fichero = open('archivo_ejemplo.csv', 'w', encoding='utf-8',newline='')
with mi_fichero:
    writer = csv.writer(mi_fichero)
    writer.writerows(datos)

print("Proceso de escritura completado")
