iniciales_prohibidas = ('X','Z')
nombres_registrados = []
total_nombres = int(input('Cuantos nombres deseas registrar?: '))
for i in range(total_nombres):
    nombre = input('Introduce el nombre: ')
    if nombre == "":
        print ("Debes escribir un nombre")


