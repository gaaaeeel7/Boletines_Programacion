palabra = input ("Pon una palabra")

palabra_limpia = palabra.lower()

if palabra_limpia == palabra_limpia[::-1]:
    print ("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")
