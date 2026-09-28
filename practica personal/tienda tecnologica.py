import os
os.system("cls")

componentes = {
    "ram": 25000,
    "ssd": 30000,
    "tarjeta de video": 180000,
    "procesador": 120000
}

carrito = []
precios_carrito = []

suma=0

while True:
    print("bienvenido")
    print(f"""
ahora mismo tenemos estos componentes
{componentes.keys()}
con un precio cada uno de 
{componentes.values()}""")

    opcion=int(input("""presione 1 si quiere añadir un articulo al carrito
presione 2 si quiere ver el carrito y el total acumulado 
presione 3 si quiere devolver el ultimo articulo agregado a su carrito 
presione 4 si quiere aplicar un cupon de descuento
presione 5 si quiere salir de la tienda.\n\ndigite que desea realizar: """))

    if opcion== 1:
    
        compra=input("escriba a continuacion lo que desea comprar de la lista anterior: ")
        if compra.lower() in componentes:
            carrito.append(compra)
            precio=componentes.get(compra)
            suma=suma+precio
            precios_carrito.append(precio)

            print(f"Se ah añadido el producto {compra} a su carrito. \nActualmente tienes {len(carrito)} articulos en el carrito.")
            os.system("pause")
            os.system("cls")
        else:
            print("producto no encontrado en el catalogo")
            os.system("pause")
            os.system("cls")
    
    elif opcion==2:
        print("a continuacion se visualizara lo que contenga el carrito.")
        print(f"""esta lista es lo que contiene su carrito
{carrito}
y el precio total de {suma}""")
        os.system("pause")
        os.system("cls")

    elif opcion==3:
        
        if (len(carrito)>0):
            print(" a continuacion se eliminara el ultimo producto agregado a el carrito")
            carrito.pop()
            precios_carrito.pop()
            print(f"el carrito ahora mismo contiene {carrito}")
            os.system("pause")
            os.system("cls")
        else:
            print("el carrito no tiene nada")
            os.system("pause")
            os.system("cls")
    
    elif opcion==4:
        codigo=input("Digite el codigo de descuento: ")
        if codigo=="DESCUENTO10":
            print("tiene un descuento de 10% en su compra")
            os.system("pause")
            os.system("cls")
        else:
            print("codigo erroneo")
            os.system("pause")
            os.system("cls")
    elif opcion==5:
        print("a continuacion saldra de la tienda digital")
        os.system("pause")
        os.system("cls")
        break
    elif opcion<1 and opcion>5:
        print("usted no indico que desea realizar correctamente")
        os.system("pause")
        os.system("cls")


