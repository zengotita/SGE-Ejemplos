#PUNTEROS, FUNCIONES SEEK y TELL
archivo = open("fichero_lineas.txt", "r")
contenido = archivo.read() # el puntero queda al final del documento
print(archivo.tell())
archivo.seek(0) #el puntero queda al PRINCIPIO del documento
print(archivo.tell())
archivo.close()

#######################################
print("".center(50,"#"))
#######################################
archivo = open("fichero_lineas.txt", "r")
archivo.readline()
print(archivo.tell())
archivo.close()
archivo = open("fichero_lineas.txt", "r")
print(archivo.tell())
