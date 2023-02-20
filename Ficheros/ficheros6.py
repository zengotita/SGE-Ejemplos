# ESCRIBIR VARIAS LÍNEAS. JUSTO DEBAJO DE LA ÚLTIMA DEL FICHERO

archivo = open('fichero_escribir.txt', "a+",encoding='utf8')
contenido = archivo.read()
#Escribimos un salto de línea
archivo.write('\n')
final_de_archivo = archivo.tell()
lista = ['Línea 1\n', 'Línea 2']
archivo.writelines(lista)
archivo.seek(final_de_archivo)
print (archivo.readline())
# Línea 1
print (archivo.readline())
# Línea 2
