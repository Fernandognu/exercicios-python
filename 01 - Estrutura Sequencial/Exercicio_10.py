#### Exercício 10

#### Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# Solicita a temperatura em graus Celsius ao usuário
celsius = float(input("Digite a temperatura em graus Celsius: "))
# Converte a temperatura para graus Fahrenheit
fahrenheit = (celsius * 9/5) + 32
# Exibe a temperatura convertida
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}°F")