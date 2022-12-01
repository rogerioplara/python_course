"""
Funções - def em python (parte 1)
"""


# cria a função e define um parâmetro, nesse caso tudo que for escrito dentro da chamada, será impresso pela função
def funcao(msg):
    print(msg)


funcao('Mensagem')  # argumentos passados para a função
funcao('Olá')
funcao('Mundo')
funcao('!')
print()


def saudacao(msg, nome):
    print(msg, nome)


# possível usar a função para passar os parâmetros em ordem, se deixar vazio gera erro
saudacao('Olá', 'Rogerio Peres Lara')
saudacao('Olá', 'Luís')
saudacao('Hello', 'Rogerio')
saudacao('Bonjour', 'Priscilla')
saudacao('Hi', 'Priscilla')
print()


def saudacao2(msg='Olá', nome='usuário'):  # Dessa forma, define um valor DEFAULT se não passar nenhnum argumento
    nome = nome.replace('e', '3')  # troca a letra E pelo numero 3
    msg = msg.replace('e', '3')
    print(msg, nome)


saudacao2()
saudacao2('Olá', 'Luís')
saudacao2('Hello', 'Rogerio')
saudacao2('Bonjour', 'Priscilla')
saudacao2('Hi', 'Priscilla')
# pode ser chamado passando os argumentos nomeados
saudacao2(nome='Zezinho')
saudacao(nome='Rogerio', msg='Hello')
print()


def saudacao3(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'  # dessa forma, a função retorna um valor e depois atribuo a variavel


variavel = saudacao3()
print(variavel)
