#### Exercício 16

#### Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# Solicita o tamanho da área a ser pintada
area_m2 = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
# Define a cobertura da tinta e o preço da lata
cobertura_por_litro = 3  # metros quadrados por litro
litros_por_lata = 18  # litros por lata
preco_por_lata = 80.00  # preço por lata em reais
# Calcula a quantidade de tinta necessária
litros_necessarios = area_m2 / cobertura_por_litro
# Calcula a quantidade de latas necessárias (arredondando para cima)
import math
latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)
# Calcula o preço total
preco_total = latas_necessarias * preco_por_lata
# Exibe o resultado para o usuário
print(f"Você precisará comprar {latas_necessarias} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")