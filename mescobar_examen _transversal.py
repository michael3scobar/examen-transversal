import csv
import random

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos = [500000,700000,1100000,800000,1500000]
matriz = []


def asignacion_sueldo(trabajadores,sueldos,matriz):
    for i in range(len(trabajadores)):
                   nombre = trabajadores[i]
                   sueldo = sueldos[i]
                   matriz.append(nombre, sueldos)
                   print ("nombre:", (nombre),"sueldo:", (sueldo))

def calificarsueldo(matriz):
    sueldos_menores = []
    sueldos_medios = []
    sueldos_superiores = []

    if sueldo < 800000:
        sueldos_menores.append(sueldo)
    if 800000 <= sueldo <2000000:
        sueldos_medios.append(sueldo)
    if sueldo > 2000000:
        sueldos_superiores.append(sueldo)

        
def cierre():
    print ("""Finalizando programa...\nDesarrollado por Michael Escobar\nRut 20.788.477-4""")
    

while True:
    opcion = str(input("""
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadísticas.
    4. Reporte de sueldos
    5. Subir Como archivo
    6. Salir del programa"""))

    match opcion:
        case "1":
            asignacion_sueldo(trabajadores,sueldo,matriz)
        case "2":
            claisificarsueldo(matriz)
        case "3":
            print()
        case "4":
            print()
        case "5":
            print()
        case "6":
            cierre()
            break
