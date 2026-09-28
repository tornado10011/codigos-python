import os
os.system("cls")

inventario=[("camisa",5), ("Pantalones",0), ("Zapatos",12)]

segundo_producto=inventario[1]
producto, cantidad=segundo_producto

if cantidad==0:
    print(f"esta agotado el producto {producto}")
else:
    print(f"todabvia tenemos {producto}")