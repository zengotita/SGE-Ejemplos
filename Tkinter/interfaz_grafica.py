import tkinter as tk
from tkinter import ttk

def convertir():
    gigas = float(caja_gigas.get())
    temp_kelvin = gigas * 1024

    etiqueta_megas.config(text=f"Megabytes: {temp_kelvin} MB")


# CREA LA VENTANA
ventana = tk.Tk()
# AÑADE TÍTULO Y DIMENSIONES
ventana.title("Conversor")
ventana.config(width=450, height=250)


etiqueta_gigas = ttk.Label(text="Gigabytes:")
etiqueta_gigas.place(x=20, y=20)

caja_gigas = ttk.Entry()
caja_gigas.place(x=140, y=20, width=60)

boton_convertir = ttk.Button(text="Convertir a MB", command=convertir)
boton_convertir.place(x=230, y=20)


etiqueta_megas = ttk.Label(text="Megabytes: --")
etiqueta_megas.place(x=20, y=120)

ventana.mainloop()