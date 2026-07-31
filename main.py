from registrarEvaluacion import registrarEvaluacion,consultarEvaluacion,calcularPromedio()



while True:
        try:
            print("\n==============================================================")
            print("          DRIVESAFE --- SISTEMA DE CALIFICACION")
            print("==============================================================")
            print("Bienvenido al menu, ¿que deseas realizar el dia de hoy?:")
            print("Ingrese '1' para registrar estudiante y calificacion")
            print("Ingrese '2' para consultar evaluacion por estudiante")
            print("Ingrese '3' para calcular promedio general")
            print("Ingrese '4' para cerrar sesion")
            alter = int(input("Ingrese un numero para seleccionar una opcion: "))
            if alter == 4: 
                print("==============================================================")
                print("                      Hasta pronto"                            )
                print("==============================================================")
                break
            if alter == 1:
                registrarEvaluacion()
            if alter == 2:
                consultarEvaluacion()
            if alter == 3:
                calcularPromedio()
        except ValueError:
            print("\n==============================================================")
            print("No se ha podido registrar la opcion,ingrese un numero entero")
            print("================================================================")
