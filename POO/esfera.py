import math 
class Esfera:
    def __init__(self, radio):
        self.radio = radio

    def volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

    def area_superficie(self):
        return 4 * math.pi * (self.radio ** 2)