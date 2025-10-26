cadena = "Java Java Java"
nueva_cadena = " "

a = 0
e = 0

for letra in cadena:
    if letra == "a":
        nueva_cadena +=  "e"
    else:
        nueva_cadena += letra

print ("Esta es la palabra nueva")
print (nueva_cadena)