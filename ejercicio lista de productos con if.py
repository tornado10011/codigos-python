lista_de_productos=["leche","pan","queso","naranja"]
precios=[1500,2000,3500,500]

nuevo_producto=input("indique un producto: ")      #le pregunto que indique un producto

if nuevo_producto in lista_de_productos:
    posicion=lista_de_productos.index(nuevo_producto)    #aqui busco donde esta ubicado ese producto que ya esta en la lista
    precip=precios[posicion]    #aqui le indico que X precio va a ser el del producto de la posicion X
    print(f"ya existe el producto {nuevo_producto} con un precio de {precip}")
else:

    nuev_list=[]   #aqui creo una nueva lista para guardar los nuevos productos
    nuev_list.append(nuevo_producto)   #se coloca el producto que indico el usuario al final de la nueva lista
    tuplistnu=tuple(nuev_list)         #se convierte en tupla

    nuevopreci=()
    nuevo_precio=int(input(f"indique el precio para el articulo {nuevo_producto}: " ))   #aqui indica el precio para el neuvo producto
    nuevopreci12=list(nuevopreci)
    nuevopreci12.append(nuevo_precio)  #Aqui se guardara el precio del nuevo articulo
    nuevopreci=tuple(nuevopreci12)   #aqui la convierto en tupla 

    print(f"para el nuevo articulo; {nuevo_producto} el precio seria de {nuevopreci}\n")

    
    