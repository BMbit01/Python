class conta_corrente:
    def __init__(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        pass
    
    def AlterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
        
    def Depósito(self, deposito):
        self.saldo += deposito
        
    def Saque(self, saque):
        if saque > 0 and saque <= self.saldo:
             self.saldo -= saque
             return True
        else:
            print("Saldo insuficiente ou valor inválido.")
            return False
    
Informacoes_conta = conta_corrente(44242-1, "Brenno Mendes Sousa", 3000.0)
print(f"Dados - Conta: {Informacoes_conta.numero_conta}, Nome: {Informacoes_conta.nome_correntista}, Saldo: {Informacoes_conta.saldo}")
    
Informacoes_conta.AlterarNome("Lucas Santos")
Informacoes_conta.Depósito(500.0)
Informacoes_conta.Saque(300.0)
print(f"Dados atualizados - Conta: {Informacoes_conta.numero_conta}, Nome: {Informacoes_conta.nome_correntista}, Saldo: {Informacoes_conta.saldo}")
