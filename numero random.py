def invalid():
   print("Valor inválido, redigite el valor correctamente")
def total(precio1, precio2):
   suma = precio1 + precio2 
   print("El total de los dos productos es:", suma)
def supermercado():
   print("Bienvenido al Super Mario")
   nom = input("Me podría otorgar su nombre: \n")
   print(f"Bienvenido {nom}")
   lista = ["leche", "leche de chocolate", "queso crema","harina de maiz", "harina de trigo", "zanahoria","camote", "lechuga", "mango", "fresa", "sandia"]
   precio = [500, 200, 300, 400, 250, 340, 110, 900, 700, 400, 500]
   dicc = {  "lacteos": ["leche", "leche de chocolate", "queso crema"],"harinas": ["harina de maiz", "harina de trigo"],"verduras": ["zanahoria", "camote", "lechuga"],"frutas": ["mango", "fresa", "sandia"]}
   precios_comprados = []
   for i in range(2):
       print("Apartados disponibles:\n")
       print("1. Lacteos")
       print("2. Harinas")
       print("3. Verduras")
       print("4. Frutas")
       busqueda = int(input("Digite el número del apartado:\n"))
       if busqueda == 1:
           apartado = "lacteos"
       elif busqueda == 2:
           apartado = "harinas"
       elif busqueda == 3:
           apartado = "verduras"
       elif busqueda == 4:
           apartado = "frutas"
       else:
           invalid()
           return
       print("Productos disponibles:", dicc[apartado])
       producto = input("Digite el producto que desea comprar:\n")
       if producto in lista:
           posicion = lista.index(producto)
           precio_producto = precio[posicion]
           print("Producto:", producto)
           print("Precio:", precio_producto)
       else:
           print("Este producto no está en la lista")
           precio_producto = int(input("Digite el precio del producto:\n"))
           lista.append(producto)
           precio.append(precio_producto)
           dicc[apartado].append(producto)
           print("Producto agregado correctamente")
       precios_comprados.append(precio_producto)
   total(precios_comprados[0], precios_comprados[1],precios_comprados[2])
supermercado()
        
        


