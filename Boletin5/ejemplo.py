
base = 4
altura = 3

def crearMenu():
    print ("1. Triangulo")
    print ("2. Rectangulo")
    print ("3. Circulo")
    print ("4. Sair")
    print ("Elixa a opcion correcta")
def calcularAreaRectangulo(base,altura):
    return base * altura
def calcularAreaTriangulo(base,altura):
    area = calcularAreaRectangulo(base, altura)/2
    return area



print ("Esta es el area del rectangulo",calcularAreaRectangulo(base, altura))


#Boletin 4.2
def recollerParametros(opcion):
    base = int(input("Introduce la base:"))
    altura = int (input("Introduce la altura"))
    return base, altura

opcion = 0
while opcion != 4:
    crearMenu()
    opcion = int (input("Escribe una opcion:"))
    if opcion > 0 and opcion < 5:
        if opcion == 1 or opcion == 2:
            base, altura = recollerParametros (opcion)
            if opcion == 1:
                area = calcularAreaRectangulo (base, altura)
                print ("O area do rectangulo é: ", area)
                if opcion == 2:
                    area = calcularAreaTriangulo(base, altura)
                    print ("O area do triangulo é: ", area)