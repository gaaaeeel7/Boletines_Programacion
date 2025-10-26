cadena = "Ola, son alumno de DAM1, e son programador desde o 2025"

letras = 0
digitos = 0
espacios = 0

for num in cadena:
    if num.isalpha():
        letras +=1
    elif num.isdigit():
        digitos +=1
    elif num == " ":
        espacios +=1

print ("Letras: " , letras)
print ("Digitos: ", digitos)
print ("Espacios: ", espacios)
