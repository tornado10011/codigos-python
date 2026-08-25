lista_de_productos=["leche","pan","queso","naranja"]
precios=[1500,2000,3500,500]

nuevos_ligares={}

diccionario_provi={"0":"barcelona","1":"buenos aires","2":"madrid","3":"heredia"}   #este diccionario es donde se va a mostrar los lugares donde estan disponible los articulos

nuev_list=[]   #aqui creo una nueva lista para guardar los nuevos productos
nuev_preci=[]   #aqui creo una nueva lista para guardar los nuevos productos
nuevo_producto=input("indique un producto: ")      #le pregunto que indique un producto

if nuevo_producto in lista_de_productos:
    posicion=lista_de_productos.index(nuevo_producto)    #aqui busco donde esta ubicado ese producto que ya esta en la lista
    precip=precios[posicion]    #aqui le indico que X precio va a ser el del producto de la posicion X

    print("donde desea comprar?")
    print(diccionario_provi)

    where=input("indique el lugar en el cual desea comprar: ")
    lugar=diccionario_provi.get(where)
    
    print(f"ya existe el producto {nuevo_producto} con un precio de {precip}")
    print(f"existe en", {lugar},) 
    
else:
   
    nuev_list.append(nuevo_producto)   #se coloca el producto que indico el usuario al final de la nueva lista
    tuplistnu=tuple(nuev_list)         #se convierte en tupla
    
    nuevo_precio=int(input(f"indique el precio para el articulo {nuevo_producto}: "))
    nuev_preci.append(nuevo_precio)   #se coloca el precio que indico el usuario al final de la nueva lista
    precitup=tuple(nuev_preci)         #se convierte en tupla

    lug=input("donde quiere guardar el nuevo producto: ") #aqui es donde pregunta donde va a guardar el producto
    lugs=list(nuevos_ligares)
    lugs.insert(0, lug)

    print(f"para el nuevo articulo; {tuplistnu} el precio seria de {precitup}")
    print(f"se guardara en, {lugs}")
    