# Abrir fichero y leer el contenido
archivo = open("fichero.txt", "r")
contenido = archivo.read()
print(contenido)

# Abrir y leer una línea
archivo = open("fichero_lineas.txt", "r")
linea1 = archivo.readline()
print("Línea: ",linea1)
linea2 = archivo.readline()
print("Línea: ", linea2)
