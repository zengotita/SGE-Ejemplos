import personacentroed


class Profesor(personacentroed.Persona_Centroed):

    def __init__(self, id, nombre, apellidos, edad, numeroProfesor,asignaturas):
        super().__init__(id, nombre, apellidos, edad)
        self.numeroProfesor = numeroProfesor
        self.asignaturas = asignaturas

    def __str__(self):
        cadena0 = "{0}".format(super().__str__())
        cadena = "- Número de profesor: " + str(self.numeroProfesor) + "\n" + "- Asignaturas: " + str(self.listar_asignaturas())
        return cadena0 + "\n" + cadena

    # GETTERS
    def getNumeroProfesor(self):
        return self.numeroProfesor

    def getAsignaturas(self):
        return self.asignaturas

    # SETTERS
    def setCodigoAlumno(self, numeroProfesor):
        self.numeroProfesor = numeroProfesor

    def setAsignaturas(self, asignaturas):
        self.asignaturas = asignaturas

    # FUNCIONES

    def corregir_Examen(self):
        print("El profesor " + str(self.nombre) + " " + str(self.apellidos) + " realiza un examen")

    def preparar_Practica(self):
        print("El profesor " + str(self.nombre) + " " + str(self.apellidos) + " prepara una práctica")

    def impartir(self):
        print("El profesor " + str(self.nombre) + " " + str(self.apellidos) + " imparte una clase")

    def listar_asignaturas(self):
        asign=""
        for i in self.asignaturas:
            asign = asign + ", " + i
        return asign.lstrip(",")

    #REIMPLEMENTAMOS FUNCIONES DE LA CLASE SUPERIOR --> sobrecarga de métodos
    def asistir_centro(self):
        print("El profesor " + str(self.nombre) + " " + str(self.apellidos) + " asiste al centro")

    def salir_centro(self):
        print("El profesor " + str(self.nombre) + " " + str(self.apellidos) + " sale del centro")