class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def Envelhecer(self, ano):
        self.idade += ano
        if self.idade > 21:
            self.crescer(0.5 * ano)
        
    def Engordar(self, peso_ganho):
        self.peso += peso_ganho
        
    def Emagrecer(self, peso_perdido):
        self.peso -= peso_perdido
        
    def Crescer(self, altura_ganha):
        self.altura += altura_ganha
        
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos, Peso: {self.peso} kg, Altura: {self.altura} cm"
        
Informacoes_Pessoa = Pessoa("Brenno", 18, 60, 172)
print("Informacoes 1:", Informacoes_Pessoa)
Informacoes_Pessoa.Envelhecer(2)
Informacoes_Pessoa.Engordar(8)
Informacoes_Pessoa.Emagrecer(2)
Informacoes_Pessoa.Crescer(4)
print("Informacoes 2:", Informacoes_Pessoa)
