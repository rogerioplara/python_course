"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada;
"""

hora = input('Digite a hora: ')

try:
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 18:
        print('Boa tarde!')
    else:
        print('Boa noite!')
except:
    print('ERROR')

# Também pode ser feito com ifs aninhados
