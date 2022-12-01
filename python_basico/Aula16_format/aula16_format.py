""""
Formatando valores com modificadores - Aula 5

:s - texto (strings)
:d - Inteiros (int)
:f - número de ponto flutuante (float)
:.(número)f - quantidade de casas decimais (float)
:(caractere)(> ou < ou ^) (quantidade)(tipo - s, d ou f) - define um tamanho específico
por exemplo um número que tenha 10 casas, preenchidos por 0

> - esquerda
< - direita
^ - centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')  # utilizando a função fstrings
nome = 'Rogerio PeReS Lara'
print(f'{nome:s}')

print(f'{num_1:0>10}')  # preenche com 0 o total de casas até 10 do lado esquerdo
print(f'{num_2:0<10}')  # preenche com 0 o total de casas até 10 do lado direito
print(f'{num_1:0^10}')  # preenche com 0 o total de casas até 10 e mantém o número no centro

num_3 = 1150
print(f'{num_3:0>10.2f}')  # aninhamento de formats

print(f'{nome:#^29}')  # pode ser usado com qualquer tipo
nome_formatado = '{:@>7}'.format(nome)  # só aparece caso seja maior que o tamanho da string usada
print(nome_formatado)

nome2 = 'Otávio'
sobrenome = 'Miranda'
nome_novo = '{0} {1:#^50}'.format(nome2, sobrenome)  # variáveis em linha separadas por vírgula
print(nome_novo)

print(nome.lower())  # tudo minúsculo
print(nome.upper())  # tudo maiúsculo
print(nome.title())  # primeiras letras maiúsculas
