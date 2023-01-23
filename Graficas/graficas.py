import matplotlib.pyplot as plt

#Doc: https://matplotlib.org/stable/tutorials/introductory/pyplot.html


circulo1 = plt.Circle((0.5, 0.5), 0.1, color='b')

fig, ejes = plt.subplots()

ejes.add_artist(circulo1)

#Guardo la "figura"
fig.savefig('circulos.png')

#Muestra la figura
plt.show()


#####################################################