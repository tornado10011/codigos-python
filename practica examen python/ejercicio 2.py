import os
os.system("cls")

memoria=[4,8,16,4,32]

memoria_baja=[]
memoria_adecuada=[]
memoria_alta=[]

for i in memoria:
    if i<8:
       memoria_baja.append(i)
    elif i>=8 and i<=16:
        memoria_adecuada.append(i)
    elif i>16:
        memoria_alta.append(i)

RAM_mayor= len(memoria_adecuada)+ len(memoria_alta)


print(f"""
las computadoras con memoria RAM baja tienen {memoria_baja}
las computadoras con memoria RAM adecuada tienen {memoria_adecuada}
las computadoras con memoria RAM alta tienen {memoria_alta}

la cantidad total de computadoras con mas de 8GB de ram son de {RAM_mayor}""")

