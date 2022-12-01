"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se esse número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro;
"""

num = input('Digite um número: ')

try:
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é ímpar')
except:
    print('Não é um número inteiro, tente novamente.')

# Pode ser feito com ifs aninhados
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é ímpar')
else:
    print('Não é um número inteiro, tente novamente.')
