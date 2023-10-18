class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, nova_cor):
        self.cor = nova_cor

    def mostrarCor(self):
        return self.cor

informacoes_bola = bola("Branca", 10, "Couro sintético")
print("Cor da bola:", informacoes_bola.mostrarCor())  

informacoes_bola.trocarCor("Azul")
print("Nova cor da bola:", informacoes_bola.mostrarCor())
