#### Exercício 18

#### Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)
data_valida = True
if ano < 1:
    data_valida = False
elif mes < 1 or mes > 12:
    data_valida = False
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia < 1 or dia > 31:
            data_valida = False
    elif mes in [4, 6, 9, 11]:
        if dia < 1 or dia > 30:
            data_valida = False
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia < 1 or dia > 29:
                data_valida = False
        else:
            if dia < 1 or dia > 28:
                data_valida = False
if data_valida:
    print("Data válida")
else:
    print("Data inválida")