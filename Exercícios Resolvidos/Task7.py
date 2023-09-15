# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$ 1.00 = R$ 5.10

# Solicita ao usuário que insira a quantidade de dinheiro em reais
reais = float(input("Digite a quantidade de dinheiro em reais: "))

# Define a taxa de câmbio
taxa_de_cambio = 5.10

# Converte o dinheiro em reais para dólares e arredonda para 2 casas decimais
dolares = round(reais / taxa_de_cambio, 2)

# Mostra a quantidade de dólares que a pessoa pode comprar
print("Com", reais, "reais, você pode comprar aproximadamente", dolares, "dólares.")
