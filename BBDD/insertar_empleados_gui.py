## TKINTER
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

## BASE DE DATOS
import pymysql

# FUNCIÓN PARA ESTABLECER LA CONEXIÓN CON LA BASE DE DATOS
def conexion():
    host = '127.0.0.1'
    usuario = 'root'
    password = '12345Abcde'
    base_datos = 'testsge'
    puerto = 3306

    return(pymysql.connect(host=host, user=usuario,password=password ,db=base_datos, port=puerto))

# FUNCIÓN PARA MOSTRAR MENSAJES EN UNA VENTANA EMERGENTE
def mostrar_mensaje(tipo,mensaje):
    #DICCIONARIO QUE GUARDA LAS DIFERENTES FUNCIONES
    tipo_mensaje = {1:lambda mensaje: messagebox.showinfo(title="Info",message=mensaje),
                    2:lambda mensaje: messagebox.showwarning(title="Aviso",message=mensaje),
                    3:lambda mensaje: messagebox.showerror(title="Error",message=mensaje),
                    4:lambda mensaje: messagebox.askquestion(title="Pregunta",message=mensaje),
                    5:lambda mensaje: messagebox.askyesno(title="¿Continuar?",message=mensaje),
                    6:lambda mensaje: messagebox.askokcancel(title="¿Ok o no?",message=mensaje),
                    7:lambda mensaje: messagebox.askyesnocancel(title="¿Cancelar?",message=mensaje),
                    8:lambda mensaje: messagebox.askretrycancel(title="¿Intentarlo otra vez?",message=mensaje)}

    #LLAMADA A LA FUNCIÓN QUE SE DESEA --> LAS FUNCIONES ESTÁN GUARDADAS EN EL DICCIONARIO
    #Nota: desde la interfaz gráfica recogemos strings, por lo que en este caso debemos usar int()
    tipo_mensaje[int(tipo)](mensaje)

def borrar_datos():
    #Borrar Producto
    input_nombre.delete(0, 'end')
    #Borrar Apellido
    input_apellido.delete(0,'end')
    #Borrar DNI
    input_dni.delete(0,'end')
    #Borrar Checkboxes
    check1.set(0)
    check2.set(0)
    check3.set(0)
    check4.set(0)

# FUNCIÓN PARA INSERTAR DATOS
def insertar_datos_generica(db,tabla,columnas,valores):
    try:
        cursor = db.cursor()

        consulta = "INSERT INTO " + tabla + "("+ columnas +") VALUES (" + valores + ")"
        print(consulta)

        # Ejecutar SQL --> es un string
        cursor.execute(consulta)
        db.commit()
        print('Registro insertado correctamente')
    except:
        print('Error en la consulta o en la conexión')
        db.rollback() #Deshacer cambios

# FUNCIÓN ASIGNADA AL BOTÓN DEL FORMULARIO DE INSERTAR DATOS
def insertar_empleado():
    nombre = input_nombre.get()
    apellido = input_apellido.get()
    dni = input_dni.get()
    compras=check1.get()
    ventas = check2.get()
    rrhh = check3.get()
    produccion = check4.get()

    departamentos=""
    if (compras): departamentos = departamentos + " Compras"
    if (ventas): departamentos = departamentos + " Ventas"
    if (rrhh): departamentos = departamentos + " RRHH"
    if (produccion): departamentos = departamentos + " Producción"
    departamentos = departamentos.replace(" ",", ").lstrip(", ")

    cadena = "Nombre: " + nombre + "\n" + "Apellido: " + apellido + "\n" + "DNI: " + dni + "\n" + "Departamentos: " + departamentos
    mostrar_mensaje(1,cadena)

    ##########################################################################
    # CONEXIÓN
    db = conexion()

    # TABLA
    tabla = 'TRABAJADORES'

    #AÑADIMOS EL REGISTRO
    columnas = "NOMBRE,APELLIDO,DNI,COMPRAS,VENTAS,RRHH,PRODUCCION"

    #VALORES PARA INSERTAR
    valores="'"+str(nombre)+"','"+str(apellido)+"','"+str(dni)+"','"+str(compras)+"','"+str(ventas)+"','"+str(rrhh)+"','"+str(produccion)+"'"

    # LLAMAMOS A LA FUNCIÓN
    insertar_datos_generica(db, tabla, columnas, valores)

    # BORRAMOS TODOS LOS CAMPOS DEL FORMULARIO
    borrar_datos()

##############################################################################################################################
# CREA LA VENTANA
ventana = tk.Tk()
# AÑADE TÍTULO Y DIMENSIONES
ventana.title("AÑADIR EMPLEADO")
#ventana.config(width=450, height=350)
ventana.geometry("360x360")
##############################################################################################################################
# Etiqueta y campo de texto - Nombre del empleado
etiqueta_nombre_e = ttk.Label(text="Nombre:    ")
etiqueta_nombre_e.place(x=20, y=20)

input_nombre = ttk.Entry()
input_nombre.place(x=145, y=20, width=180)
##############################################################################################################################
# Etiqueta y campo de texto - Apellido del empleado
etiqueta_apellido_e = ttk.Label(text="Apellido:    ")
etiqueta_apellido_e.place(x=20, y=60)

input_apellido = ttk.Entry()
input_apellido.place(x=145, y=60, width=180)
##############################################################################################################################
# Etiqueta y campo de texto - DNI del empleado
etiqueta_dni_e = ttk.Label(text="DNI:    ")
etiqueta_dni_e.place(x=20, y=100)

input_dni = ttk.Entry()
input_dni.place(x=145, y=100, width=180)
##############################################################################################################################
# DEPARTAMENTOS
etiqueta_radio_p = ttk.Label(text="Departamentos al que pertenece el empleado:    ")
etiqueta_radio_p.place(x=20, y=140)

check1 = tk.IntVar()
check2 = tk.IntVar()
check3 = tk.IntVar()
check4 = tk.IntVar()

tk.Checkbutton(text="Compras", variable=check1, onvalue=1, offvalue=0).place(x=20, y=170)
tk.Checkbutton(text="Ventas", variable=check2, onvalue=1, offvalue=0).place(x=100, y=170)
tk.Checkbutton(text="RRHH", variable=check3, onvalue=1, offvalue=0).place(x=20, y=210)
tk.Checkbutton(text="Producción", variable=check4, onvalue=1, offvalue=0).place(x=100, y=210)
##############################################################################################################################
boton_insertar_p = ttk.Button(text="Añadir producto", command=insertar_empleado)
boton_insertar_p.place(x=200, y=260)
###############################################################
boton_insertar_p = ttk.Button(text="Borrar datos", command=borrar_datos)
boton_insertar_p.place(x=200, y=300)
###############################################################

# CARGA LA VENTANA
ventana.mainloop()