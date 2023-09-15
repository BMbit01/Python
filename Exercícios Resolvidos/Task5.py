#Escreve um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Solicita ao usuário que insira um valor em metros
metros = float(input("Digite um valor em metros: "))

# Converte metros para centímetros e milímetros
centimetros = round(metros * 100, 2)
milimetros = round(metros * 1000, 2)

# Exibe o resultado
print(f"{metros} metros equivalem a {centimetros} centímetros.")
print(f"{metros} metros equivalem a {milimetros} milímetros.")
