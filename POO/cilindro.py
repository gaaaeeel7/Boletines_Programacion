import math

class figura3D:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f"Figura: {self.nombre}")

class Cilindro(figura3D):
    def __init__(self, radio, altura):     # ← CORREGIDO
        super().__init__("Cilindro")
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return math.pi * (self.radio ** 2) * self.altura

    def area_superficie(self):
        return 2 * math.pi * self.radio * (self.altura + self.radio)

