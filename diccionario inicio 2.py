diccionario={"juventus":"italia","barcelona":"españa"}
tupla=(1,2,3)

#diccionario={tupla[0]:"italia",tupla[1]:"españa",tupla[2]:"costa rica"}  
#print(len(diccionario))

#print(diccionario.keys())
#print(diccionario.values())

pais=(diccionario.get("juventus"))     #el get es para obtener algo del diccionario 
print(f"el pais donde juega la juventus es {pais}")

diccionario.pop("juventus")   #elimina una parte del diccionario
print(diccionario)

copydicc=diccionario.copy()  #es para copiar el diccionario completo
print(copydicc)

diccionario.clear()     #es para borrar el diccionario completo
print(diccionario)

