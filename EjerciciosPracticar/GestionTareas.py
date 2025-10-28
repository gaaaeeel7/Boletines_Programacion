lista_tareas = ["Matematicas", "Lengua", "Biologia", "Religion"]

otras_tareas = []

while True:
    print("1. Añadir Tarea")
    print ("2. Marcar Tarea completada")
    print ("3. Mostrar tareas pendientes")
    print ("4. Salir del programa")

    opcion = int(input("Elige la opcion que tu quieras:"))

    if opcion == 1:
        tarea = input("Añademe la tarea que tu quieras",)
        otras_tareas.append(tarea)
        print("Tareas actuales",otras_tareas)

    if opcion == 2:
        if otras_tareas:
            print("Tareas terminadas", otras_tareas)
        else:
            print("No hay tareas pendientes", otras_tareas)
    if opcion == 3:
        print ("Salir del programa")
        break


