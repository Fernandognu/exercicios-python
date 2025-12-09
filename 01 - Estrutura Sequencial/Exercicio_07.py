#### Exercício 07

#### Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# Solicita ao usuário o valor do lado do quadrado
lado = float(input("Digite o valor do lado do quadrado: "))
# Calcula a área do quadrado
area = lado ** 2
# Calcula o dobro da área
dobro_area = area * 2
# Exibe o resultado para o usuário
print("O dobro da área do quadrado é:", dobro_area)