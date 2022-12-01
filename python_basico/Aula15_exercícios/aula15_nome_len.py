"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto;
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
Maior que 6 escreva "Seu nome é muito grande.
"""

nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print(f'Seu nome tem {len(nome)} letras e é um nome curto!')
elif 5 <= len(nome) <= 6:
    print(f'Seu nome tem {len(nome)} letras e tem um tamanho normal!')
else:
    print(f'Seu nome tem {len(nome)} letras e é muito grande!')
