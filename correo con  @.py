correo=str(input("digite su correo electronico: "))

for i in correo:
    if i == "@":
        email=True
    else:
        email=False
if email==True:
    print("correo correcto")
else:
    print("correo incorrecto")