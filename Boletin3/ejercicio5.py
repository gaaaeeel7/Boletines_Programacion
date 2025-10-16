dado1 = int(input("Dime el dado1: "))
dado2 = int(input("Dime el dado2: "))
dado3= int (input("Dime el dado 3: "))

if dado1 > dado2:
    print ("dado1 es mayor")
elif dado2 > dado3:
    print ("dado2 es mayor")
elif dado3 > dado1:
    print ("dado3 es mayor")
elif dado2 > dado1:
    print ("dado2 es mayor")
elif dado3 > dado2:
    print ("dado3 es mayor")