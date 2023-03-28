## Ejemplo de uso de *args

## Función suma de dos números
def sum(x, y):
	return x + y
## Llamamos a la función con 2 argumentos y funciona
print(sum(2,3))
'''Resultado: 5'''

## Si se llama con más de 2 argumentos, da error
#print(sum(2,3,4))
'''Resultado: TypeError: sum() takes 2 positional arguments but 3 were given'''

## Función suma de n números con args
def sum2(*args):
	value = 0
	for n in args:
		value += n
	return value

## Ahora podemos llamar a la función con n argumentos
print(sum2(2,3,4))
'''Resultado: 9'''
print(sum2(2,3,4,5,6,7,8,9,10))
'''Resultado: 54'''

