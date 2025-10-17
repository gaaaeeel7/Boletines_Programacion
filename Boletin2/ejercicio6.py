tarifa = int(input("Dime el precio de tarifa"))
pagado = int(input("Dime el precio pagado"))

descuento = ((tarifa - pagado) / tarifa) * 30

print ("Dame el descuento que tiene el producto", descuento)