estudiantes=["jose","veronica","santiago","dylan","leonardo","mathias",]
present=[]
ausente=[]

for estudiante in estudiantes:

    pregun=input(f"presione 1 si {estudiante} esta presente, si no presione 2: ")

    if pregun=="1":
        present.append(estudiante)
        print(f"el estudiante esta presente, se añadira a la lista de estudiantes presentes \n{present}")
    else:
        ausente.append(estudiante)
        print(f"el estudiante no esta presente, se añadira en la lista de ausentes \n{ausente}")
