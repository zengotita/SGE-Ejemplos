##Ejemplo de métodos __init__ y __repr__ en herencia con args y kwargs

##Clase Punto
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return "x: {}, y: {}".format(self.x, self.y)

##Clase Circulo, hereda de punto, pero necesitamos el radio
class Circulo(Punto):
    def __init__(self, radio, *args, **kwargs):
        self.radio = radio
        super().__init__(*args, **kwargs)
    def __repr__(self):
        return "x: {}, y: {}, radio: {}".format(self.x, self.y, self.radio)

##Podemos crear un objeto de la clase Circulo:
print(Circulo(10, 1, 1))
