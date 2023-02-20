archivo = open('fichero_escribir.txt', "a+")
contenido = archivo.read()
final_de_archivo = archivo.tell()

archivo.write('Nueva linea')
archivo.seek(final_de_archivo)
nuevo_contenido = archivo.read()

print (nuevo_contenido)

#Escribe al final, pero no realiza un salto de línea
#¿Cómo podemos escribir en una nueva línea por lo tanto?
