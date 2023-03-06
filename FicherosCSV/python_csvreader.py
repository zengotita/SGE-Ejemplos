import csv

with open('ficheros_csv/personas.csv') as csvfichero:
    #Devuelve una lista de listas, incluida la cabecera
    reader = csv.reader(csvfichero, delimiter=',',
                        quoting=csv.QUOTE_NONNUMERIC, strict=True)

    for fila in reader:
        print(fila)
