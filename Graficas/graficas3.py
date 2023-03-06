import numpy as np
import matplotlib.pyplot as plt

# Datos guardados en una lista
dataset = [30, 20, 7, 18, 45, 30]
nombres = ('Op1', 'Op2', 'C', 'D', 'E','F')
y_pos = np.arange(len(nombres)) #creamos el array con los nombres

# Creamos las barras: primero los nombres, luego los datos y añadimos color (rgb + opacidad)
plt.bar(y_pos, dataset, color=(0.2, 0.7, 0.7, 1))

# Añadimos título y nombre a los ejes
plt.title('Mis datos')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Límites para el eje Y - ajustará que se vea de 10 en 10
plt.ylim(0, 60)


# Añadimos los nombres
plt.xticks(y_pos, nombres)

# Guarda en un archivo png - este paso lo hacemos antes de mostrar la gráfica, si no, no guarda nada
plt.savefig('barras.jpg')

# Mostramos gráfica
plt.show()


