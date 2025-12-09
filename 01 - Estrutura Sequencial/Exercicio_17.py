#### Exercício 17

#### Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#### - Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#### - comprar apenas latas de 18 litros;
#### - comprar apenas galões de 3,6 litros;
#### - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litros_necessarios = area / 6
litros_necessarios_com_folga = litros_necessarios * 1.1
# Comprar apenas latas de 18 litros
latas_18l = math.ceil(litros_necessarios_com_folga / 18)
custo_latas_18l = latas_18l * 80.00
print(f"Comprando apenas latas de 18 litros: {latas_18l} latas, custo total: R$ {custo_latas_18l:.2f}")
# Comprar apenas galões de 3,6 litros
galoes_3_6l = math.ceil(litros_necessarios_com_folga / 3.6)
custo_galoes_3_6l = galoes_3_6l * 25.00
print(f"Comprando apenas galões de 3,6 litros: {galoes_3_6l} galões, custo total: R$ {custo_galoes_3_6l:.2f}")
# Misturar latas e galões
latas_mistas = math.floor(litros_necessarios_com_folga / 18)
litros_restantes = litros_necessarios_com_folga - (latas_mistas * 18)
galoes_mistos = math.ceil(litros_restantes / 3.6)
custo_misto = (latas_mistas * 80.00) + (galoes_mistos * 25.00)
print(f"Misturando latas e galões: {latas_mistas} latas e {galoes_mistos} galões, custo total: R$ {custo_misto:.2f}")