numero_1 = int(input("Pon el primer número"))
numero_2 = int(input("Pon el segundo número"))

for numeros in range(numero_1 + 1, numero_2 ):
    if numeros % 2 == 0:
        print (numeros)

