numeros = []

for i in range (6):
    numero = int(input(f"Dime el numero ganador {i + 1}: "))
    numeros.append(numero)
    numeros_menoramayor = sorted(numeros)

print ("\nLos que ganaron son:" , numeros_menoramayor)