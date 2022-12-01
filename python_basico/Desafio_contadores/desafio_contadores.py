"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
fazer 2 contadores no mesmo laço
"""
# primeiro crie o range do contador regressivo, utilizando a função range
# depois, encapsule o contador regressivo com enumerate, dessa forma imprimirá na tela da forma correta
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
