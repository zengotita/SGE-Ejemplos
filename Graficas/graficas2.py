import matplotlib.pyplot as plt
#Para añadir sombreado
from matplotlib.patches import Shadow

# Creamos una figura y sus ejes
figura = plt.figure(figsize=(6, 6))
ejes = figura.add_axes([0.1, 0.1, 0.8, 0.8])

#Etiquetas
labels = 'Python', 'Javascript', 'Swift', 'C++', 'C#', 'VisualBasic'
#Valores por cada una de las etiquetas
fracs = [30, 35, 7, 15, 10, 3]

#Separo un quesito con explode
explode = (0.2, 0, 0, 0, 0, 0)

#Creamos los quesitos
quesitos = ejes.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%')

#Loop para añadir etiqueta y borde
for w in quesitos[0]:
    # Añadir la etiqueta
    w.set_gid(w.get_label())

    # Sin bordes en los quesitos
    w.set_edgecolor("none")

#Por cada quesito, añadiremos sombra --> estética
for w in quesitos[0]:
    # Añade sombras
    s = Shadow(w, -0.01, -0.01)
    s.set_gid(w.get_gid() + "_shadow")
    s.set_zorder(w.get_zorder() - 0.1)
    ejes.add_patch(s)

# Añadimos título
plt.title("Lenguajes de programación")

# Guarda en un archivo png
plt.savefig('quesitos.png')

# Lo muestra
plt.show()




