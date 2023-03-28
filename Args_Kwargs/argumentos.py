##Args y kwargs como argumentos de una función

## Función base
def resultado(x, y, op):
	if op == '+':
		return x + y
	elif op == '-':
		return x - y

## Posibles llamadas a la función:
### Llamada "normal":
print(resultado(1, 2, '+'))
'''Resultado: 3'''
### Llamadas con args I:
a = (1, 2, '+')
print(resultado(*a))
'''Resultado: 3'''
### Llamadas con args II:
b = (2, '-')
print(resultado(3, *b))
'''Resultado: 1'''
### Llamadas con kwargs I:
c = {'x': 1, 'y': 2, 'op': '+'}
print(resultado(**c))
'''Resultado: 3'''


