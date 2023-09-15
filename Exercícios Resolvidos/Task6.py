#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Loop para calcular e exibir a tabuada
for i in range(1, 11):  # Loop de 1 a 10
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
