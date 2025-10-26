texto = int(input("Dime el numero de tu DNI"))

letras = "TRWAGMYFPDXBNJZSQVHLCKE"

letra= letras [texto % 23]


print ("Esta es la letra de tu DNI", letra)