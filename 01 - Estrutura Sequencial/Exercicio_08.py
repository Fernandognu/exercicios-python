#### Exercício 08

#### Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# Solicita o valor ganho por hora ao usuário
valor_hora = float(input("Digite quanto você ganha por hora: "))
# Solicita o número de horas trabalhadas no mês ao usuário
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
# Calcula o salário mensal
salario_mensal = valor_hora * horas_trabalhadas
# Exibe o salário mensal calculado
print(f"Seu salário no mês é: R$ {salario_mensal:.2f}")