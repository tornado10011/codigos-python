import os
os.system("cls")


for i in range(2):

    produ = input("Escriba el nombre del producto: ")
    os.system("pause")
    os.system("cls")
    
    print(f"El producto a ingresar seria: {produ}")
    precio_produ = float(input("Digite el precio del producto: "))
    desc = int(input("Si tiene descuento presione 1. Si no tiene descuento presione 2: "))
    
    producto = (produ, precio_produ, desc)
    nombre, precio, tiene_descuento = producto

    if desc == 1:
        tiene_descuento = True
    else:
        tiene_descuento = False
    

    if tiene_descuento == True:
        descuento = precio * 0.15
        final = precio - descuento
        print(f"Su producto contiene un descuento de {descuento} del precio original")
        os.system("pause")
        os.system("cls")

        print(f"""        
Estimado cliente
El producto seria: {nombre}
Con un precio final de: {final}""")
        os.system("pause")   
        os.system("cls")   
            
    else:
        print("No tiene descuento, el precio se mantendra igual\n")
        print(f"""
Estimado cliente
El producto seria: {nombre}
Con un precio final de: {precio}""")
        os.system("pause")
        os.system("cls")



import os
os.system("cls")


calificaciones = (85, 90, 95) 

valor_1, valor_2, valor_3 = calificaciones
total = valor_1 + valor_2 + valor_3   #se suman los valores de la tupla ya definidos por el programa no por el usuario

buena_nota = 200

if total >= 270:
    print("excelentes calificaciones")
    os.system("pause")
    os.system("cls")
elif total >= 200 and total <= 269:
    print("buenas calificaciones")
    os.system("pause")
    os.system("cls")
elif total < 200:
    print("tiene una nota insuficiente")
    print(f"le faltan {buena_nota - total} puntos para una buena nota")
    os.system("pause")
    os.system("cls")

print(f"""
sus notas fueron de {valor_1}, {valor_2}, {valor_3}.
y obtuvo un total de {total}""")



import os
os.system("cls")

temperaturas = [22.5, 30.1, 18.4] 

fria = []
templada = []
calurosa = []

#aqui se clasifican las temperarutas de la lista primero
for temp in temperaturas:
    if temp < 20:
        fria.append(temp)
    elif temp >= 20 and temp <= 28:
        templada.append(temp)
    elif temp > 28:
        calurosa.append(temp)

contador = 1

# Luego pedimos las 4 nuevas temperaturas por teclado
for i in range(4):
    print("va a ingresar 4 veces diferentes temperaturas")
    print(f"va por la vez {contador}")
    contador += 1
    temp = float(input("digite las nuevas temperaturas: "))
    
    temperaturas.append(temp)
    
    # se califican las nuevas temperaturas
    if temp < 20:
        fria.append(temp)
    elif temp >= 20 and temp <= 28:
        templada.append(temp)
    elif temp > 28:
        calurosa.append(temp)

    os.system("pause")
    os.system("cls")

#saco promedio de las temperaturas
#aqui se usa el :.2f es para que se me pongan 2 digitos despues de la coma de la division de los promedios
promedio = sum(temperaturas) / len(temperaturas)

print(f"""
las temperaturas frias son de {fria} 
las temperaturas templadas son de {templada} 
las temperaturas calurosa son de {calurosa}

El promedio de las temperaturas es de {promedio:.2f}    
""")