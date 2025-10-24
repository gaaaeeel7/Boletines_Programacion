palabra = input("Añade una palabra")

palabra = palabra.lower()


a = palabra.count ("a")
e = palabra.count ("e")
i = palabra.count ("i")
o = palabra.count ("o")
u = palabra.count ("u")

print ("¿Cuantas veces sale cada vocal?")

print (f"a: {a}")
print (f"e: {e}")
print (f"i: {i}")
print (f"o: {o}")
print (f"u: {u}")