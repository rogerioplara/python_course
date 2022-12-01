"""
Desempacotamento de listas
"""
lista = ["Luiz", "João", "Maria", 1, 2, 3, 4, 5, 6, 7]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista  # atribui os dois primeiros valores para n1 e n2 e o restante para a
# outra_lista -> pode ser manipulado de qualquer forma
# o * (asterisco) funciona como um select *
# caso não queira utilizar os outros valores da lista, utiliza-se *_ como placeholder para os outros índices da lista
print(n1, n2, n3, outra_lista, ultimo_da_lista)
print()
n1, n2, *_ = lista
print(n1, n2)
