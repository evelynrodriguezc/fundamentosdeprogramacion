'''Mini Proyecto: Gestor de Tareas
Objetivo:
Crear una aplicación de consola que permita al usuario gestionar una lista de tareas. 
El usuario podrá añadir tareas, ver la lista de tareas, ordenarlas por prioridad, y eliminar tareas completadas.
Funcionalidades:
Añadir Tarea: Permite al usuario añadir una nueva tarea con una descripción y una prioridad.
Mostrar Tareas: Muestra todas las tareas actuales.
Ordenar Tareas: Ordena las tareas por su prioridad.
Eliminar Tarea: Permite al usuario eliminar una tarea completada.
Estructura del Proyecto:
La lista de tareas será una lista de diccionarios, donde cada diccionario representará una tarea con una descripción 
y una prioridad.
'''

def agregar_tareas(tareas):
    print("\n--------- Agregar tarea ---------")
    descripcion = input("Ingresa la descripción de la tarea: ")
    prioridad = int(input("Ingrese la prioridad de la tarea ([más baja]:1 - 5:[más alta]): "))
    tarea = {"descripcion": descripcion, "prioridad": prioridad}
    tareas.append(tarea)
    print("\nTarea agregada con éxito\n")

def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas para mostrar")
    else:
        tareas.sort(key=lambda x: x["prioridad"])
        i = 1
        print("\nTAREAS")
        for tarea in tareas:
            print(f"{i}. {tarea['descripcion']} - Prioridad: {tarea['prioridad']}")
            i += 1
            

def eliminar_tareas(tareas):
    pass

#Sistema de gestión
def menu():
    tareas = [{"descripcion":"Programar ciclos", "prioridad": 5},
            {"descripcion":"Programar condicinales", "prioridad": 3},
            {"descripcion":"Programar variables", "prioridad": 2}]
    
    while True:
        print("\nGESTIÓN DE TAREAS")
        print("1. Agregar Tareas")
        print("2. Mostrar Tareas")
        print("3. Eliminar Tarea(s)")
        print("4. Salir")
        opcion = input("\nElija una opción: ")
        
        if opcion == "1":
            agregar_tareas(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            pass
        elif opcion == "4":
            print("\nSaliendo del gestor de tareas...")
            break
        else: 
            print("\nOpción invalida. Intente de nuevo\n")
        
menu()