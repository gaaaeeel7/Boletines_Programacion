#Pida al usuario que escriba varias palabras separadas por comas.
#Guarde esas palabras en una lista.
#Recorra la lista con un bucle y:
#Si una palabra tiene 5 o más letras, la añada a una tupla llamada largas.
#Si tiene menos de 5 letras, la añada a otra tupla llamada cortas.
#Finalmente, muestre:
#Cuántas palabras escribió el usuario.
#Las palabras largas y cortas por separado



lista = ['casa', 'ordenador', 'sol', 'montaña', 'rio', 'gato']

for palabras in lista:
    if len(palabras) > 5:
        print("Esto es una palabra larga" )
    else:
        print ("Esto es una palabra corta ")