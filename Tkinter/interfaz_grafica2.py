import tkinter as tk
from tkinter import ttk
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import Text
from tkinter import messagebox

#FUNCIONES
def funcion_simple():
    print("Hola")

def mostrar_mensaje(tipo,mensaje):
    #DICCIONARIO QUE GUARDA LAS DIFERENTES FUNCIONES
    tipo_mensaje = {1:lambda mensaje: messagebox.showinfo(title="Info",message=mensaje),
                    2:lambda mensaje: messagebox.showwarning(title="Aviso",message=mensaje),
                    3:lambda mensaje: messagebox.showerror(title="Error",message=mensaje),
                    4:lambda mensaje: messagebox.askquestion(title="Pregunta",message=mensaje),
                    5:lambda mensaje: messagebox.askyesno(title="¿Continuar?",message=mensaje),
                    6:lambda mensaje: messagebox.askokcancel(title="¿Ok o no?",message=mensaje),
                    7:lambda mensaje: messagebox.askyesnocancel(title="¿Cancelar?",message=mensaje),
                    8:lambda mensaje: messagebox.askretrycancel(title="¿Intentarlo otra vez?",message=mensaje),
                    9:funcion_simple}

    #LLAMADA A LA FUNCIÓN QUE SE DESEA --> LAS FUNCIONES ESTÁN GUARDADAS EN EL DICCIONARIO
    #Nota: desde la interfaz gráfica recogemos strings, por lo que en este caso debemos usar int()
    tipo_mensaje[int(tipo)](mensaje)


def mensaje():
    mensaje=area_texto.get("1.0",'end')
    tipo_mensaje=lista_desplegable.get()
    # Obtenemos de una lista desplegable la opción que define el tipo de mensaje
    # El texto aparece en el área de texto
    mostrar_mensaje(tipo_mensaje,mensaje)

if __name__ == "__main__":
    ##########################################################################
    # CREA LA VENTANA
    ventana = tk.Tk()
    ventana.title("MENSAJES EMERGENTES")
    ventana.geometry("500x500")
    ##########################################################################
    # LISTA DESPLEGABLE
    etiqueta_tipo_p = ttk.Label(text="Número:    ")
    etiqueta_tipo_p.place(x=10, y=60)

    tipos_num = [1,2,3,4,5,6,7,8,9]
    lista_desplegable = ttk.Combobox(ventana, values=tipos_num,width=7) # Combobox
    lista_desplegable.set("--Elige--")
    lista_desplegable.place(x=60, y=60)
    ##########################################################################
    # ÁREA DE TEXTO
    area_texto = Text(ventana, height = 5, width = 52, bg="light cyan")
    area_texto.place(x=20, y=120)

    ##########################################################################
    boton_insertar_p = ttk.Button(text="Mensaje", command=mensaje)
    boton_insertar_p.place(x=50, y=220)
    ##########################################################################

    ventana.mainloop()