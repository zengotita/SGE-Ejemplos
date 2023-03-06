#writerow
import csv

#Usando "with open" no tenemos que utilizar el método close()
with open('ficheros_csv/datos_ejemplo.csv', 'w', newline='') as csvfichero:
    #Definimos la cabecera: una lista con cada una de las columnas
    campos = ['Nombre', 'Apellido', 'Nota']
    #Con fieldnames ya indicamos cuál va a ser la cabecera
    writer = csv.DictWriter(csvfichero, fieldnames=campos)

    #Método para escribir la cabecera
    writer.writeheader()
    #A pesar de indicar primero la nota, se colocan todos los campos en el orden correcto
    writer.writerow({'Nota': 'B', 'Nombre': 'Aitor', 'Apellido': 'Urrutia'})
    writer.writerow({'Nota': 'A', 'Nombre': 'Miren', 'Apellido': 'Rodriguez'})
    writer.writerow({'Nota': 'C', 'Nombre': 'Mikel', 'Apellido': 'Loidi'})
    writer.writerow({'Nota': 'B', 'Nombre': 'Jose', 'Apellido': 'Lopez'})
    writer.writerow({'Nota': 'A', 'Nombre': 'Olaia', 'Apellido': 'Vela'})


print("El fichero se ha escrito correctamente")
