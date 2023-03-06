datos = [{'Nota': 'B', 'Nombre': 'Aitor', 'Apellido': 'Urrutia'},
{'Nota': 'A', 'Nombre': 'Miren', 'Apellido': 'Rodriguez'},
{'Nota': 'C', 'Nombre': 'Mikel', 'Apellido': 'Loidi'},
{'Nota': 'B', 'Nombre': 'Juan', 'Apellido': 'Lopez'},
{'Nota': 'A', 'Nombre': 'Olaia', 'Apellido': 'Vela'}]

#writerows
import csv

#Usando "with open" no tenemos que utilizar el método close()
with open('ficheros_csv/datos_ejemplo3.csv', 'w', newline='') as csvfichero:
    # Definimos la cabecera: una lista con cada una de las columnas
    campos =['Nombre', 'Apellido', 'Nota']
    # Con fieldnames ya indicamos cuál va a ser la cabecera
    writer = csv.DictWriter(csvfichero, fieldnames= campos)
    # Método para escribir la cabecera
    writer.writeheader()
    # Con writerows sólo necesitamos un argumento: una lista de diccionarios
    writer.writerows(datos)

print("El fichero se ha escrito correctamente")
