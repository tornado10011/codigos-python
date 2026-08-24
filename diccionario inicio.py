diccionario={"juventus":"italia","barcelona":"españa"}
tupla=("roma","madrid","san jose")

print(diccionario["barcelona"])

print(diccionario)

diccionario["saprissa"]=41         #si se pone texto va entre comillas, y si es numero normal
print(diccionario) 

diccionario["saprissa"]="san jose"
print(diccionario) 

diccionario["saprissa"]="el monstruo morado"         
print(diccionario) 

diccionario={tupla[0]:"italia",tupla[1]:"españa",tupla[2]:"costa rica"}   #asi se cambian valores especificos de diccionario, por los valores creados por la tupla
print(diccionario[tupla[1]])


newdiccionario={"tipos":{"hondo":"dulcetira","extendido":"jarron"}}
print(newdiccionario["tipos"])

