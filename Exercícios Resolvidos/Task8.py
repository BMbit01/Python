#Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

# Solicita ao usuário que insira o preço do produto
preco_original = float(input("Digite o preço do produto: "))

# Calcula o novo preço com 5% de desconto
desconto = 0.05  # 5% em forma decimal
novo_preco = preco_original - (preco_original * desconto)

# Exibe o novo preço com desconto
print(f"O novo preço com 5% de desconto é: R$ {novo_preco:.2f}")
