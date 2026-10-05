import random
import os

print("Bienvenido al juego :D")

def num_random():
    return random.randint(1,50)
ran=(num_random())
print(ran)

for i in range(5):
    integrado=int(input("indique un numero para ver si se acerca al numero random: "))

    if integrado==ran:
        print("adivinaste el numero :D")
        break
    else:
        print("No adivinaste.")

    if ran<integrado:
        print("es menor")
    elif ran>integrado:
        print("es mayor")

        
        


