#### Exercício 14

#### Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

#### ```
#### Média de Aproveitamento  Conceito
#### Entre 9.0 e 10.0         A
#### Entre 7.5 e 9.0          B
#### Entre 6.0 e 7.5          C
#### Entre 4.0 e 6.0          D
#### Entre 4.0 e zero         E
#### ```

#### O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

# Leitura das notas parciais
nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))
# Cálculo da média
media = (nota1 + nota2) / 2
# Determinação do conceito e situação
if 9.0 <= media <= 10.0:
    conceito = 'A'
    situacao = 'APROVADO'
elif 7.5 <= media < 9.0:
    conceito = 'B'
    situacao = 'APROVADO'
elif 6.0 <= media < 7.5:
    conceito = 'C'
    situacao = 'APROVADO'
elif 4.0 <= media < 6.0:
    conceito = 'D'
    situacao = 'REPROVADO'
else:
    conceito = 'E'
    situacao = 'REPROVADO'
# Exibição dos resultados
print(f"Notas: {nota1} e {nota2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")