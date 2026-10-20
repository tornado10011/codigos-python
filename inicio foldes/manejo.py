import os

###importante
# r se usa para leer y guardarlo en una variables
# w me crea y edita
# a me añade sin borrar nada al final
# strip() quita espacio despues de una palabra 



print("esto es de manejo de archivos")

"""

archivo=open("archivo.txt", "r")   #se pone el nombre del archivo con el txt, y el r es para leerlo y que se guarde en la variable todo lo que esta en ese archivo 
print(archivo.read())  #se pone el read para que se logre mostrar lo que se guardo anteriormente
archivo.close()  #se cierra el archivo para que no se modifique nada mas 


"""


"""
archivo=open("inventario.txt", "w", encoding="utf-8")  #se pone la "w" porque va a crear un archivo y va a editarlo 
#encoding="utf-8"... se usa para que se me guarden las tildes o comillas o la ñ o caracteres diferentes y no me de un error o algo similar
archivo.write("tarjeta_de_video \n")  #aqui se usa para escribir en el archivo nuevo los siguientes datos
archivo.write("ram_soddim \n")
archivo.write("procesador \n")
archivo.close()
"""


#si no se tiene cuidado se puede borrar lo que hizo antes y borrar y poner lo de ahora 


"""
with open ("inventario.txt","a",encoding="utf-8") as inventario:   #esta es una forma de hacer lo de arriba pero mas facil y se cierra solo
    inventario.write("silla_gamer \n")
    inventario.write("pasta_termica \n")

"""


"""
#aqui lo estoy leyendo y creando una variables para guardar todo lo que esta en ese txt
with open ("archivo.txt","r",encoding="utf-8") as inventario:
    contenido=inventario.read() 

print(contenido)

"""

"""
with open ("archivo.txt","r",encoding="utf-8") as inventario:
    for linea in inventario:
        print(linea.split()) 

"""

"""
#esto siguiente es para crear un txt nuevo y ir agregando usuarios o datos que ingrese el usuario 
nombre=str(input("Digite el nombre de usuario: "))

with open ("usuarios.txt", "a", encoding="utf-8") as inventario:
    inventario.write(nombre + "\n")

print("usuario guardado correctamente ")

"""

"""
#este de aqui es ara guardar los datos de precios de un usuario en un archivo txt y pasarlo a float si fuera un str en la pregunta del precio
# tambien funciona para sacarle el impuesto con 2 decimales  
while True:

    precios=str(input("ingrese los precios de sus productos: "))

    with open ("precios.txt", "a", encoding="utf-8") as inventario:
        inventario.write(precios + "\n")

    print("\nprecio guardado correctamente")
    

    otra_vez=int(input("\ndigite 1 si quiere agregar otro precio \ndigite 2 si no quiere agregar mas \nDigite aqui:"))

    if otra_vez==1:
        #prueba echa en otro sistema operativo pero es lo mismo que el cls
        os.system("clear")
        continue
    elif otra_vez==2:
        print("Muchas gracias")
        break


with open ("precios.txt", "r", encoding="utf-8") as inventario:
    for linea in inventario:
        precio=float(linea.strip())
        print(f"\nEl precio base es de {precio:.0f} con impuesto es {precio*1.13:.2f}")

"""

"""
with open ("inventario.txt", "r", encoding="utf-8") as inventario:
    for linea in inventario:
        datos=linea.strip().split(",")
        nombre= datos[0]
        precio=float(datos[1])
        print(f"\nProducto: {nombre"}
        print(f"Precio: {precio}")

"""
"""
try:
    with open("inventario.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe. Verifique el nombre y la ubicación.")
"""


"""
#me crea un archivo vacio 
f=open("pruebas1.txt","x")
"""

#se elimina el archivo creado
if os.path.exists("pruebas1.txt"):
    os.remove("pruebas1")
else:
    print("the file does not exits. el archivo no existe")
