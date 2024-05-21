def main():
    tasks = []
    while True:
        print("\nMenú de Lista de Tareas:")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            if not tasks:
                print("No hay tareas pendientes.")
            else:
                print("\nTareas pendientes:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
        elif option == "2":
            task = input("Ingrese la tarea que desea agregar: ")
            tasks.append(task)
            print("Tarea agregada.")
        elif option == "3":
            if not tasks:
                print("No hay tareas para eliminar.")
            else:
                print("\nTareas pendientes:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
                num = int(input("Ingrese el número de la tarea que desea eliminar: "))
                if 1 <= num <= len(tasks):
                    tarea_eliminada = tasks.pop(num - 1)
                    print(f"Tarea '{tarea_eliminada}' eliminada.")
                else:
                    print("Número inválido.")
        elif option == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Iniciar el programa
main()
