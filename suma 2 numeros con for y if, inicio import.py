import os
os.system("cls")
total=0

mayor_que_67=() #tupla para las sumas mayores a 67
menor_que_67=[] #lista para las sumas menores a 67

for i in range(6):    #aqui me indica que se realizara lo que esta dentro 6 veces
   
   num1=int(input("digite su primer numero: "))    #los siguientes 2 comandos son para q  ue el usuario ingrese los numeros
   num2=int(input("digite su segundo numero: "))
   suma=num1+num2    #aqui se suman los numeros ingresados por el usuario

   print(f"\nla suma es igual a {suma} \n")
   
   total=suma+total
   print(f"llevamos un total de {total}\n")
   
   if suma>67:   #el if me dice que si la suma es mayor a 67 va a hacer lo siguiente
      lista_mayor=list(mayor_que_67)    #convierto la tupla a lista porque no se puede ingresar datos en una tupla
      lista_mayor.append(suma,)         #ingreso la suma en la lista convertida anteriormente
      mayor_que_67=tuple(lista_mayor)   #convierto la lista a tupla como estaba desde un comienzo
   else:
        menor_que_67.append(suma)       #ingreso la suma en la lista menor que 67

   if  i == 2 and total>67:     #este if lo que hace es contar las primeras 3 sumas y ver si el total es mayor a 67 realizar lo siguiente
         print("Bienvenido")
         print(f"las sumas mayores a 67 serian {mayor_que_67}")
         print(f"las sumas menores a 67 serian {menor_que_67}\n")
         print("programa finalizado")
         break      #aqui se finaliza el programa si se cumple la condicion del if

   print(f"las sumas mayores a 67 serian {mayor_que_67}")
   print(f"las sumas menores a 67 serian {menor_que_67}\n")
   os.system("\n""pause")
   os.system("cls")
      



