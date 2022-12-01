"""
while
utilizado para realizar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

i = 0
while i < 10:  # condição
    if i == 3:
        i = i + 1
        continue  # pula para a próxima iteração do laço de repetição (para cima)
    print(i)
    i = i + 1  # incremento
print('Acabou!')

i = 0
while i < 10:  # condição
    if i == 3:
        break  # pula o laço de repetição quando a condição for alcançada (para baixo)
    print(i)
    i = i + 1  # incremento
print('Acabou!')

x = 0  # coluna


while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'({x},{y})')
        y += 1  # y = y + 1
    x += 1  # x = x + 1

print('Acabou!')

#  CALCULADORA SIMPLES

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')  # + - / *
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':  # gambiarra para sair do laço
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador Inválido!')
