class TV:
    def __init__(self, canal_inicial=1, volume_inicial=10):
        self.canal = canal_inicial
        self.volume = volume_inicial

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:  # Faixa válida de canais
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal fora da faixa válida.")

    def aumentar_volume(self):
        if self.volume < 100:  # Volume máximo é 100
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")

    def diminuir_volume(self):
        if self.volume > 0:  # Volume mínimo é 0
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")

# Exemplo de uso:
tv = TV()

while True:
    print("\nOpções:")
    print("1. Mudar canal")
    print("2. Aumentar volume")
    print("3. Diminuir volume")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        novo_canal = int(input("Digite o novo canal: "))
        tv.mudar_canal(novo_canal)
    elif escolha == '2':
        tv.aumentar_volume()
    elif escolha == '3':
        tv.diminuir_volume()
    elif escolha == '4':
        print("Você desligou a TV")
        break
    else:
        print("Opção inválida. Tente novamente.")
