'''
Ficheros en Python
'''
#######################################################
#Método read
def leer_archivo():
    archivo = open("ficheros/fichero.txt", "r")
    contenido = archivo.read()
    print(contenido)

#leer_archivo()
#######################################################
#Método readline: 3 funciones

def leer_linea():
    archivo = open("ficheros/fichero.txt", "r")
    #sólo leerá una línea, porque llamamos a readline() sólo una vez
    linea1 = archivo.readline()
    print(linea1)

    archivo.close()

#leer_linea()
#
# Segunda función: leer todas las líneas con while
def leer_todas_las_lineas1():
    archivo = open("ficheros/fichero.txt", "r")
    linea = archivo.readline()
    print(linea)
    while linea != '':
        # procesar línea
        linea = archivo.readline()
        print(linea)

    archivo.close()

#leer_todas_las_lineas1()
#
# Tercera función: leer todas con for
def leer_todas_las_lineas2():
    archivo = open("ficheros/fichero.txt", "r")
    for linea in archivo:
        print(linea)
    archivo.close()
#leer_todas_las_lineas2()

#######################################################
#Método readlines()

def metodo_readlines():
    archivo = open("ficheros/fichero.txt", "r")
    lineas = archivo.readlines()
    print(lineas)
    for linea in archivo.readlines():
         print (linea)

    archivo.close()

    # Guardo en una variable todas las líneas
    # archivo = open("ficheros/fichero.txt", "r")
    # lineas = archivo.readlines()

#metodo_readlines()

#######################################################
# Método seek()

def metodo_seek():
    archivo = open("ficheros/fichero.txt", "r")
    print(archivo.read())
    # Después de usar el método read, el puntero queda al final del documento
    print("Posición del puntero: ", archivo.tell())
    # Nos posicionamos nuevamente en la primera posición
    archivo.seek(0)
    print("Posición del puntero después de seek(0): ", archivo.tell())

#metodo_seek()

#######################################################
# Mostrar líneas con FOR y sin usar read
def mostrar_info_lineas():
    archivo = open("ficheros/fichero.txt")
    i = 1
    for linea in archivo:
        linea = linea.rstrip('\n')
        print ('{0}: {1}'.format(i, linea))
        i+=1
    archivo.close()

#mostrar_info_lineas()
#######################################################
# Método de ESCRITURA: write
def escribir_nueva_linea():
    archivo = open("ficheros/fichero2.txt", "r+")
    contenido = archivo.read()
    #Ahora el puntero apunta el final del fichero, después de "read"
    final_de_archivo = archivo.tell()

    #Estando al final, escribimos el texto con write
    archivo.write('Nueva linea')

    #Volvemos a antes de escribir la nueva línea
    archivo.seek(final_de_archivo)

    #Leemos a partir de aquí, es decir, lo que hemos escrito
    nuevo_contenido = archivo.read()

    print (nuevo_contenido)
    # Nueva linea

#escribir_nueva_linea()

#######################################################
# Método de ESCRITURA: writelines
def escribir_varias_lineas():

    archivo = open("ficheros/fichero2.txt", "r+")
    contenido = archivo.read()
    # Ahora el puntero apunta el final del fichero, después de "read"
    final_de_archivo = archivo.tell()

    #Lista de líneas que queremos escribir: añadimos \n al final para el salto de línea
    lista = ['\nLinea 1\n', 'Linea 2']

    #Escribimos todos los elementos de la lista
    archivo.writelines(lista)

    #Nos posicionamos antes de haber añadido las líneas
    archivo.seek(final_de_archivo)

    #Leemos la primera línea nueva y luego la segunda
    print (archivo.readline())
    # Línea 1
    print (archivo.readline())
    # Línea 2

#escribir_varias_lineas()

#######################################################
#Estados de los ficheros
def estados_fichero():
    # Fichero para lectura y escritura. El puntero se posiciona al principio
    mi_fichero = open("ficheros/fichero.txt","r+")

    # Nombre
    print("Nombre del fichero: ",mi_fichero.name)
    # Estado: si está cerrado o no
    print("¿Está cerrado? ",mi_fichero.closed)
    # Modo en el que se ha abierto
    print("Modo: ",mi_fichero.mode)
    # Codificación de caracteres
    print("Codificación: ",mi_fichero.encoding)

    #Cerramos fichero
    mi_fichero.close()

    print("\n")

    # Comprobamos que está cerrado después de haberlo hecho
    print("¿Está cerrado? ",mi_fichero.closed)

