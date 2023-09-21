#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido caso seja informado uma letra inválida

sexo = input("Digite uma letra (F para feminino, M para masculino): ")

if sexo == "F" or sexo == "f":
  print("F - Feminino")
elif sexo == "M" or sexo == "m":
  print("M - Masculino")
else:
  print("Sexo Inválido")
