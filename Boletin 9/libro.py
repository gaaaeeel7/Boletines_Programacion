class Libro:
    def __init__(self, titulo, autor, ano, numPaginas, valoracion):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.numPaginas = numPaginas
        self.valoracion = valoracion

#Estas funciones son para getters
    def titulo(self):
        return self.titulo

    def autor(self):
        return self.autor

    def ano(self):
        return self.ano

    def valoracion(self):
        return self.valoracion

# Estas funciones son para Setters

    def titulo(self, valor):
        self.titulo = valor

    def autor (self, valor):
        self.autor = valor

    def ano(self, valor):
        self.ano = valor

    def numPaginas(self, valor):
        self.numPaginas = valor

    def valoracion(self, valor):
        self.valoracion = valor


    def amosar_libro(self):
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Ano: {self.ano}\n"
            f"numPaginas : {self.numPaginas}\n"
            f"Valoracion: {self.valoracion}\n"
        )
