lista_de_productos=["leche","pan","queso","naranja"]

nuevo_producto=input("indique un producto: ")

if nuevo_producto in lista_de_productos:
    print("no se puede guardar, ya existe el producto")
else:
    lista_de_productos.insert(len(lista_de_productos)//2,nuevo_producto)
    print(lista_de_productos," el producto se añadie correctamente")
    