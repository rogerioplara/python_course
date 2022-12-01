"""
len = LENGTH
quantidade de caracteres
"""

usuario = input('Digite seu usuário: ')  # input do usuário
qtd_caracteres = len(usuario)  # contagem de caracteres e atribui à variável qtd_caracteres
print(usuario, qtd_caracteres, type(qtd_caracteres))  # mostra do andamento do código

if qtd_caracteres < 6:  # checagem do requisito de tamanho do usuário
    print('O usuário deve ter ao menos 6 caracteres!')
else:
    print('Cadastrado com sucesso!')

# Soma de strings

string1 = input('Digite algo: ')
string2 = input('Digite outra coisa: ')
print(f'A quantidade total de caracteres digitado foi de {len(string1) + len(string2)}')  # pode-se usar direto no {}
# INT, FLOAT E BOOL não possuem LEN
