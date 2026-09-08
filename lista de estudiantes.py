estudiantes=["jose","veronica","santiago","dylan","leonardo","mathias","daniel","miguel"]    #lista original de estudiantes
present=[]    #lista nueva para los presentes
ausente=[]    #lista nueva para los ausentes

for estudiante in estudiantes:
    pregun=input(f"presione 1 si {estudiante} esta presente, si no presione 2: ")    #aqui pregunta si esta presente o no a la lista original de estudiantes
    if pregun=="1":
        present.append(estudiante)
        print(f"el estudiante esta presente, se añadira a la lista de estudiantes presentes \n{present}\n")     #aqui me muestra un mensaje que se añadio a la lista correspondiende y mostrara como va la lista
    else:
        ausente.append(estudiante)
        print(f"el estudiante no esta presente, se añadira en la lista de ausentes \n{ausente}\n")
print(f"\n los estudiantes presente son: {present} \n y los ausentes son: {ausente}")    #mostrara un mensaje final con todos los estudiantes presentes y ausentes


