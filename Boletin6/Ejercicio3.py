numeros = []



for i in range (10):
    numero = int(input(f"Dime un numero del 1 al 10  "))
    numeros.append(numero)
    numeros_lista = sorted(numeros, reverse=True)

print ("\nLa lista de numeros es:" , numeros_lista)