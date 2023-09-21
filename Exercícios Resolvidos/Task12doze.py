#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota1 = int(input("Digite uma nota de 0 a 10: "))
    if nota1 >= 0 and nota1 <= 10:
        break
    else:
        print("Nota inválida, digite novamente!")

print("Nota válida inserida:", nota1)
