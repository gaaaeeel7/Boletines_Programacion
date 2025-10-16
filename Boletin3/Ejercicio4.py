nombre1 = int(input("Escribe el nombre de la persona"))
peso1 = int (input("Escribe el peso de la persona"))

nombre2 = int(input("Escribe el nombre de la persona"))
peso2 = int (input("Escribe el peso de la persona"))

if peso1 > peso2:
    print ("El nombre 1 pesa mas")
    print ("Diferencia", peso1-peso2)

else:
    print ("El nombre 2 pesa mas")
    print ("Diferencia", peso2-peso1)
