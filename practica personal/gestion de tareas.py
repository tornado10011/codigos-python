import os
os.system("cls")


tareas = {
    "servidor": 1,
    "base de datos": 2,
    "interfaz": 3,
    "respaldo": 1
}

completadas = []

print("tareas pentiendes\n\n")

while True:

    opciones=int(input("""
presione 1 su quiere ver todas las tareas penteindes
presione 2 si quiere agregar una nueva tarea
presione 3 si quiere marcar tarea como completada
presione 4 si quiere ver un resumen
presione 5 si quiere ver historial de tareas completas
presione 6 si quiere salir del programa

digite aqui su opcion: \n"""))

    if opciones==1:
        os.system("cls")
        for tarea, prioridad in tareas.items():
            if prioridad == 1 :
                print(f"tarea: {tarea} con prioridad alta")
            elif prioridad == 2:
                print(f"tarea: {tarea} con prioridad medio")
            elif prioridad == 3:
                    print(f"tarea: {tarea} con prioridad baja")
            else:
                len(tareas)== 0
                print("no hay tareas pendientes")
        os.system("pause")
        os.system("cls")

    if opciones==2:
        nueva_tarea=input("escriba el nombre de la nueva tarea: ")
        if nueva_tarea ==tareas:
              print("ya existe esa tarea")
              os.system("pause")
              os.system("cls")
        else:
            prioridad=int(input("digite del 1 al 3 la prioridad de la tarea: "))
            tareas[nueva_tarea]=prioridad
            os.system("pause")
            os.system("cls")

    if opciones==3:
        print(f" estas son las tareas disponibles: {tareas.keys()}\n\n")
        tarea_completada=input("digite el nombre de la tarea completada: ")
        if tarea_completada in tareas:
            tareas.pop(tarea_completada)
            completadas.append(tarea_completada)
            print(f"la tarea paso a completada, a continuacion se mostrara la lista de las tareas completadas\n\n {completadas}")
            os.system("pause")
            os.system("cls")
        else:
            print("la tarea no fue encontrada")
            os.system("pause")
            os.system("cls")

    if opciones==4:
        contador=0
        for prioridad in tareas.values():
            if prioridad ==1:
              contador=contador+1

        print(f"""la cantidad de tareas pentientes en total es de {len(tareas)}
la cantidada de tareas completadas es de {len(completadas)}
la cantidad de tareas urgentes con prioridad alta es de {contador}""")
        os.system("pause")
        os.system("cls")

    if opciones==5:
        if len(completadas) >0:
            for i in completadas:
                print(i)
        else:
            print("no se a completado nignuna tarea")
        os.system("pause")
        os.system("cls")

    if opciones== 6:
        print("a continuacion se finalizara el programa")
        os.system("pause")
        break