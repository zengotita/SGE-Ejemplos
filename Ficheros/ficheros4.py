archivo = open("fichero_lineas.txt", "r")
i = 1
for linea in archivo:
	linea = linea.rstrip('\n')
	print ('{0}: {1}'.format(i, linea))
	i+=1
archivo.close()
