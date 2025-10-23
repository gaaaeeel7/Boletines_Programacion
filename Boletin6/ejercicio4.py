asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notas = []
for asignatura in asignaturas:
    nota = int(input(f"Dime la nota que sacaste {asignatura}: "))
    notas.append(nota)

    if nota <5:
        print (f"Has suspendido {asignatura} con un {nota}: ")

print("\nResultados: ")
for i in range(len(asignaturas)):
        print(f"En {asignaturas[i]} sacaste {notas[i]}: ")
