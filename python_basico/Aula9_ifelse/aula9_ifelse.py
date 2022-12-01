"""
Condições IF, ELIF e ELSE
"""

if False:
    print("Verdadeiro.")
    num_1 = 2
    num_2 = 4
    print(num_2 + num_1)
elif False:
    print('Agora é verdadeiro')
elif False:
    print('Mais uma verdadeira.')
else:
    print('Não é verdadeiro.')
# Encadeamento de if/elif/else

# jogo de dados simples para números aleatórios
dado = int(input('Insira um número aleatório: '))
resultado = dado % 6

if resultado == 0:
    print('1')
elif resultado == 1:
    print('2')
elif resultado == 2:
    print('3')
elif resultado == 3:
    print('4')
elif resultado == 4:
    print('5')
elif resultado == 5:
    print('6')
