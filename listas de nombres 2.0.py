alumnos10_3=["thamara","mathias","allison","dario","leonardo","veronica"]
alumnos10_4=[1,2,3,4,5,6]


print(alumnos10_3)
print(alumnos10_4)

print(alumnos10_3[3])   #para indicar de la lista que posicion se quiere mostrar, siempre empezara de 0
print(alumnos10_4[3])

print(alumnos10_4[-3])  #para traer lo que esta desde la derecha hacia la izquierda

print(alumnos10_4[0:3]) #para mostrar varias cosas especificas de la lista de un numero a otro
print(alumnos10_3[0:2])
print(alumnos10_3[:3])

alumnos10_3.append("derek") # para poner un nuevo dato en lo ultimo de la lista

print(alumnos10_3)

alumnos10_3.insert(2,"miguel") # ingrese un nuevo dato en un lugar especifico de la lista

print(alumnos10_3)

alumnos10_3.extend(["dylan", "valeska", "lucia","rogelio"]) #expande la lista con varios nombres o datos

print(alumnos10_3)

print(alumnos10_3.index("dylan"))  #me dira en que posicion esta lo que se pidio en el index

posicion=(alumnos10_3.index("allison"))

alumnos10_3.insert(posicion,"daniel")   #para ingresar un dato en la posicion que indico anteriormente

print(len(alumnos10_3))   #PARA SABER CUANTOS PRODUCTOS AHI EN ESA LISTA

print(alumnos10_3)


print("ronald" in alumnos10_3)  #esto le pregunta al sistema si esta ese nombre en la lista

print(alumnos10_3.sort())


alumnos10_4.remove(6)
alumnos10_3.pop(posicion)

print(alumnos10_4)
print(alumnos10_3)






