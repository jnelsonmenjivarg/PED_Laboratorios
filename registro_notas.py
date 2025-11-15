# Programa para registrar notas de estudiantes
# Autor: [Tu nombre]
# Universidad: [Tu universidad]

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Agregar estudiante")
    print("2. Agregar nota a estudiante")
    print("3. Mostrar registro completo")1
    print("4. Mostrar promedio de un estudiante")
    print("5. Salir")


def agregar_estudiante(registro):
    nombre = input("Nombre del estudiante: ").strip().capitalize()

    if nombre in registro:
        print(f"El estudiante {nombre} ya existe en el registro.")
    else:
        registro[nombre] = []
        print(f"Estudiante {nombre} agregado correctamente.")


def agregar_nota(registro):
    nombre = input("Nombre del estudiante: ").strip().capitalize()

    if nombre not in registro:
        print(f"El estudiante {nombre} no está registrado.")
        return

    if len(registro[nombre]) >= 5:
        print("Ya tiene el máximo de 5 notas registradas.")
        return

    try:
        nota = float(input("Ingrese la nota (0 - 10): "))
        if  nota > 0 and nota <= 10:
            registro[nombre].append(nota)
            print(f"Nota {nota} agregada a {nombre}.")
        else:
            print("La nota debe estar entre 0 y 10.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")


def mostrar_registro(registro):
    if not registro:
        print("No hay estudiantes registrados por el momento.")
        return

    for nombre, notas in registro.items():
        print(f"{nombre}: {notas}")


def mostrar_promedio(registro):
    nombre = input("Nombre estudiante: ").strip().capitalize()

    if nombre not in registro:
        print(f"El estudiante {nombre} no está registrado.")
        return

    notas = registro[nombre]
    if notas:
        promedio = sum(notas) / len(notas)
        print(f"Promedio de {nombre}: {promedio:.2f}")
    else:
        print(f"El alumno {nombre} aún no tiene notas registradas.")


def main():
    registro = {}

    while True:
        mostrar_menu()
        opcion = input("Elige la opción deseada: ")

        if opcion == "1":
            agregar_estudiante(registro)
        elif opcion == "2":
            agregar_nota(registro)
        elif opcion == "3":
            mostrar_registro(registro)
        elif opcion == "4":
            mostrar_promedio(registro)
        elif opcion == "5":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente otra.")


if __name__ == "__main__":
    main()
