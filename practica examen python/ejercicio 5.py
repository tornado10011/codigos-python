import os
os.system("cls")

computadora={
    "marca":"Dell",
    "ram":16,
    "disco":512
}

marca=(computadora.get("marca"))
ram=(computadora.get("ram"))

if ram>=16:
    print("la computadora tiene suficiente memoria RAM")

else:
    print("la computadora necesita mas memoria RAM.")

print(f"""\nla marca de la computadora es {marca}
la cantidad de ram que dispone es de {ram}""")