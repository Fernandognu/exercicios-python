#### Exercício 01

#### Faça um programa que peça dois números e imprima o maior deles.

# Solicita ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
# Compara os números e imprime o maior
if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Os dois números são iguais.")