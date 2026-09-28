import os
os.system("cls")

velocidades=[45,80,65,110,55]

baja=[]
media=[]
alta=[]

for i in velocidades:      #i se va a volver todo lo que contiene velocidades
    if i<60:
        baja.append(i)    #guarda en la lista baja los datos indicados por el if anteriormente
    elif i>60 and i<100:
        media.append(i)
    elif i>100:
        alta.append(i)

print(f"las velocidades bajas son de {baja} \nlas velocidades medias son de {media} \nlas velocidades altas son de {alta} \n\nGracias.")