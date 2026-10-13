import os
import random

#sistema
contador=0
numeros_comprados=[]
serie_comprada=[]

#usuario
numero_usuario=[]
serie_user=[]

#si sale bolita roja hay acumulado osea para el primer premio se multiplica x3, si es blanca queda todo normal
#bolita_roja=1
#bolita_blanca=2


#premios
premio_mayor=10000000
segundo_premio=5000000
tercer_premio=2000000


#aqui genero un numero random que me va a generar un numero para generar los numeros comprados
def aleatorio():
    numero=random.randint(1,15)
    return numero

#aqui defino el numero que se va a generar para guardarlo como comprado dependiendo de la cantidad de numeros vendidos anteriormente
def numero():
    numero=random.randint(1,100)
    return numero
for i in range(aleatorio()):
    numeros_comprados.append(numero())
    
#aqui defino para el #serie
def serie():
    serie=random.randint(100,300)
    return serie
for i in range(aleatorio()):
    serie_comprada.append(serie())

def bolita():
    bolita=random.randint(1,2)
    return bolita


while contador==0:
    try:
        num_usuario=int(input(f"""
los numeros comprados son {numeros_comprados}
que numero desea comprar? :"""))

        if num_usuario in numeros_comprados:
            print("se intento comprar un numero que ya estaba comprado, se reiniciara el sistema.")
            os.system("pause")
            os.system("cls")
            continue
    except ValueError:
        print("se produjo un error. se reiniciara el sistema")
        os.system("pause")
        os.system("cls")
        continue
    else:
        numero_usuario.append(num_usuario)
        print(f"se compro correctamente el numero {numero_usuario}")
        os.system("pause")
        os.system("cls")
        while contador==0:
            try:
                serie_usuario=int(input(f""" las series compradas son: {serie_comprada}
escoja que serie quiere comprar que no este en la lista: """))
                if serie_usuario in serie_comprada:
                    print("se intento comprar una serie que ya estaba comprado, se reiniciara el sistema.")
                    os.system("pause")
                    os.system("cls")
                    continue
            except ValueError:
                print("se produjo un error. se reiniciara el sistema")
                os.system("pause")
                os.system("cls")
                continue
            else:
                serie_user.append(serie_usuario)
                print(f"se compro correctamente el numero {serie_user}")
                os.system("pause")
                os.system("cls")

                if bolita==1: 
                    premio_mayor*=3
                else:
                    print(f"""
---RIFA---

""")


                
            
            
    


        

            
    





"""
print(numeros_comprados)
print(serie_comprada)
"""