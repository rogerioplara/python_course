"""
For in em python
Iterando strings com for
Função range(start = 0, stop, step = 1)
"""
texto = 'Python'

# for letra in texto:
#     print(letra)

for numero in range(0, 10, 1):  # (inicio, fim, passo) inicio e passo é padrão 0 e 1;
    print(numero)

print(' ')

for n in range(100):
    if n % 8 == 0:
        print(n)

print(' ')

# continue - pula para o próximo laço
# break - termina o laço
nova_string = ''
for letra in texto:
    if letra == 't':
        continue  # tira a letra t da string
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break  # fecha o loop quando encontrar a letra h
    else:
        nova_string += letra

print(nova_string)
