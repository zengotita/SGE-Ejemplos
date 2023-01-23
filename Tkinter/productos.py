import tkinter as tk
# MÓDULO PARA AÑADIR ELEMENTOS A LA INTERFAZ
from tkinter import ttk
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import Text
from tkinter import messagebox
from interfaz_grafica2 import mostrar_mensaje


def insertar_producto():
    producto = input_producto.get()
    texto = area_texto.get("1.0",'end')
    radio_b=seleccion_radio.get()
    tipo=texto_desplegable.get()

    print(producto)
    print(texto.strip())
    print(tipo)
    print(radio_b)

    cadena = "Nombre del producto: " + producto + "\n" + "Descripción: " + texto.strip() + "\n" + "Tipo de producto: " + tipo + \
             "\n" + "Departamento: " + radio_b
    mostrar_mensaje(1,cadena)

    #Por hacer: insertar los datos en un fichero


def borrar_datos():
    #Borrar Producto
    input_producto.delete(0, 'end')
    #Borrar área de texto
    area_texto.delete(1.0, 'end')
    #Borrar Lista desplegable
    # --> POR HACER
    #Borrar radio button
    # --> POR HACER

##############################################################################################################################
# CREA LA VENTANA
ventana = tk.Tk()
# AÑADE TÍTULO Y DIMENSIONES
ventana.title("AÑADIR PRODUCTO")
#ventana.config(width=450, height=350)
ventana.geometry("450x450")
##############################################################################################################################
# Etiqueta y campo de texto - Nombre del producto
etiqueta_nombre_p = ttk.Label(text="Nombre del producto:    ")
etiqueta_nombre_p.place(x=20, y=20)

input_producto = ttk.Entry()
input_producto.place(x=145, y=20, width=180)
##############################################################################################################################
# LISTA DESPLEGABLE
etiqueta_tipo_p = ttk.Label(text="Tipo de producto:    ")
etiqueta_tipo_p.place(x=20, y=60)

tipos = ["Almacenable","Consumible","Servicio"]

# Texto que aparecerá en la lista desplegable
texto_desplegable = StringVar()

# AÑADIMOS EL TEXTO INICIAL
texto_desplegable.set("Selecciona tipo")

# CREAMOS Y COLOCAMOS LA LISTA DESPLEGABLE
menu_tipos = OptionMenu(ventana, texto_desplegable, *tipos)
# COLOCAMOS LA LISTA EN EL MENÚ CON .PLACE
menu_tipos.place(x=145, y=60, width=200)

##############################################################################################################################
# ÁREA DE TEXTO
etiqueta_descripción_p = ttk.Label(text="Descripción del producto:    ")
etiqueta_descripción_p.place(x=20, y=100)

area_texto = Text(ventana, height = 5, width = 52, bg="light yellow")
area_texto.place(x=20, y=120)
###############################################################
# RADIO BUTTON
etiqueta_radio_p = ttk.Label(text="Área al que pertenece el producto:    ")
etiqueta_radio_p.place(x=20, y=220)

seleccion_radio = tk.StringVar()
r1 = ttk.Radiobutton(ventana, text='Compras', value='Compras', variable=seleccion_radio)
r2 = ttk.Radiobutton(ventana, text='Ventas', value='Ventas', variable=seleccion_radio)
r3 = ttk.Radiobutton(ventana, text='Ambas', value='Compras/Ventas', variable=seleccion_radio)

r1.place(x=20, y=240)
r2.place(x=20, y=260)
r3.place(x=20, y=280)
###############################################################
boton_insertar_p = ttk.Button(text="Añadir producto", command=insertar_producto)
boton_insertar_p.place(x=300, y=300)
###############################################################
boton_insertar_p = ttk.Button(text="Borrar datos", command=borrar_datos)
boton_insertar_p.place(x=300, y=340)
###############################################################

# CARGA LA VENTANA
ventana.mainloop()