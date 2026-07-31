from cargarDatos import cargar_json, guardar_json
from datetime import datetime

def registrarEvaluacion():
    try:
        print("\n--- Registrar evaluación del estudiante ---")
         
        estudiantes = cargar_json("calificacion.json", {})
        
        if not isinstance(estudiantes, dict):
            estudiantes = {}

        nombre = input("Ingrese nombre del estudiante: ").strip().upper()

        if not nombre:
            raise ValueError("Error: El nombre no puede estar vacío.")

        if not nombre.replace(" ", "").isalpha():
            raise ValueError("Error: El nombre solo puede contener letras y espacios.")

        try:
            calificacion = float(input("Ingrese la calificación (0-100): ").strip())
        except ValueError:
            raise ValueError("Error: Debe ingresar un número válido.")

        if calificacion < 0 or calificacion > 100:
            raise ValueError("Error: La calificación debe estar entre 0 y 100.")

        estudiantes[nombre] = {
            "calificacion": calificacion,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        guardar_json("calificacion.json", estudiantes)
        
        print(f"Se ha registrado exitosamente la evaluación de '{nombre}'.")

    except ValueError as e:
        print(f"\n[X] {e}")


def consultarEvaluacion():
    print("\n--- Consulta de evaluación por estudiante ---")
    estudiantes = cargar_json("calificacion.json", {})
    
    if not estudiantes:
        print("Actualmente no hay estudiantes registrados en el sistema.")
        return

    consulta = input("Ingrese el nombre del estudiante para la evaluación: ").strip().upper()
    
    if consulta in estudiantes:
        datos = estudiantes[consulta]
        print("\n==============================================================")
        print(f"Estudiante: {consulta}")
        print(f"Calificación: {datos['calificacion']}")
        print(f"Fecha de registro: {datos['fecha']}")
        print("==============================================================")
    else:
        print(f"\n[X] Error: El estudiante '{consulta}' no fue encontrado.")


def calcularPromedio():
    print("\n--- Promedio General ---")
    estudiantes = cargar_json("calificacion.json", {})
    
    if not estudiantes:
        print("Actualmente no hay calificaciones para calcular el promedio.")
        return
        
    calificaciones = [datos["calificacion"] for datos in estudiantes.values()]
    
    promedio = sum(calificaciones) / len(calificaciones)
    
    print("\n==============================================================")
    print(f"Total de estudiantes evaluados: {len(calificaciones)}")
    print(f"Promedio general: {promedio:.2f}")
    print("==============================================================")
