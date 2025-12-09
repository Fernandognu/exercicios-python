#### Exercício 10

#### Faça um programa que pergunte em que turno você estuda. Peça para digitar: 

#### - M - Matutino
#### - V - Vespertino
#### - N - Noturno.

#### Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Em que turno você estuda? Digite M (Matutino), V (Vespertino) ou N (Noturno): ").strip().upper()
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")