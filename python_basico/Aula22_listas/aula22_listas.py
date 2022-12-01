"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max, range

texto = 'Valor'
lista = [1, 2, 3, 4, 'Rogerio', True, 10.5]  # uma lista comporta qualquer tipo;
# índices  0    1    2    3    4   5
lista2 = ['A', 'B', 'C', 'D', 'E', 10.5]
# índices -6   -5   -4   -3   -2   -1
lista2[5] = 'Qualquer outra coisa'  # altera o item da lista baseado no índice
string = 'ABCDE'
print(string[1])  # acessa o índice 1 a variável string
print(string[-1])

print(lista2[1])
print(lista2[-1])  # último número da lista

print(lista2[2:])  # começa do índice 2 até o fim
print(lista2[::2])  # começa do 0 até o fim pulando de 2 em 2
print(lista2[::-1])  # inverte  a lista / pode ser usado com string
"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2  # concatena as 2 listas
print(l3)
print(l1)
print(l2)
l1.extend(l2)  # adiciona l2 a l1
print(l1)
l1.extend('a')  # adiciona 'a' a l1
print(l1)

l2.append('b')  # mais usado para adicionar valores a lista
print(l2)
print(l2[3])

l2.insert(0, 'banana')  # adiciona um item ao índice escolhido
print(l2)

l2.pop()  # remove o último valor da lista
print(l2)

l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l4)
print(' ')
del(l4[3:5])  # remove os itens de índice 3 e 4 - fatiamento
print(l4)
l4.insert(0, 'banana')
print(l4)
del(l4[0])
print(l4)

print(max(l4))  # busca o maior valor da lista - serve para números
print(min(l4))  # busca o menor valor da lista - serve para números

# função do python built-in para criar uma lista mais facilmente
l5 = list(range(0, 100, 3))  # list cria uma lista( range define um tamanho (valor inicial, valor final, passo)
print(l5)

for valor in l5:  # iteração da lista mostrando os valores definidos item a item
    print(valor)

soma = 0
for valor in l5:  # soma de todos os valores da lista
    soma = soma + valor

print(soma)

l6 = ['String', True, 10, -20.5]
for elem in l6:  # mostra os tipos dos valores da lista
    print(f'O tipo de {elem} é {type(elem)}')


