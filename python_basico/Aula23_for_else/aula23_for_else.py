"""
FOr / Else em python
"""

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

print('Exemplo 1')
for valor in variavel:
    print(valor)
    continue  # muda para a próxima iteração do laço (para cima) e não executa o que está em baixo
    # break sai do laço e acaba a iteraçao do FOR
    print(valor)

print()
print('Exemplo 2')
for value in variavel:
    if value.startswith('J'):  # case-sensitive
        print('Começa com J', value)  # checagem se qualquer item da lista começa com J
    else:
        print('Não começa com J', value)

print()
print('Exemplo 3')
comeca_com_j = False
for val in variavel:
    if val.lower().startswith('j'):  # converte todos os itens da lista para minúsculo / deixa de ser case-sensitive
        comeca_com_j = True  # muda o valor da variável comeca_com_j para true

if comeca_com_j:  # checa se a variavel comeca_com_j é TRUE
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

print()
print('Exemplo 4')  # mesmo exemplo do anterior porém com FOR/ELSE
for va in variavel:
    print(va)  # imprime o valor onde a iteração vai parar
    if va.lower().startswith('j'):  # converte todos os itens da lista para minúsculo / deixa de ser case-sensitive
        print('Existe uma palavra que começa com J.')
        break
else:
    print('Não existe uma palavra que começa com J.')
