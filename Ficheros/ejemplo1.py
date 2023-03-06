###########
#Escribir#
###########
# Crear una lista de tuplas con los datos de los participantes
datos = [("Ion", 10), ("Ane", 8), ("Maider", 5), ("Jokin", 7)]

# Abrir el archivo en modo escritura
with open("ejemplo1.txt", "w") as archivo:
    # Recorremos la lista de tuplas y escribimos cada tupla en una línea del archivo
    for tupla in datos:
        # Convertimos la puntuación en una cadena
        linea = f"{tupla[0]},{str(tupla[1])}\n"
        archivo.write(linea)

######
#Leer#
######
# Abrimos el archivo en modo lectura
with open("ejemplo1.txt", "r") as archivo:
    # Creamos una lista vacía para guardar los datos leídos
    datos2 = []
    # Recorremos las líneas del archivo
    for linea in archivo:
        # Eliminamos el carácter de nueva línea al final de la línea
        linea = linea.strip()
        # Separamos los valores de la línea por la coma
        valores = linea.split(",")
        # Convertimos la puntuación de la cadena a un valor numérico
        valores[1] = int(valores[1])
        # Creamos una tupla con los valores y la agregamos a la lista
        tupla = tuple(valores)
        datos2.append(tupla)

# Imprimimos la lista de tuplas con los datos leídos
print(datos2)
