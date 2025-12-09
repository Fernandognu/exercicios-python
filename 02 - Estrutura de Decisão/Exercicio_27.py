#### Exercício 27

#### Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#### ```
####                 Até 5 Kg                Acima de 5 Kg
#### Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#### Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#### ```

#### Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Leitura das quantidades de frutas
kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))
# Definição dos preços por Kg
if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20
if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50
# Cálculo do valor total
valor_total = (kg_morango * preco_morango) + (kg_maca
    * preco_maca)
# Verificação de desconto
if (kg_morango + kg_maca) > 8 or valor_total > 25.00:
    valor_total *= 0.90  # Aplica desconto de 10%
# Exibição do valor a ser pago
print(f"O valor a ser pago pelo cliente é: R$ {valor_total:.2f}")