#### Exercício 08

#### Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

# Solicita o preço dos três produtos ao usuário
preco1 = float(input("Digite o preço do primeiro produto: R$ "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))
# Inicializa variáveis para armazenar o menor preço e o produto correspondente
menor_preco = preco1
produto_mais_barato = "primeiro produto"
# Compara o preço do segundo produto com o menor preço atual
if preco2 < menor_preco:
    menor_preco = preco2
    produto_mais_barato = "segundo produto"
# Compara o preço do terceiro produto com o menor preço atual
if preco3 < menor_preco:
    menor_preco = preco3
    produto_mais_barato = "terceiro produto"
# Exibe o resultado para o usuário
print(f"O produto mais barato é o {produto_mais_barato} com o preço de R$ {menor_preco:.2f}.")