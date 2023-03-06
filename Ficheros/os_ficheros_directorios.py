import os
########################################################################################################################
# Archivos y directorios
directorio_proyecto=os.getcwd()

# 1 - Creamos el directorio donde guardaremos el fichero
try:
    os.mkdir("pruebas_ficheros")
except FileExistsError:
    print("El directorio ya existe")
# Exista o no, nos situamos dentro del directorio
os.chdir("pruebas_ficheros")

# 2 - Creamos el fichero vacío --> usamos open en modo w+
f=open("fichero.txt","w+")

# 3 - Mostramos el nombre del fichero
print("Nombre del fichero:",f.name)

# 4 - Cambiamos el nombre al archivo
f.close() # Si no lo cerramos, dará error porque no puede estar abierto antes de renombrarlo
try: os.rename(f.name,"fichero_nuevo.txt")
except FileExistsError: print("El fichero no puede ser renombrado")

# 5 - Eliminamos fichero
os.remove("fichero_nuevo.txt")

# 6 - Eliminamos directorio: primero cambiamos de directorio, para no estar dentro
os.chdir(directorio_proyecto)
os.rmdir("pruebas_ficheros")

########################################################################################################################

# FUNCIÓN PARA OBTENER LA RUTA ABSOLUTA DE LOS FICHEROS, EN BASE AL DIRECTORIO QUE INDIQUEMOS
# DEVUELVE UNA LISTA CON LA RUTA ABSOLUTA DE LOS FICHEROS DEL DIRECTORIO QUE HEMOS PASADO COMO ARGUMENTO
def ruta_absoluta(directorio):
    lista_directorios=[]
    for ruta,subdirectorios,archivos in os.walk(directorio):
        for a in archivos:
            lista_directorios.append(os.path.abspath(os.path.join(ruta, a)))
    return lista_directorios

def mostrar_ficheros(directorio,tipo):
    for ruta,subdirectorios,archivos in os.walk(directorio):
        for a in archivos:
            if a.endswith(tipo):
                print(a)


mostrar_ficheros(directorio_proyecto,".txt")