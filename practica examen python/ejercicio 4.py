import os
os.system("cls")

numeros_positivos=[]

while True:
    num=int(input("Ingrese un digito: "))

    if num>=1:
        numeros_positivos.append(num)
        print(f"el numero {num} es positivo\n")

    if num==0:
        break

total=len(numeros_positivos)
print(f"la cantidad de numeros positivos que ingreso son el total de {total}")