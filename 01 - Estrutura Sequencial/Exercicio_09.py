#### Exercício 09

#### Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# Solicita a temperatura em Fahrenheit ao usuário
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
# Converte a temperatura para Celsius
celsius = (fahrenheit - 32) * 5.0/9.0
# Exibe a temperatura em Celsius
print(f"A temperatura em graus Celsius é: {celsius:.2f}°C")