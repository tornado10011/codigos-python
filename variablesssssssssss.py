materias=["español","matematicas","ciencias"]

materia=str(input("digite su materia: "))

busqueda= materia.lower()
print(busqueda)


if busqueda in materias[:]:                       # los 2 puntos [:] del if es para que busque en todo la lista, no algo especifico ni nada en un rango
    print("la materia buscada si se encuentra")
else:
    print("la materia buscada no se encuentra, se añadira a la lista:\n")
    
    materias.append(busqueda)
   # print(materias)

    busqueda=materia.upper()
    materias.insert(0,busqueda)
    print(materias)