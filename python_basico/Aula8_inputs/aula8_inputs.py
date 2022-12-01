"""
Entrada de dados
"""
# Sempre o valor que o usuário digitar será reconhecido como STRING;
nome = input('Qual o seu nome? ')
print(f'O usuário digitou {nome} e o tipo da variável é {type(nome)}')
idade = input('QUal a sua idade? ')
print(f'O usuário digitou {idade} e o tipo da variável é {type(idade)}')  # ambos são reconhecidos como strings;

ano_nascimento = 2022 - int(idade)  # para funcionar necessário fazer casting de variáveis (transformar em int)
print()  # pular linha
print(f'{nome} tem {idade} e nasceu em {ano_nascimento}')
print()

"""
Calculadora de soma
"""

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(numero_1 + numero_2)  # dessa forma concatena-se as variáveis como strings, necessário fazer um casting;
print(int(numero_1) + int(numero_2))  # pode ser feito dessa forma ou alterando a variável;

numero_3 = int(input('Digite um número: '))
numero_4 = int(input('Digite outro número: '))

print(numero_3 + numero_4)
