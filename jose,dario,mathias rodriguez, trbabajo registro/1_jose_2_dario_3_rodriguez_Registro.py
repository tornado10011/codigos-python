import os
import random

pasaron=[]
quedados=[]

def pasa():
    print(f"""
los estudiantes que pasaron son de {pasaron} 
y los estudiantes que no pasaron son de {quedados}""")
    os.system("pause")
    os.system("cls")
    return pasa

estudiantes={"dario":0,
"rodri":0,
"leo":0,
"lucia":0,
"daniel":0,
"miguel":0,
"shanti":0,
"dylan":0,
"allison V":0,
"veronica":0,
"allison F":0,
"moreno":0,
"monkey":0,
"jefferson":0,
"jose":0}



os.system("cls")

while True:
    try:
        empezar=int(input("""
BIENVENIDO
presione 1 si quiere empezar a registrar los datos del estudiante
presione 2 si quiere ver el registro
presione 3 si quiere ver quienes pasaron o no
presione 4 si quiere guardar el registro
presione 5 si quiere salir del programa
        
    digite: """))
        os.system("cls")

        if empezar==1:
            for i in range(len(estudiantes)):
                print("""---BIENVENIDO AL SISTEMA DE ESTUDIANTES---
                los siguientes estudiantes son los que puede escoger:""")
                print(estudiantes.keys())
                os.system("pause")

                print("si quiere salir de este proceso escriba ""salir""")
                estu=input("digite el nombre del estudiante con el que desea trabajar: ")

                if estu in estudiantes:
                    try:
                        while True:
                            trabajo=float(input(f"indique el trabajo cotidiano (max:25%) de {estu}: "))
                            if trabajo<0 or trabajo>25:
                                print("indico un valor incorrecta, vuelva a intentarlo")
                                
                            else:
                                break
                            
                        while True:
                            examen=float(input(f"indique los examenes (max: 45%) de {estu}: "))
                            if examen<0 or examen>45:
                                print("indico un valor incorrecta, vuelva a intentarlo")
                            else:
                                break  

                        while True:
                            asistencia=float(input(f"indique la asistencia (max: 5%) de {estu}: "))
                            if asistencia<0 or asistencia>5:
                                print("indico un valor incorrecta, vuelva a intentarlo")
                            else:
                                break

                        while True:
                            tareas=float(input(f"indique el valor de las tareas (max: 10%) de {estu}: "))
                            if tareas<0 or tareas>10:
                                print("indico un valor incorrecta, vuelva a intentarlo")
                            else:
                                break

                        while True:
                            proyecto=float(input(f"indique el valor del proyecto (max: 15%) de {estu}: "))
                            if proyecto<0 or proyecto>15:
                                print("indico un valor incorrecta, vuelva a intentarlo")
                            else:
                                break

                        promedio=(trabajo+examen+asistencia+tareas+proyecto)
                        estudiantes[estu]=promedio

                        print(f"el estudiante {estu} tiene un promedio total de {promedio}")
                        
                        
                        #print(estudiantes)
                        if promedio<70:
                            quedados.append(estu)
                        elif promedio>70:
                            pasaron.append(estu)
                        os.system("pause")
                        
                        print("presione alguna tecla para seguir con el siguiente estudiante")
                        os.system("cls")
                    except (TypeError, ValueError):
                        print("esta indicando valores que no son correctos, se empezara desde 0 intente de nuevo")
                        os.system("pause")
                        os.system("cls")
                        continue

                elif estu=="salir":
                    os.system("pause")
                    os.system("cls")
                    break
                else:
                    print("no indico el estudiante correctamente")
                    continue
        elif empezar==2:
            try:

                with open ("registro.txt", "r", encoding="utf-8") as historial:
                    print(historial.read())
                os.system("pause")
                os.system("cls")
                continue
            except FileNotFoundError:
                print("el archivo no existe, intente de nuevo")
                os.system("pause")
                os.system("cls")
                continue

        elif empezar==3:
            pasa()

        elif empezar==4:
            try:
                with open ("registro.txt", "a", encoding="utf-8") as historial:
                    historial.write("\n===== REGISTRO DE ESTUDIANTES =====\n")
                    for estu, promedio in estudiantes.items():                
                        historial.write(f"\nEstudiante: {estu} Promedio Final: {promedio}")                    
            except FileNotFoundError:
                print("no hay ningun registro o no se ah guardado nada")
            print("se guardo correctamente el archivo")
            os.system("pause")
            os.system("cls")

        elif empezar==5:
            print("gracias por utilizar el programa")
            break
        elif empezar<0 or empezar>5:
            print("no indico que desea realizar correctamente")
            os.system("pause")
            os.system("cls")

    except (TypeError, ValueError):
        print("indico algun valor mal")
        os.system("pause")
        os.system("cls")



        





