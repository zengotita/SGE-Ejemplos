import csv

resultados = []
with open('ficheros_csv/datos_ejemplo.csv') as csvfichero:
    #Devuelve un objeto que guarda diccionarios
    reader = csv.DictReader(csvfichero)
    #print(reader) --> <csv.DictReader object at 0x000002CEFE3925E0>
    for fila in reader:
        #print(fila) --> Diccionario con datos
        print(fila['Nombre'],fila['Apellido'])
        #Guardamos los resultados en una lista
        resultados.append(fila)

#Sacamos por pantalla la lista de resultados: lista de diccionarios
print(resultados)

#Nombre del primer registro
print(resultados[0]['Nombre'])
