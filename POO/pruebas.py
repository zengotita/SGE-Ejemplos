import personacentroed
import alumno
import profesor
import pas


per=personacentroed.Persona_Centroed(1,"Aloy", "Sobeck", 30)
print(per)
per.asistir_centro()
per.salir_centro()

print("".center(50,"#"))

alu=alumno.Alumno(2,"Ellie", "Williams", 23, "TL333")
print(alu)
alu.realizar_Examen()
alu.realizar_Practica()
alu.atiende()

print("#".center(50,"#"))

profe=profesor.Profesor(3, "Joel", "Miller", 50, "OU1709",["SGE", "BBDD", "SOM"])
print(profe)
profe.asistir_centro()
profe.salir_centro()
profe.corregir_Examen()
profe.impartir()
profe.preparar_Practica()

print("#".center(50,"#"))

pas=pas.PAS(4, "Ezio", "Auditore", 40, "AC01")
print(pas)
pas.asistir_centro()
pas.salir_centro()
pas.visualizar_incidencia()
pas.resolver_incidencia()

