import os
########################################################################################################################
# os.chdir(directorio_nuevo)
# Cambiar de directorio
directorio_proyecto=os.getcwd()
directorio_nuevo="Ficheros"
print("Directorio actual: ",os.getcwd())
os.chdir(directorio_nuevo)
print("Directorio nuevo: ",os.getcwd())
os.chdir(directorio_proyecto)
print("Vuelta al directorio original: ",os.getcwd())
########################################################################################################################
# -->  os.access(directorio, modo_de_acceso) <-
# Comprobar si es posible acceder a un archivo: Ruta + Modo
# Devuelve True/false
# Modo:
# --> os.F_OK: comprueba si el directorio existe
# --> os.R_OK: comprueba si es posible leer el contenido del directorio
# --> os.W_OK: comprueba si es posible escribir en el directorio
# --> os.X_OK: comprueba si el fichero tiene permisos de ejecución
directorio = "Ficheros"
print("El directorio existe: ", os.access(directorio,os.F_OK))
print("El directorio se puede leer: ", os.access(directorio,os.R_OK))
print("Se puede escribir en el directorio: ", os.access(directorio,os.W_OK))
print("Tiene permisos de ejecución:", os.access(directorio,os.X_OK))

########################################################################################################################
# os.getcwd()
# Devuelve el directorio actual
print("Directorio actual: ",os.getcwd())

########################################################################################################################
# os.mkdir(ruta, modo)
# ruta --> ruta donde se creará el nuevo directorio. Si sólo se especifica el nombre, se creará en el directorio actual.
# modo --> permisos que tendrá el directorio, 0o777, 0o655, etc. (por defecto 0o777)
# FileExistsError --> excepción que salta si el directorio ya existe
try: os.mkdir("Nuevo_directorio")
except FileExistsError: print("El directorio ya existe")

########################################################################################################################
# os.rmdir(ruta)
# ruta --> ruta y nombre del directorio que se quiere eliminar.
os.rmdir("Nuevo_directorio")

########################################################################################################################
# OS.PATH
# RUTA ABSOLUTA --> Obtenemos la ruta absoluta teniendo en cuenta el directorio que le pasamos como argumento
directorio_proyecto=os.getcwd()
ruta_absoluta = os.path.abspath(directorio_proyecto)
print("Ruta absoluta: ", ruta_absoluta)

# Directorio base: sólo muestra el nombre de la carpeta principal. Podemos pasarle la ruta absoluta también.
directorio_base = os.path.basename(directorio_proyecto)
print("Directorio base del proyecto: ",directorio_base)

# Comprobamos si un directorio existe con os.path.exists
print("Existe el directorio: ", os.path.exists(directorio_proyecto))

# Obtenemos el tamaño del directorio con os.path.getsize(directorio)
print("Tamaño del directorio: ", os.path.getsize(directorio_proyecto))

# Sabemos si es directorio con os.path.isdir(directorio)
print("¿Es directorio? --> ", os.path.isdir(directorio_proyecto))

# O si es fichero con os.path.isfile(directorio)
print("¿Es fichero? --> ", os.path.isfile(directorio_proyecto))