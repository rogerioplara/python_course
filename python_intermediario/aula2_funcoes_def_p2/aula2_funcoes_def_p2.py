"""
Funções em python - RETURN
"""


def funcao(var):
    return var
# Ao encontrar o RETURN, o restante da função não será executada


variavel = funcao('Valor que eu quero passar para a função!')
# sempre que a função não encontrar um return, retorna um valor None (tipo de dado não valor)

if variavel:  # se a função retornar algum valor, será verdadeiro
    print(variavel)
else:
    print('Nenhum valor.')
print()


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2


divide = divisao(8, 0)  # gera um valor NONE pois está dividindo por zero

if divide:
    print(divide)
else:
    print('Conta inválida.')

print()


def divisao2(n1, n2):
    if n2 == 0:
        return  # se retornar verdadeiro, para nesse primeiro RETURN

    return n1 / n2  # se o if for falso, retorna este segundo RETURN (testar com o segundo parâmentro sendo zero


divide2 = divisao2(8, 2)

if divide2:
    print(divide2)
else:
    print('Conta inválida.')

print()


def dumb():
    return 1


def dumb1():
    return 1.1


def dumb2():
    return


def dumb3():
    return [1, 2, 3, 4, 5]


def dumb4():
    return 'Olá'


def dumb5():
    return True


def dumb6():
    return dumb


print(dumb(), type(dumb()))  # checagem do tipo de retorno que a fução retorna
print(dumb1(), type(dumb1()))  # checagem do tipo de retorno que a fução retorna
print(dumb2(), type(dumb2()))  # checagem do tipo de retorno que a fução retorna
print(dumb3(), type(dumb3()))  # checagem do tipo de retorno que a fução retorna
print(dumb6(), type(dumb6()))  # checagem do tipo de retorno que a fução retorna
print(dumb4(), type(dumb4()))  # checagem do tipo de retorno que a fução retorna
print(dumb5(), type(dumb5()))  # checagem do tipo de retorno que a fução retorna
# funções podem retornar QUALQUER COISA em python


def tupla():
    return ('Luiz', 'Otavio')  # neste caso os parênteses são redundantes


var = tupla()

print(var, type(var))
print(var[0], type(var))
print(var[1], type(var))

# tuplas são listas que não podem ser alteradas
