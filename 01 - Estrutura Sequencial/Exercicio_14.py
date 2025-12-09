#### Exercício 14

#### João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# Leitura do peso dos peixes
peso = float(input("Digite o peso dos peixes em quilos: "))
limite = 50.0  # Limite de peso em quilos
multa_por_quilo = 4.0  # Valor da multa por quilo excedente
excesso = 0.0
multa = 0.0
# Cálculo do excesso e da multa
if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_por_quilo
    print(f"Excesso de peso: {excesso:.2f} quilos")
    print(f"Multa a pagar: R$ {multa:.2f}")
else:
    print("Não há excesso de peso. Nenhuma multa a pagar.")
