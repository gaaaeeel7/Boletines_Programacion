from libro import Libro
from consumo import Consumo



coche = Consumo(km=150, litros=10, vMed=75, pGas=1.7)
print("Tempo da viaxe:", coche.getTempo(), "horas")
print("Consumo medio:", coche.consumoMedio(), "L/100km")
print("Consumo en euros:", coche.consumoEuros(), "€/100km")





print("")
print("")
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