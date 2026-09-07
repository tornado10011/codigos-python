print("tuplas \n")

precios=(10000,20000,50000,20000,20000,20000,20000)  #tupla

articulos=["camisa","pantalones","saco","vestido","vestido","vestido","vestido"]    #listas

print(f"la tupla contiene estos valores: {precios}" )
#print(precios[2])

precioslista=list(precios)   #el comando lista pasa una tupla a lista
precioslista.insert(3,42500)
#print(precioslista)

esta=(20000 in precios)
print(esta)

print(precios.count(20000))     #se usa para contar  cuantos ahi de ese valor que le esta indicando en una lista
print(articulos.count("vestido"))
print(f"la tupla contiene la cantidad de elementos: {len(precios)}")

precios=tuple(precioslista)  #
print(f"la tupla actualizada contiene estos valores {precios}" )




datos=(18,"diciembre",1000000)

edad,mes,salario=datos

print(f"""la edad de la persona es: {edad}
cumple años en el mes de: {mes}
y le dieron de regalo: {salario} colones
""")