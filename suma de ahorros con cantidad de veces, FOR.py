suma=0
contar=int(input("cuantas veces va a guardar sus ahorros: "))

for i in range(contar):
    ahorros=int(input("ingrese la cantidad de ahorros: \n"))
    suma=suma+ahorros
print(f"se sumo una cantidad de {suma}  {i} veces")  
