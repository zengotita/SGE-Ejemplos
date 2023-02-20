# TRATAR LÍNEA A LÍNEA EL FICHERO
archivo = open("fichero_lineas.txt", "r")
linea = archivo.readline()
while linea != '':
    # procesar línea
    print(linea.strip())
    linea = archivo.readline()
archivo.close()

# MISMO EJEMPLO CON FOR
print("".center(50,"#"))
archivo = open("fichero_lineas.txt", "r")
for linea in archivo:
    print(linea.strip())
archivo.close()