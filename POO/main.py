from cilindro import Cilindro
from persoa import Persoa
from esfera import Esfera
from coche import Coche
from libro import Libro

# Libro
def main():
    # Crear un libro
    libro1 = Libro("O Señor dos Aneis", "J.R.R. Tolkien", 1954, 1216, 9.8)

    # Amosar información
    print(libro1.amosar_libro())

    libro1.titulo = "El Hobbit"
    libro1.valoracion = 9.5

    print("\nDESPOIS DE CAMBIAR DATOS:")
    print(libro1.amosar_libro())

if __name__ == "__main__":
    main()


print ("")
print("")
# Coche

c1 = Coche("BMW", 3)
c1.avanzar()
print(c1.gasolina)

print ("")
print("")

#Persoa
manuel = Persoa ("Manuel",
                 dni ="00000000T",
                 nacionalidade = "Española",
                 direccion="Garcia Barbon 48",
                 edade= 30)
print (manuel)


print ("")
print("")


#Esfera
radio = float(input("Ingresa el radio de la esfera: "))
mi_esfera = Esfera(radio)
print(f"El volumen de la esfera es: {mi_esfera.volumen():.2f}")
print(f"El área de la superficie de la esfera es: {mi_esfera.area_superficie():.2f}")


print ("")
print("")


#Cilindro
radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))

cilindro = Cilindro(radio, altura)
cilindro.mostrar_nombre()
print(f"Volumen: {cilindro.volumen():.2f}")
print(f"Área de superficie: {cilindro.area_superficie():.2f}")

