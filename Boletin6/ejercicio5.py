abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","v","w","x","y","z"]

letras = []

for i in range(len(abecedario)):
    if (i+1) % 3 != 0:
        letras.append(abecedario[i])

print("Esta es la lista" , letras)