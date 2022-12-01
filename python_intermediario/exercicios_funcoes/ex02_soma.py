"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""
entra = input('Digite 3 números separados por espaços: ').split(' ')
a, b, c = entra


def convert(a2, b2, c2):
    try:
        a2 = int(a2)
        b2 = int(b2)
        c2 = int(c2)
        print(a2 + b2 + c2)
    except:
        print('Números inválidos')
        exit()

    return a2 + b2 + c2


convert(a, b, c)
