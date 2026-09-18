from src.cita import CitaMedica
from src.gestion_datos import cargar_citas, guardar_citas

RUTA_JSON = "data/citas.json"


def listar_citas(citas: list):
    print("\n" + "=" * 20)
    print("LISTADO DE CITAS MÉDICAS")
    if not citas:
        print("No hay citas registradas en el sistema.")
        return

    print(f"{'ID CITA':<12} | {'PACIENTE':<20} | {'ESPECIALIDAD':<18} | {'MÉDICO':<18} | {'URGENCIA':<8} | {'COSTO FINAL':<12}")
    print("-" * 95)
    for cita in citas:
        urgencia_txt = "Sí" if cita["es_urgencia"] else "No"
        costo_fmt = f"${cita['costo_final']:,.2f}"
        print(f"{cita['id_cita']:<12} | {cita['paciente']:<20} | {cita['especialidad']:<18} | {cita['medico_asignado']:<18} | {urgencia_txt:<8} | {costo_fmt:<12}")


def registrar_cita(citas: list):
    print("\n" + "=" * 20)
    print("REGISTRO DE NUEVA CITA MÉDICA")

    id_cita = input("Ingrese el ID de la cita (ej: CIT-2026-01): ").strip()
    for cita in citas:
        if cita["id_cita"] == id_cita:
            print("Error: Ya existe una cita registrada con este ID.")
            return

    paciente = input("Ingrese nombre completo del paciente: ").strip()
    especialidad = input("Ingrese especialidad médica: ").strip()
    medico_asignado = input("Ingrese nombre del médico asignado: ").strip()

    try:
        costo_consulta = float(input("Ingrese el costo de la consulta (COP): "))
    except ValueError:
        print("Error: El costo debe ser un valor numérico.")
        return

    urgencia_input = (input("¿Es una cita de urgencia? (s/n): ").strip().lower())
    es_urgencia = urgencia_input == "s"

    nueva_cita = CitaMedica(
        id_cita,
        paciente,
        especialidad,
        medico_asignado,
        costo_consulta,
        es_urgencia,
    )
    citas.append(nueva_cita.a_diccionario())

    if guardar_citas(RUTA_JSON, citas):
        print("Cita registrada y guardada exitosamente en el JSON.")


def calcular_ingresos_proyectados(citas: list):
    print("\n" + "=" * 20)
    total = sum(cita["costo_final"] for cita in citas)
    print(f"El total de ingresos proyectados es: ${total:,.2f} COP")


def main():
    citas = cargar_citas(RUTA_JSON)

    while True:
        print("\n" + "=" * 20)
        print("SISTEMA DE CITAS MÉDICAS MEDISENA")
        print("1. Listar citas")
        print("2. Registrar nueva cita")
        print("3. Consultar total de ingresos proyectados")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            listar_citas(citas)
        elif opcion == "2":
            registrar_cita(citas)
        elif opcion == "3":
            calcular_ingresos_proyectados(citas)
        elif opcion == "4":
            print("Saliendo del sistema. ¡Datos guardados correctamente!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()