#### Exercício 03

#### Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

#### - F - Feminino
#### - M - Masculino
#### - Sexo Inválido.

sexo = input("Digite uma letra (F para Feminino ou M para Masculino): ").upper()
if sexo == "F":
    print("Feminino")
elif sexo == "M":
    print("Masculino")
else:
    print("Sexo Inválido.")