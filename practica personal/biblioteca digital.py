import os
os.system("cls")


libros={
    "python": 3000,
    "javascript": 2500,
    "html": 2000
}

precios=libros.values()
nombre_de_libros=libros.keys()
libros_prestados=[]

print("bienvenido a la biblioteca digital\n")

while True:
    opcion=int(input("""
presione 1 si quiere pedir un libro
presione 2 si quiere ver los libros prestados
presione 3 si quiere devolver el ultimo libro
presione 4 si quiere salir del programa\n\n
indique aqui que desea realizar: """))
    
    if opcion==1:
        print(f"estos son los libros que tenemos actualmente {nombre_de_libros} y con un precio de {precios}\n")
        escoger_libro=input("Digite el nombre del libro a pedir: ")
        libros_prestados.append(escoger_libro)
        print(f"se pidio el libro {escoger_libro} \nllevas un total de {len(libros_prestados)} libros prestados.")
        os.system("pause")
        os.system("cls")

    elif opcion==2:
        print(f"a continuacion se mostraran los libros prestados. \n\nlos libros prestados son {libros_prestados}")
        os.system("pause")
        os.system("cls")

    elif opcion==3:
        print("se devolvera el ultimo libro que pidio")
        libros_prestados.pop()
        print(f"se elimino el libro {escoger_libro}")
        os.system("pause")
        os.system("cls")

    elif opcion <0 or opcion >4:
        print("usted no indico correctamente lo que desea realizar, intente de nuevo")
        os.system("pause")
        os.system("cls")

    elif opcion==4:
        print("el programa sera finalizado.")
        break
