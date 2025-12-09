#### Exercício 24

#### Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#### - par ou ímpar;
#### - positivo ou negativo;
#### - inteiro ou decimal.

# Leitura dos números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
# Leitura da operação desejada
operacao = input("Qual operação você deseja realizar? (+, -, *, /): ")
# Realização da operação
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        exit()
else:
    print("Operação inválida.")
    exit()
# Verificação das características do resultado
if resultado % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"
if resultado > 0:
    sinal = "positivo"
elif resultado < 0:
    sinal = "negativo"
else:
    sinal = "neutro"
if resultado.is_integer():
    tipo = "inteiro"
else:
    tipo = "decimal"
# Exibição do resultado com as características
print(f"O resultado da operação é {resultado}, que é {paridade}, {sinal} e {tipo}.")