"""
3 - Crie uma função que receba 2 números. O primeiro é um valor inteiro e o segundo um valor percentual.
Retorne o valor do primeiro número somado do aumento percentual
"""
num1 = input('Digite um número: ')
perc1 = input('Digite a porcentagem de incremento: ')


def convert(num, perc):
    try:
        num = float(num)
        perc = float(perc)
    except:
        print('Números inválidos.')
        exit()

    return num * ((perc / 100.0) + 1)


print(convert(num1, perc1))
