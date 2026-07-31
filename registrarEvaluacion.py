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

        fecha_input = input("Ingrese la fecha de calificación (DD-MM-AAAA) o presione Enter para la fecha actual: ").strip()
        
        if fecha_input: 
            try:
                fecha_obj = datetime.strptime(fecha_input, "%d-%m-%Y")
            except ValueError:
                raise ValueError("Error: Formato de fecha incorrecto. Debe ser DD-MM-AAAA (Ejemplo: 31-07-2026).")

            año_actual = datetime.now().year
            if fecha_obj.year < año_actual:
                raise ValueError(f"Error: La fecha ingresada no puede ser de un año anterior al actual ({año_actual}).")

            fecha_guardar = fecha_obj.strftime("%Y-%m-%d") 
        else:
            fecha_guardar = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        estudiantes[nombre] = {
            "calificacion": calificacion,
            "fecha": fecha_guardar
        }

        guardar_json("calificacion.json", estudiantes)
        
        print(f"Se ha registrado exitosamente la evaluación de '{nombre}'.")

    except ValueError as e:
        print(f"\n[X] {e}")