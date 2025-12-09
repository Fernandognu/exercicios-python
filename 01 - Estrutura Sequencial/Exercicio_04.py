#### Exercício 04

#### Faça um programa que peça as 4 notas bimestrais e mostre a média.

# Solicita as 4 notas bimestrais ao usuário
nota1 = float(input("Digite a primeira nota bimestral: "))
nota2 = float(input("Digite a segunda nota bimestral: "))
nota3 = float(input("Digite a terceira nota bimestral: "))
nota4 = float(input("Digite a quarta nota bimestral: "))
# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4
# Exibe a média calculada
print("A média das notas bimestrais é:", media)