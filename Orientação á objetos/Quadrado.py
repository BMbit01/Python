class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def retornarLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado ** 2

# Exemplo de uso da classe Quadrado:
meu_quadrado = Quadrado(5)
print("Lado do quadrado:", meu_quadrado.retornarLado())
print("Area do quadrado:", meu_quadrado.calcularArea())

meu_quadrado.mudarLado(7)
print("Novo lado do quadrado:", meu_quadrado.retornarLado())
print("Nova area do quadrado:", meu_quadrado.calcularArea())
