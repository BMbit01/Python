#Faça um Programa que leia três números e mostre o maior e o menor deles.

def encontrar_maior_e_menor():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

    maior = numero1
    menor = numero1

    # Encontra o maior número
    if numero2 > maior:
        maior = numero2
    if numero3 > maior:
        maior = numero3

    # Encontra o menor número
    if numero2 < menor:
        menor = numero2
    if numero3 < menor:
        menor = numero3

    print(f"O menor número é {menor}")
    print(f"O maior número é {maior}")

encontrar_maior_e_menor()
