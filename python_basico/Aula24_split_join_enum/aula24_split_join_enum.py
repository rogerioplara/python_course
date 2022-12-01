"""
Split, Join, Enumerate
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""
print('Função SPLIT')
string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista1 = string.split(' ')  # dividir a lista por espaços -> transforma a string em uma lista
lista2 = string.split(',')  # dividir a lista por vírgulas
print(lista1)
print(lista2)

print()
print('Exemplo 1')
for valor in lista1:  # iteração sobre a lista, mostra cada palavra em cada iteração do laço e quantas vezes apareceu
    print(f'A palavra {valor} apareceu {lista1.count(valor)} vez(es) na frase.')

print()
print('Exemplo 2')
palavra = ''
contagem = 0
for valor in lista1:  # iteração para contar qual palavra apareceu mais vezes e a quantidade de vezes
    qtd_vezes = lista1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

print()
print()

# função join

string = 'O Brasil é penta.'  # string básica
lista = string.split(' ')  # separa a string em uma lista separada por espaços
string2 = ','.join(lista)  # junta a lista com vírgulas, pode ser usado com qualquer caracter

print(string)
print(lista)
print(string2)
print()
print()

# função enumerate -> enumera a lista com seus respectivos valores

string = 'O Brasil é penta.'
lista = string.split(' ')

for index, valor in enumerate(lista):  # mostra na tela o índice e o valor de cada elemento da lista
    print(index, valor, lista[index])  # lista[index] -> mostra o valor da lista

# lista dentro de lista
lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for v in lista:  # imprime a lista de listas
    print(v)

print()

for v in lista:
    print(v[0], v[1])  # pega os índices 0 e 1 de dentro da lista

print()

lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria']
]

for indice, nome in lista:  # faz a mesma função de ENUMERATE
    print(indice, nome)

print()

for indice, nome in enumerate(lista):  # desempacotamento dos valores da lista
    print(indice, nome)

print()
lista3 = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista3  # desempacotamento do valor n2 da lista
print(n2)

print()
print()

lista = [
    #  0      1       2
    ['Edu', 'João', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Helena', 'Ed', 'Lu']  # 2
]

enumerada = list(enumerate(lista))  # pode ser feito um typecast com essa lista
print(list)

print(enumerada)  # imprime toda a lista com seus índices - IMPRIME TODAS AS TUPLAS DA LISTA
print(enumerada[1])  # imprime o índice 1 dentro da lista - IMPRIME SOMENTE A TUPLA DE ÍNDICE 1
print(enumerada[1][1])  # imprime o índice 1 dentro da lista, mostrando o valor sem o índice
print(enumerada[1][1][1])  # imprime o índice 1 dentro da lista de índice 1, valor 1 da lista 1

print()
print()

for v1, v2 in enumerate(lista):  # imprime a lista linha a linha com seus índices
    print(v1, v2)

print()

for v1, v2 in enumerate(lista, 53):  # imprime a lista linha a linha a partir da numeração definida (parametro start)
    print(v1, v2)

# enumerate é usado para ENUMERAR uma lista
print()

for v1 in enumerate(lista, 53):  # forma de desempacotar a lista
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2)
