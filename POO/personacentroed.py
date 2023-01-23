class Persona_Centroed():
    def __init__(self, id, nombre, apellidos, edad):
        self.id=id
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad

    #GETTERS
    def getId(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getEdad(self):
        return self.edad

    #SETTERS
    def setId(self,id):
        self.id=id
    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def setEdad(self, edad):
        self.id = id

    #FUNCIÓN STR
    def __str__(self):
        return ("Datos de la persona: \n" + "- Nombre: " + str(self.nombre) + "\n" + "- Apellidos: "
                + str(self.apellidos) + "\n" + "- Edad: " + str(self.edad))

    #OTRAS FUNCIONES
    def asistir_centro(self):
        print("La persona " + str(self.nombre) + " " + str(self.apellidos) + " asiste al centro")

    def salir_centro(self):
        print("La persona " + str(self.nombre) + " " + str(self.apellidos) + " sale del centro")


if __name__=="__main__":
    p=Persona_Centroed(1,"eee", "ap1 ap2", 30)
    print(p)