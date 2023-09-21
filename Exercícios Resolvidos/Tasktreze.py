#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def imprimir_numeros_impares():
    for numero in range(1, 51):
        if numero % 2 != 0:
            print(numero)

imprimir_numeros_impares()
