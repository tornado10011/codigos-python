print("factorial\n")

"""
factorial de un numero dado
la multiplicacion de 1 hasta ese numero
5f= 1*2*3*4*5
120

4f= 1*2*3*4
24

"""

factorial=1

facto=int(input("digite un numero a calcular el factorial: "))

for i in range(1,facto+1):   #aqui va del 1 hasta el numero indicado +1 para que cuente el numero que indico el usuario
    factorial=factorial*i

    print(factorial)



