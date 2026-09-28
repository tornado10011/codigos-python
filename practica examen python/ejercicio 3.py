import os
os.system("cls")

usuarios=["Carlos","Maria","Luis","Ana","Pedro"]

nombre_de_usuario=input("Escriba el nombre de usuario: ")

for i in usuarios:
    usuario=nombre_de_usuario.capitalize()
    if usuario in usuarios:
        print(f"usuario encontrado: {nombre_de_usuario}")
        break
    else:
        print("usuario no encontrado")
        break