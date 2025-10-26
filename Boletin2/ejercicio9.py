cantidad = int(input("Introduce la cantidad de dinero"))

billete100 = cantidad // 100
cantidad = cantidad % 100


billete20 = cantidad // 20
cantidad = cantidad % 20


billete5 = cantidad // 5
cantidad = cantidad % 5


billete1 = cantidad // 1
cantidad = cantidad % 1

print ("Estos son los billetes de 100: ", billete100)
print ("Estos son los billetes de 20: ", billete20)
print ("Estos son los billetes de 5: ", billete5)
print ("Estos son los billetes de 1: ", billete1)
