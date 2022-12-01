"""
Operador ternário em Python
"""

logged_user = False  # simula se o usuário está logado ou não

# FORMA TRADICIONAL DE SER FAZER COM UM IF
# if logged_user:  # if logged_user == true:
#     msg = 'Usuário logado'
# else:
#     msg = 'Usuário não logado'
#
# print(msg)

# OPERADOR TERNÁRIO, TAMBÉM CHAMADO DE IF DE UMA LINHA
msg = 'Usuário logado.' if logged_user else 'Usuário deslogado.'
# possível usar mais de uma condição, colocar entre parênteses
print(msg)
print()

idade = input('Qual a sua idade? ')
if not idade.isnumeric():  # checa se o valor do input é numérico
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    msg = 'Pode acessar.' if maior_idade else 'Não pode acessar.'
    print(msg)
