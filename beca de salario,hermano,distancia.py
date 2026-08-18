print("salarios")

salario=300000
hermanos=5
distancia=20


pregsalario=int(input("de cuanto es su salario? "))
preghermanos=int(input("cuantos hermanos tiene? "))
pregdist=int(input("de cuanto es su distancia? "))


if pregsalario<salario and preghermanos<hermanos and pregdist<distancia:
    print("su beca fue aceptada")
else:
    print("su beca fue rechazada")