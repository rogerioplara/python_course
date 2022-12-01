"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome
"""
inp1 = input('Digite seu nome: ')
inp2 = input('Digite o horário do dia (m, t, n): ')


def saudacao(nome, saut):
    if saut == 'm':
        saut = 'Bom dia'
    elif saut == 't':
        saut = 'Boa tarde'
    elif saut == 'n':
        saut = 'Boa noite'
    return f'{saut}, {nome}'


print(saudacao(inp1, inp2))
