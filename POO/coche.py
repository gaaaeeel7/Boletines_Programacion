class Coche:
    def __init__(self,marca,gasolina):
        self.marca = marca
        self.gasolina = gasolina

    def avanzar(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("El coche avanza")
        else:
            print("No queda gasolina")