m = int(input("Cuántos números vas a ingresar? "))

for i in range(1, m + 1):
    num = int(input(f"Número {i}: "))
    factorial = 1
    for c in range(1, num + 1):
        factorial *= c
    print(i, "-", factorial)