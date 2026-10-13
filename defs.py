def suma(num1, num2):
    return num1+num2
def resta(num1, num2):
    return num1-num2
def multiplica(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1/num2


contador=0
while contador<=0:
    try:
        op1=int(input("Inserte el primer numero: "))
        op2=int(input("Inserte el segundo numero: "))
    except ValueError:
        print("lo digito mal, se reiniciara el programa")
        continue
    else:
        operacion=input("Que desea hacer? Digite el nombre de la operacion(suma, resta, multiplicacion, division: ")
        if operacion=="suma":
            print(suma(op1,op2))
            print ("operacion ejecutada")
        elif operacion=="resta":
            print(resta(op1,op2))
            print ("operacion ejecutada")
        elif operacion=="multiplicacion":
            print(multiplica(op1,op2))
            print ("operacion ejecutada")
            
        elif operacion=="division":
            try:
                print(divide(op1,op2))
                print ("operacion ejecutada")
            except ZeroDivisionError:
                print("error en la division")
        else:
            print("usted no escogio la opcion correcta")
        
        otra=str(input("\nQuiere repetir? (si,no): "))
        if otra=="si":
            continue
        else:
            print("Muchas gracias")
            contador+=1






