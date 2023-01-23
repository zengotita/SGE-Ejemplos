import personacentroed


class PAS(personacentroed.Persona_Centroed):

    def __init__(self, id, nombre, apellidos, edad, codigoPAS):
        super().__init__(id, nombre, apellidos, edad)
        self.codigoPAS = codigoPAS

    def __str__(self):
        cadena0 = "{0}".format(super().__str__())
        cadena = "- Código PAS: " + str(self.codigoPAS)
        return cadena0 + "\n" + cadena

    # GETTER
    def getCodigoPAS(self):
        return self.codigoPAS

    # SETTER
    def setCodigoAlumno(self, CodigoPAS):
        self.codigoPAS = CodigoPAS

    # FUNCIONES

    def visualizar_incidencia(self):
        print(str(self.nombre) + " " + str(self.apellidos) + " con el código " + str(self.codigoPAS) + " visualiza una incidencia ")

    def resolver_incidencia(self):
        print(str(self.nombre) + " " + str(self.apellidos) + " con el código " + str(self.codigoPAS) + " resuelve una incidencia ")


    #REIMPLEMENTAMOS UNA FUNCIÓN DE LA CLASE SUPERIOR --> sobrecarga de un método
    def asistir_centro(self):
        print("El trabajador " + str(self.nombre) + " " + str(self.apellidos) + " asiste al centro")