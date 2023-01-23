import personacentroed


class Alumno(personacentroed.Persona_Centroed):

    def __init__(self, id, nombre, apellidos, edad, codigoalumno):
        super().__init__(id, nombre, apellidos, edad)
        self.codigoalumno = codigoalumno

    def __str__(self):
        cadena0 = "{0}".format(super().__str__())
        cadena = "- Código alumno: " + str(self.codigoalumno)
        return cadena0 + "\n" + cadena

    #GETTER
    def getCodigoAlumno(self):
        return self.codigoalumno

    #SETTER
    def setCodigoAlumno(self, codigoalumno):
        self.codigoalumno = codigoalumno

    #FUNCIONES

    def realizar_Examen(self):
        print("El alumno " + str(self.nombre) + " " + str(self.apellidos) + " realiza un examen")
    def realizar_Practica(self):
        print("El alumno " + str(self.nombre) + " " + str(self.apellidos) + " realiza una práctica")
    def atiende(self):
        print("El alumno " + str(self.nombre) + " " + str(self.apellidos) + " atiende en clase")