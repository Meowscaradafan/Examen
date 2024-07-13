import random
import csv

trabajadores = [
    {"nombre": "Juan Pérez", },
    {"nombre": "María García", },
    {"nombre": "Carlos López", },
    {"nombre": "Ana Martínez", },
    {"nombre": "Pedro Rodríguez",},
    {"nombre": "Laura Hernández", },
    {"nombre": "Miguel Sánchez", },
    {"nombre": "Isabel Gómez", },
    {"nombre": "Francisco Díaz", },
    {"nombre": "Elena Fernández", }
]

def sueldosrandom(trabajadores):
    for trabajador in trabajadores:
        trabajador["sueldo"] = random.randint(300000, 2500000)

def clasificacionsueldo(trabajadores):
    clasificacion = {"Sueldos menores a $800.000": [], "Sueldos entre $800.000 - $2.000.000": [], "Sueldos arriba de $2.000.000": []}
    for trabajador in trabajadores:
        sueldo = trabajador["sueldo"]
        if sueldo < 800000:
            clasificacion["Sueldos menores a $800.000"].append(trabajador)
        elif sueldo <= 2000000:
            clasificacion["Sueldos entre $800.000 - $2.000.000"].append(trabajador)
        else:
            clasificacion["Sueldos arriba de $2.000.000"].append(trabajador)
    for rango, lista in clasificacion.items():
        print(f"{rango}:")
        for trabajador in lista:
           print(f"  {trabajador['nombre']} ${trabajador['sueldo']:,.0f}")
        print()

def reportedesueldos(trabajadores):
    with open('reportedesueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for trabajador in trabajadores:
            sueldo_base = trabajador["sueldo"]
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
            writer.writerow([trabajador["nombre"], f"${sueldo_base:,.0f}", f"${descuento_salud:,.0f}", f"${descuento_afp:,.0f}", f"${sueldo_liquido:,.0f}"])

    print("Reporte generado como reportesueldos.csv")
def estadisticas():
    estadisticas = 
def menu():
    while True:
        print("\n***** Menú *****\n")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sueldosrandom(trabajadores)
            print("\nSueldos asignados aleatoriamente.")
        elif opcion == "2":
            clasificacionsueldo(trabajadores)
        elif opcion == "3":
            print("\nEstadisticas")
            print("sueldos mas al")
        elif opcion == "4":
            reportedesueldos(trabajadores)
        elif opcion == "5":
            print("\nFinalizando programa...")
            print("Desarrollado por Lucas Paillafil Arancibia")
            print("RUT 21055579-k")
            break
        else:
            print("Valor no valido")   
            
menu()            