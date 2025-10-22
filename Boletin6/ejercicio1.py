asignaturas = ["Matematicas","Fisica","Quimica","Historia","Lengua"]

notas = []

for asignatura in asignaturas:
    nota = input(f"Dime la nota que sacaste {asignatura}: ")
    notas.append(nota)


print("\nResultados: ")
for i in range(len(asignaturas)):
 print(f"En {asignaturas[i]} sacaste {notas[i]}: ")